class EX_MEM:

    def __init__(self):
        self._initialize_registers()

    def _initialize_registers(self):
        self.MemRead = 0
        self.MemWrite = 0
        self.Branch = 0
        self.MemToReg = 0
        self.RegWrite = 0
        self.ReadReg1Value = 0
        self.ReadReg2Value = 0
        self.SEOffset = 0
        self.ALUOp = 0
        self.incrPC = 0
        self.CalcBTA = -999
        self.Zero = 0
        self.ALUResult = 0
        self.SWValue = 0
        self.WriteRegNum = 0
        self.Func = 0

    def execute(self, MemRead, MemWrite, Branch, RegWrite,
                ALUOp, ReadReg1Value, ReadReg2Value, SEOffset,
                Func, IncrPC, opcode, RegDST,
                WriteReg_20_16, WriteReg_15_11, MemToReg, incrPC):
        self.MemRead = MemRead
        self.MemWrite = MemWrite
        self.MemToReg = MemToReg
        self.RegWrite = RegWrite
        self.Branch = Branch
        self.incrPC = incrPC

        self.CalcBTA = self.calculate_BTA(SEOffset, IncrPC)
        
        self.WriteRegNum = self.determine_write_reg_num(RegDST, WriteReg_15_11, WriteReg_20_16)
        self.perform_alu_operations(ALUOp, ReadReg1Value, ReadReg2Value, SEOffset, Func, opcode)

    def reset(self):
        self._initialize_registers()

    def determine_write_reg_num(self, RegDST, WriteReg_15_11, WriteReg_20_16):
        if RegDST == 1: 
            return WriteReg_15_11
        elif RegDST == 0:
            return WriteReg_20_16
        return -999

    def perform_alu_operations(self, ALUOp, ReadReg1Value, ReadReg2Value, SEOffset, Func, opcode):
        if ALUOp == 0b10: 
            if Func == 32:
                self.ALUResult = ReadReg1Value + ReadReg2Value
                self.SWValue = ReadReg2Value
            elif Func == 34:
                self.ALUResult = ReadReg1Value - ReadReg2Value
                self.SWValue = ReadReg2Value
        elif ALUOp == 0b00:
            if opcode == 0x20:
                self.ALUResult = ReadReg1Value + SEOffset
                self.SWValue = ReadReg2Value
            elif opcode == 0x28:
                self.ALUResult = ReadReg1Value + SEOffset
                self.SWValue = ReadReg2Value

    def calculate_BTA(self, SEOffset, IncrPC):
        # Assuming a simple calculation for demonstration
        if SEOffset + IncrPC > 0:
            return 'x'
