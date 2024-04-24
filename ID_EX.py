from globalvariables import *
from InstructionExtractor import InstructionExtractor
class ID_EX:

    def __init__(self):
        self.instruction = 0x0

        # Controls
        self.RegDST = 0
        self.ALUSrc = 0
        self.ALUOp = 0
        self.MemRead = 0
        self.MemWrite = 0
        self.Branch = 0
        self.MemToReg = 0
        self.RegWrite = 0

        self.SEOffset = 0
        self.incrPC = 0

        self.ReadReg1Value = 0
        self.ReadReg2Value = 0

        self.WriteReg_20_16 = 0
        self.WriteReg_15_11 = 0

        self.Func = 0x0
        self.opcode = 0x0
    def decode_mips_instruction(instruction):
        opcode = (instruction >> 26) & 0x3F
        if opcode == 0x00:  # R-type instructions
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            rd = (instruction >> 11) & 0x1F
            funct = instruction & 0x3F
            if funct == 0x20:  # add
                return f"[add ${rd}, ${rs}, ${rt}]"
            elif funct == 0x22:  # sub
                return f"[sub ${rd}, ${rs}, ${rt}]"
            else:
                return "unknown R-type instruction"
        elif opcode == 0x23:  # lw
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            immediate = sign_extend(instruction & 0xFFFF)
            return f"[lw ${rt}, {immediate},(${rs})]"
        elif opcode == 0x2B:  # sw
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            immediate = sign_extend(instruction & 0xFFFF)
            return f"[sw ${rt}, {immediate},(${rs})]"
        elif opcode == 0x04:  # beq
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            immediate = sign_extend(instruction & 0xFFFF)
            return f"[beq ${rs}, ${rt}, lable]"
        else:
            return "unknown instruction"
    def decode_instruction(self, instruction, incrPC):
        self.instruction = instruction
        self.incrPC = incrPC
        from InstructionExtractor import InstructionExtractor
        extractor = InstructionExtractor()
        opcode = extractor.extract_bits_from_instruction_26_31(instruction)
        self.opcode = opcode
        if opcode == 0: 
            src1 = extractor.extract_bits_from_instruction_21_25(instruction)
            src2 = extractor.extract_bits_from_instruction_16_20(instruction)
            dest = extractor.extract_bits_from_instruction_11_15(instruction)
            func = extractor.extract_bits_from_instruction_0_5(instruction)  # 确保在使用前赋值
    
            if func == 32 or func == 34: 
                self.RegDST = 1
                self.ALUSrc = 0
                self.MemToReg = 0
                self.RegWrite = 1
                self.MemRead = 0
                self.MemWrite = 0
                self.Branch = 0
                self.ALUOp = 0b10
    
                if func == 32:
                    self.Func = 0x20
                elif func == 34:
                    self.Func = 0x22
    
                self.WriteReg_20_16 = src2
                self.WriteReg_15_11 = dest
    
                self.ReadReg1Value = Regs[src1]
                self.ReadReg2Value = Regs[src2]


                self.SEOffset = -999 
       
        elif opcode == 7:  # Assuming 7 is the opcode for BEG
        # BEG-type instructions processing
            src1 = extract_bits_from_instruction_21_25(instruction)
            src2 = extract_bits_from_instruction_16_20(instruction)
            offset = extract_bits_from_instruction_0_15(instruction)

            self.RegDST = -999  # Not relevant for branch
            self.ALUSrc = 0     # Using values directly from registers
            self.MemToReg = -999  # Not relevant for branch
            self.RegWrite = 1  # register write-back
            self.MemRead = 0   # No memory read
            self.MemWrite = 0  # No memory write
            self.Branch = 1    # Branch is taken
            self.ALUOp = 0b01  # Set ALU to compare operation

            self.WriteReg_20_16 = -999  # Not used in this instruction
            self.WriteReg_15_11 = -999  # Not used in this instruction
            self.ReadReg1Value = Regs[src1 >> 21]
            self.ReadReg2Value = Regs[src2 >> 16]
            self.Func = -999   # Not applicable for BEG

            # Compute signed extension of offset
            self.SEOffset = twos_comp(offset) << 2  # Assuming offset needs to be shifted left by 2 (standard for MIPS)
    
            # Calculate Branch Target Address
            self.BTA = self.incrPC + self.SEOffset

        elif opcode == 0x23:  # Assuming 0x23 is the opcode for LW
            src1 = extractor.extract_bits_from_instruction_21_25(instruction)
            dest = extractor.extract_bits_from_instruction_16_20(instruction)
            offset = extractor.extract_bits_from_instruction_0_15(instruction)
        
            self.RegDST = 0
            self.ALUSrc = 1
            self.MemToReg = 1
            self.RegWrite = 1
            self.MemRead = 1
            self.MemWrite = 0
            self.Branch = 0
            self.ALUOp = 0b00
        
            self.WriteReg_20_16 = str(dest >> 16)
            self.WriteReg_15_11 = 0
            self.ReadReg1Value = Regs[src1 >> 21]
            self.ReadReg2Value = offset  # Assuming offset is used directly
            self.Func = -999
            self.SEOffset = extractor.twos_comp(offset)

        elif opcode == 0x2B:  # Assuming 0x2B is the opcode for SW
            src1 = extractor.extract_bits_from_instruction_21_25(instruction)
            dest = extractor.extract_bits_from_instruction_16_20(instruction)
            offset = extractor.extract_bits_from_instruction_0_15(instruction)
        
            self.RegDST = -999
            self.ALUSrc = 1
            self.MemToReg = -999
            self.RegWrite = 0
            self.MemRead = 0
            self.MemWrite = 1
            self.Branch = 0
            self.ALUOp = 0b00
        
            self.Func = -999
            self.WriteReg_20_16 = str(dest >> 16)
            self.WriteReg_15_11 = 0
            self.ReadReg1Value = Regs[src1 >> 21]
            self.ReadReg2Value = offset  # Assuming offset is used directly
            self.SEOffset = extractor.twos_comp(offset)


    def reset(self):
        self.RegDST = 0
        self.ALUSrc = 0
        self.ALUOp = 0
        self.MemRead = 0
        self.MemWrite = 0
        self.Branch = 0
        self.MemToReg = 0
        self.RegWrite = 0

        self.SEOffset = 0
        self.incrPC = 0

        self.ReadReg1Value = 0
        self.ReadReg2Value = 0

        self.WriteReg_15_11 = 0
        self.WriteReg_20_16 = 0

        self.WriteReg1 = 0
        self.WriteReg2 = 0

        self.Func = 0x0
