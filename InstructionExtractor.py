class InstructionExtractor:
    @staticmethod
    def extract_bits_from_instruction_26_31(instruction):
        return (instruction >> 26) & 0x3F

    @staticmethod
    def extract_bits_from_instruction_21_25(instruction):
        return (instruction >> 21) & 0x1F

    @staticmethod
    def extract_bits_from_instruction_16_20(instruction):
        return (instruction >> 16) & 0x1F

    @staticmethod
    def extract_bits_from_instruction_11_15(instruction):
        return (instruction >> 11) & 0x1F

    @staticmethod
    def extract_bits_from_instruction_0_5(instruction):
        return instruction & 0x3F

    @staticmethod
    def extract_bits_from_instruction_0_15(instruction):
        return instruction & 0xFFFF

    @staticmethod
    def twos_comp(val):
        if val >> 15 == 1: 
            val -= 2**16 
        return val