hexadecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
decimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
binaries = ["0", "1"]


def hex_to_dec(hexadecimal):
    x = len(hexadecimal) - 1
    i = x
    answer = 0
    while i >= 0:
        if hexadecimal[i] in hexadecimals:
            hexadecimal_value = hexadecimals.index(hexadecimal[i])
            decimal_value = hexadecimal_value * (16 ** (x - i))
            answer += decimal_value
            i -= 1
    return answer


def dec_to_bin(decimal):
    decimal_value = int(decimal)
    answer = ""
    if decimal == "0":
        return "0"
    while decimal_value >= 1:
        answer += str(decimal_value % 2)
        decimal_value = int(decimal_value / 2)
    i = len(answer) - 1
    real_answer = ""
    while i >= 0:
        real_answer += answer[i]
        i -= 1
    return real_answer


def hex_to_bin(hexadecimal):
    decimal = hex_to_dec(hexadecimal)
    binary = dec_to_bin(decimal)
    return binary


def bin_to_dec(binary):
    x = len(binary) - 1
    i = x
    answer = 0
    while i >= 0:
        if binary[i] in binaries:
            binary_value = binaries.index(binary[i])
            decimal_value = binary_value * (2 ** (x - i))
            answer += decimal_value
            i -= 1
    return answer


def dec_to_hex(decimal):
    decimal_value = int(decimal)
    answer = ""
    if decimal == "0":
        return "0"
    while decimal_value >= 1:
        answer += hexadecimals[decimal_value % 16]
        decimal_value = int(decimal_value / 16)
    i = len(answer) - 1
    real_answer = ""
    while i >= 0:
        real_answer += answer[i]
        i -= 1
    return real_answer


def bin_to_hex(binary):
    decimal = bin_to_dec(binary)
    hexadecimal = dec_to_hex(decimal)
    return hexadecimal


def imms5_to_unsigned(number):
    if number[0] == "-":
        unsigned = str(256 - int(number[1:4]))
        unsigned = dec_to_bin(unsigned)
    else:
        unsigned = dec_to_bin(number[0:3])
    if unsigned[0] == "0":
        while len(unsigned) < 8:
            unsigned = "0" + unsigned
    else:
        while len(unsigned) < 8:
            unsigned = "1" + unsigned
    imms5 = unsigned[3:8]
    return imms5


