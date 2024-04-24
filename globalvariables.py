INITIAL_ADDRESS = 0x7a004
Main_Mem = []
Regs = [0] * 32
instructions = [
        0x00a63820,
        0x8d0f0004,
        0xad09fffc,
        0x00625022,
        0x10c8fffb
    ]
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

def sign_extend(value):
    if value & 0x8000:  # If the value is negative
        return value - 0x10000
    return value
decoded_instructions = [decode_mips_instruction(inst) for inst in instructions]
