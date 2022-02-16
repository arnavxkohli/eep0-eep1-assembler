import converters

alu = ["mov", "add", "sub", "adc", "sbc", "and", "xor", "lsl"]
rest = ["ldr", "str"]
ldr_str = ["8", "a"]
jumps = ["jmp", "not", "jne", "jeq", "jcs", "jcc", "jmi", "jpl", "jge", "jlt", "jgt", "jle", "jhi", "jls", "jsr", "ret"]


def input_instruction():
    instruction_assembly = input("please enter the instruction in assembly language: ").lower()
    instruction_assembly = instruction_assembly.replace(" ", "")
    instruction_assembly = instruction_assembly.replace(",", "")
    instruction_assembly = instruction_assembly.replace("#", "")
    return instruction_assembly


def bit_12_to_15(instruction_assembly):
    if instruction_assembly[0:3] in alu:
        twelve_to_fifteen = alu.index(instruction_assembly[0:3])
        twelve_to_fifteen = converters.dec_to_hex(twelve_to_fifteen)
    elif instruction_assembly[0:3] in rest:
        index = rest.index(instruction_assembly[0:3])
        twelve_to_fifteen = ldr_str[index]
    else:
        twelve_to_fifteen = "c"
    return twelve_to_fifteen


def bit_8_to_11(instruction_assembly):
    if instruction_assembly[3] == "r":
        if instruction_assembly[5] == "r":
            eight_to_eleven = converters.dec_to_bin(instruction_assembly[4]) + "0"
        else:
            eight_to_eleven = converters.dec_to_bin(instruction_assembly[4]) + "1"
        eight_to_eleven = converters.bin_to_hex(eight_to_eleven)
    else:
        index = jumps.index(instruction_assembly[0:3])
        eight_to_eleven = str(index)
        eight_to_eleven = converters.dec_to_hex(eight_to_eleven)
    while len(eight_to_eleven) < 4:
        eight_to_eleven = "0" + eight_to_eleven
    eight_to_eleven = converters.bin_to_hex(eight_to_eleven)
    return eight_to_eleven


def bit_0_to_7(instruction_assembly):
    if instruction_assembly[5] == "r":
        if instruction_assembly[7] == "-":
            zero_to_seven = converters.dec_to_bin(instruction_assembly[6]) + converters.imms5_to_unsigned(
                instruction_assembly[8:11])
        else:
            zero_to_seven = converters.dec_to_bin(instruction_assembly[6]) + converters.imms5_to_unsigned(
                instruction_assembly[7:10])
    else:
        zero_to_seven = converters.dec_to_bin(instruction_assembly[5:8])
    while len(zero_to_seven) < 8:
        zero_to_seven = "0" + zero_to_seven
    zero_to_seven = converters.bin_to_hex(zero_to_seven)
    return zero_to_seven


def output_of_eep1(instruction):
    in_hex = bit_12_to_15(instruction) + bit_8_to_11(instruction) + bit_0_to_7(instruction)
    in_hex = str.upper(in_hex)
    return in_hex


def operate_eep1(instruction):
    output = output_of_eep1(instruction)
    print(f"the instruction in hexadecimals is: 0x{output}")
