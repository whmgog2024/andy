'''
ZEGUANG XIA
CS472
2024/4/24
Log version 1.17:
- Organize the format and use the correct decimal and hexadecimal
- Optimize structure and enhance program stability
'''

import copy
from EX_MEM import EX_MEM
from IF_ID import IF_ID
from InstructionExtractor import InstructionExtractor
from GarbageValueChecker import GarbageValueChecker
from ID_EX import ID_EX
from globalvariables import *
#import all definition in the globalvariables.py
from MEM_WB import MEM_WB
#--------------------------------------------------------------------------------------------------------------------------------#

class Print_out_everything:
    @staticmethod
    def print_state():
        print('\n=== REGISTERS ===')
        for regNum, reg in enumerate(Regs):
            if (regNum + 1) % 4 == 1:
                print()
            print(f'R{regNum:2d}: {reg:08x}', end='  ')
    
        print('\n\n' + '=' * 80)
        print('<IF/ID Write (written to by the IF stage)>')
    
        if IF_ID_WRITE.instruction == 0:
            print('\tControl = 00000000')
        else:
            print(f'\tInstruction = {hex(IF_ID_WRITE.instruction)} {decode_mips_instruction(IF_ID_WRITE.instruction)}')
            print(f'\tIncrPC = {hex(IF_ID_WRITE.incrPC)}')
    
        print('\n<IF/ID Read (read to by the ID stage)>')
        if IF_ID_READ.instruction == 0:
            print('\tControl = 00000000')
        else:
            print(f'\tInstruction = {hex(IF_ID_READ.instruction)} {decode_mips_instruction(IF_ID_READ.instruction)}')
            print(f'\tIncrPC = {hex(IF_ID_READ.incrPC)}')
    
        print('\n' + '=' * 80)
        print('<ID/EX Write (written to by the ID stage)>')
        print(f'\tControl: RegDST = {GarbageValueChecker.check_garbage_val(ID_EX_WRITE.RegDST)}', \
              f'ALUSrc = {ID_EX_WRITE.ALUSrc}', \
              f'ALUOp = {bin(ID_EX_WRITE.ALUOp)}', \
              f'MemRead = {ID_EX_WRITE.MemRead}', \
              f'MemWrite = {ID_EX_WRITE.MemWrite}', \
              f'Branch = {ID_EX_WRITE.Branch}', \
              f'MemToReg = {GarbageValueChecker.check_garbage_val(ID_EX_WRITE.MemToReg)}', \
              f'RegWrite = {ID_EX_WRITE.RegWrite}')
    
        if ID_EX_WRITE.instruction == 0:
            print('\n\tIncrPC = 0')
        else:
            print(f'\n\tIncrPC = {hex(ID_EX_WRITE.incrPC)}')
        print(f'\tReadReg1Value = {hex(ID_EX_WRITE.ReadReg1Value)}')
        print(f'\tReadReg2Value = {hex(ID_EX_WRITE.ReadReg2Value)}')
        print(f'\n\tSEOffset = {GarbageValueChecker.check_garbage_val(hex(((abs(ID_EX_WRITE.SEOffset) ^ 0xffff) + 1) & 0xffff))}')
        print(f'\tWriteReg_20_16 = {ID_EX_WRITE.WriteReg_20_16}')
        print(f'\tWriteReg_15_11 = {ID_EX_WRITE.WriteReg_15_11}')
        print(f'\tFunction = {GarbageValueChecker.check_garbage_val(ID_EX_WRITE.Func)}')
    
        print('\n<ID/EX Read (read to by the EX stage)>')
        print(f'\tControl: RegDST = {GarbageValueChecker.check_garbage_val(ID_EX_READ.RegDST)}', \
              f'ALUSrc = {ID_EX_READ.ALUSrc}', \
              f'ALUOp = {bin(ID_EX_READ.ALUOp)}', \
              f'MemRead = {ID_EX_READ.MemRead}', \
              f'MemWrite = {ID_EX_READ.MemWrite}', \
              f'Branch = {ID_EX_READ.Branch}', \
              f'MemToReg = {GarbageValueChecker.check_garbage_val(ID_EX_READ.MemToReg)}', \
              f'RegWrite = {ID_EX_READ.RegWrite}')
    
        if ID_EX_READ.instruction == 0:
            print('\n\tIncrPC = 0')
        else:
            print(f'\n\tIncrPC = {hex(ID_EX_READ.incrPC)}')
        print(f'\tReadReg1Value = {hex(ID_EX_READ.ReadReg1Value)}')
        print(f'\tReadReg2Value = {hex(ID_EX_READ.ReadReg2Value)}')
        print(f'\n\tSEOffset = {GarbageValueChecker.check_garbage_val(hex(((abs(ID_EX_READ.SEOffset) ^ 0xffff) + 1) & 0xffff))}')
        print(f'\tWriteReg_20_16 = {ID_EX_READ.WriteReg_20_16}')
        print(f'\tWriteReg_15_11 = {ID_EX_READ.WriteReg_15_11}')
        print(f'\tFunction = {GarbageValueChecker.check_garbage_val(ID_EX_READ.Func)}')
    
        print('\n' + '=' * 80)
        print('<EX/MEM Write (written to by the EX stage)>')
        print(f'\tControl: MemRead = {EX_MEM_WRITE.MemRead}', \
              f'MemWrite = {EX_MEM_WRITE.MemWrite}', \
              f'Branch = {EX_MEM_WRITE.Branch}', \
              f'MemToReg = {GarbageValueChecker.check_garbage_val(EX_MEM_WRITE.MemToReg)}', \
              f'RegWrite = {EX_MEM_WRITE.RegWrite}')
        print(f'\n\tCalcBTA = {GarbageValueChecker.check_garbage_val(EX_MEM_WRITE.CalcBTA)}')
        print(f'\tZero = {EX_MEM_WRITE.Zero}')
        print(f'\tALUResult = {hex(EX_MEM_WRITE.ALUResult)}')
        print(f'\n\tSWValue = {hex(EX_MEM_WRITE.SWValue)}')
        print(f'\tWriteRegNum = {GarbageValueChecker.check_garbage_val(EX_MEM_WRITE.WriteRegNum)}')
    
        print('\n<EX/MEM READ (read to by the MEM stage)>')
        print(f'\tControl: MemRead = {EX_MEM_READ.MemRead}', \
              f'MemWrite = {EX_MEM_READ.MemWrite}', \
              f'Branch = {EX_MEM_READ.Branch}', \
              f'MemToReg = {GarbageValueChecker.check_garbage_val(EX_MEM_READ.MemToReg)}', \
              f'RegWrite = {EX_MEM_READ.RegWrite}')
        print(f'\n\tCalcBTA = {GarbageValueChecker.check_garbage_val(EX_MEM_READ.CalcBTA)}')
        print(f'\tZero = {EX_MEM_READ.Zero}')
        print(f'\tALUResult = {hex(EX_MEM_READ.ALUResult)}')
        print(f'\n\tSWValue = {hex(EX_MEM_READ.SWValue)}')
        print(f'\tWriteRegNum = {GarbageValueChecker.check_garbage_val(EX_MEM_READ.WriteRegNum)}')
    
        print('\n' + '=' * 80)
        print('<MEM/WB Write (written to by the MEM stage)>')
        print(f'\tControl: MemToReg = {GarbageValueChecker.check_garbage_val(MEM_WB_WRITE.MemToReg)}', \
              f'RegWrite = {MEM_WB_WRITE.RegWrite}')
        print(f'\n\tLWDataValue = {hex(MEM_WB_WRITE.LWDataValue)}')
        print(f'\tALUResult = {hex(MEM_WB_WRITE.ALUResult)}')
        print(f'\tWriteRegNum = {GarbageValueChecker.check_garbage_val(MEM_WB_WRITE.WriteRegNum)}')
    
        print('\n<MEM/WB Read (read by the WB stage)>')
        print(f'\tControl: MemToReg = {GarbageValueChecker.check_garbage_val(MEM_WB_READ.MemToReg)}', \
              f'RegWrite = {MEM_WB_READ.RegWrite}')
        print(f'\n\tLWDataValue = {hex(MEM_WB_READ.LWDataValue)}')
        print(f'\tALUResult = {hex(MEM_WB_READ.ALUResult)}')
        print(f'\tWriteRegNum = {GarbageValueChecker.check_garbage_val(MEM_WB_READ.WriteRegNum)}')
    
        print('=' * 100)
