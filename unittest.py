'''
This is the Xth debug session, 
addressing the issue related to decoding MIPS instructions in the ID_EX module, 
successfully resolved debug OFTest case for the ID_EX module，Initialize the module and global registers

'''
import unittest
from ID_EX import ID_EX
from globalvariables import Regs

class TestIDEXModule(unittest.TestCase):
    def setUp(self):
        # Initialize the module and global registers
        self.id_ex = ID_EX()
        Regs[1] = 10  # Sample data
        Regs[2] = 20  # Sample data

    def test_decode_instruction(self):
        # Simulate decoding a simple addition instruction
        # Assume the instruction encoding is 0x00221820, i.e., add $3, $1, $2
        instruction = 0x00221820
        self.id_ex.decode_instruction(instruction, 0x00400004)
        self.assertEqual(self.id_ex.RegDST, 1)
        self.assertEqual(self.id_ex.ALUSrc, 0)
        self.assertEqual(self.id_ex.MemToReg, 0)
        self.assertEqual(self.id_ex.RegWrite, 1)
        self.assertEqual(self.id_ex.MemRead, 0)
        self.assertEqual(self.id_ex.MemWrite, 0)
        self.assertEqual(self.id_ex.Branch, 0)
        self.assertEqual(self.id_ex.ALUOp, 0b10)
        self.assertEqual(self.id_ex.ReadReg1Value, 10)
        self.assertEqual(self.id_ex.ReadReg2Value, 20)
        self.assertEqual(self.id_ex.Func, 0x20)

if __name__ == '__main__':
    unittest.main()
