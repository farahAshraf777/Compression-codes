def Calc_OriginalCode(num):
    binary = bin(num)[2:]
    return (len(binary))

input = open("input_decode.txt", "r")
output = open("output_decode.txt", "w")
decode = input.read()
Huffman_table = {}

with open("huffman_table.txt") as table:
    for line in table:
       (key, val) = line.split()
       Huffman_table[key] = val
others = {}
with open("original_code.txt") as original_code:
    for line in original_code:
       (key, val) = line.split()
       others[key] = val
others_size = Calc_OriginalCode(len(others))
index = 0

code_length = 2
while index < len(decode):
    if decode[index] in Huffman_table:
        if Huffman_table[decode[index]] == "others":
            index += 1
            output.write(others[decode[index: index+others_size]])
            index += others_size
        else:
            output.write(Huffman_table[decode[index]])
            index += 1
        code_length = 1
    elif decode[index: index+code_length] in Huffman_table:
        if Huffman_table[decode[index: index+code_length]] == "others":
            index += code_length
            output.write(others[decode[index: index+others_size]])
            index += others_size
        else:
            output.write(Huffman_table[decode[index: index+code_length]])
            index += code_length
        code_length = 1

    code_length += 1

output.close()