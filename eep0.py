import converters

mnemonics = ["mov", "add", "sub", "adc", "ldr", "str", "jmp", "jne", "jcs", "jmi"]
opcode = ["0", "1", "2", "3", "4", "5", "6", "6", "7", "7"]


def input_instruction():
    instruction_assembly = input("please enter the instruction in assembly language: ").lower()
    instruction_assembly = instruction_assembly.replace(" ", "")
    instruction_assembly = instruction_assembly.replace(",", "")
    instruction_assembly = instruction_assembly.replace("#", "")
    return instruction_assembly


def find_opcode(instruction_assembly):
    if instruction_assembly[0:3] in mnemonics:
        opcode_index = mnemonics.index(instruction_assembly[0:3])
        opcode_in_decimal = opcode[opcode_index]
        opcode_in_binary = converters.dec_to_bin(opcode_in_decimal)
    return opcode_in_binary


def process_bit_8_to_12(instruction_assembly):
    if instruction_assembly[0:3] == "jmp" or instruction_assembly[0:3] == "jcs":
        return "00000"
    if instruction_assembly[0:3] == "jne" or instruction_assembly[0:3] == "jmi":
        return "10000"
    if instruction_assembly[5] == "r":
        register_1 = instruction_assembly[4]
        register_2 = instruction_assembly[6]
    else:
        register_1 = instruction_assembly[4]
        register_2 = "00"
    return instruction_assembly[5] + register_1 + register_2


def process_bit_0_to_7(instruction_assembly):
    if instruction_assembly[0:3] == "jmp" or instruction_assembly[0:3] == "jcs" or instruction_assembly[
                                                                                   0:3] == "jne" or instruction_assembly[
                                                                                                    0:3] == "jmi":
        last_8_bits = converters.dec_to_bin(instruction_assembly[3:6])
        while len(last_8_bits) < 8:
            last_8_bits = "0" + last_8_bits
        return last_8_bits
    if instruction_assembly[5] == "r":
        return "00000000"
    else:
        last_8_bits = converters.dec_to_bin(instruction_assembly[5:8])
        while len(last_8_bits) < 8:
            last_8_bits = "0" + last_8_bits
        return last_8_bits


def output_of_eep0(instruction):
    binary_in = find_opcode(instruction) + process_bit_8_to_12(instruction) + process_bit_0_to_7(instruction)
    in_hex = converters.bin_to_hex(binary_in)
    while len(in_hex) < 4:
        in_hex = "0" + in_hex
    in_hex = str.upper(in_hex)
    return in_hex


def operate_eep0(instruction):
    output = output_of_eep0(instruction)
    print(f"the instruction in hexadecimals is: 0x{output}")
