from globalvariables import *

class MEM_WB:
    def __init__(self):
        # Set default values for all attributes to 0 using a unified approach
        attributes = [
            'MemToReg', 'RegWrite', 'MemRead', 'MemWrite', 'Branch',
            'LWDataValue', 'SWDataValue', 'ALUResult', 'WriteRegNum'
        ]
        for attr in attributes:
            setattr(self, attr, 0)

    def access_memory(self, MemToReg, RegWrite, ALUResult, WriteRegNum, MemRead, SWValue, MemWrite):
        # Update control signals
        self.MemToReg, self.RegWrite, self.ALUResult, self.WriteRegNum = MemToReg, RegWrite, ALUResult, WriteRegNum
        # Memory operation based on control flags
        if MemRead:
            self.LWDataValue = Main_Mem[ALUResult]
        elif MemWrite:
            Main_Mem[ALUResult] = SWValue


    def write_back(self):
    # Check if a write back to the register is needed
        if self.WriteRegNum != -999 and not self.MemWrite:
            # Determine the source of data based on MemToReg
            write_value = self.ALUResult if not self.MemToReg else Main_Mem[self.ALUResult]
            Regs[int(self.WriteRegNum)] = write_value


    def reset(self):
        # Reset all internal states
        attributes = [
            'MemToReg', 'RegWrite', 'MemRead', 'MemWrite', 'Branch',
            'LWDataValue', 'SWDataValue', 'ALUResult', 'WriteRegNum'
        ]
        for attr in attributes:
            setattr(self, attr, 0)