################################global definition################################
IF_ID_WRITE = IF_ID(0x0, INITIAL_ADDRESS)
IF_ID_READ = IF_ID(0x0, 0x0)

ID_EX_WRITE = ID_EX()
ID_EX_READ = ID_EX()

EX_MEM_WRITE = EX_MEM()
EX_MEM_READ = EX_MEM()

MEM_WB_WRITE = MEM_WB()
MEM_WB_READ = MEM_WB()
################################global definition################################
'''
Keeping global variables in main.py for simplicity and ease of access, which helps 
in avoiding the complexity of cross-module dependencies and potential circular imports, 
especially suitable for smaller projects or during the initial development phases.
'''

class PipelineCopier:
    def __init__(self):
        pass

    def Copy_write_to_read(self):
        global IF_ID_READ, ID_EX_READ, EX_MEM_READ, MEM_WB_READ

        objects = [IF_ID_WRITE, ID_EX_WRITE, EX_MEM_WRITE, MEM_WB_WRITE]

        for i in range(len(objects)):
            globals()[f"{objects[i].__class__.__name__}_READ"] = copy.deepcopy(objects[i])

        for obj in (ID_EX_WRITE, EX_MEM_WRITE, MEM_WB_WRITE):
            obj.reset() 
            
copier = PipelineCopier()


class PipelineStages:
    @staticmethod
    def IF_stage(instruction, running_address):
        IF_ID_WRITE.instruction = instruction
        IF_ID_WRITE.incrPC = running_address
    
    def ID_stage():
        ID_EX_WRITE.decode_instruction(IF_ID_READ.instruction, IF_ID_READ.incrPC)
    
    def EX_stage():
        EX_MEM_WRITE.execute(ID_EX_READ.MemRead, ID_EX_READ.MemWrite, ID_EX_READ.Branch, ID_EX_READ.RegWrite,
                             ID_EX_READ.ALUOp, ID_EX_READ.ReadReg1Value, ID_EX_READ.ReadReg2Value, ID_EX_READ.SEOffset,
                             ID_EX_READ.Func, ID_EX_READ.incrPC, ID_EX_READ.opcode, ID_EX_READ.RegDST, 
                             ID_EX_READ.WriteReg_20_16, ID_EX_READ.WriteReg_15_11,ID_EX_READ.MemToReg, ID_EX_READ.incrPC)
    
    def MEM_stage():
        MEM_WB_WRITE.access_memory(EX_MEM_READ.MemToReg, EX_MEM_READ.RegWrite, EX_MEM_READ.ALUResult, EX_MEM_READ.WriteRegNum, 
                                   EX_MEM_READ.MemRead, EX_MEM_READ.SWValue, EX_MEM_READ.MemWrite)
    
    def WB_stage():
        MEM_WB_READ.write_back()
#--------------------------------------------------------------------------------------------------------------------------------#

def main():
    count = 0

    for x in range(0x0, 0x7FF+1):
        Main_Mem.append(count) 

        count += 1

        if count > 0xFF:
            count = 0

    for x in range(0, 32):
        Regs[x] = 0x100 + x

    print('==[CLOCK CYCLE 0]==\n') 
    Print_out_everything.print_state() 
    running_address = INITIAL_ADDRESS

    # MAIN LOOP
    for clock_cycle in range(len(instructions)): 
        print('==[CLOCK CYCLE:', clock_cycle+1,']==\n')

        instruction = instructions[clock_cycle]

        PipelineStages.IF_stage(instruction, running_address)
        PipelineStages.ID_stage()
        PipelineStages.EX_stage()
        PipelineStages.MEM_stage()
        PipelineStages.WB_stage()
        Print_out_everything.print_state()
        copier.Copy_write_to_read()

        running_address += 4

if __name__ == '__main__':
    main()
