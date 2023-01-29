input = open("input_decode.txt", "r")
decode = input.read()
Huffman_table = {}
with open("huffman_table.txt") as table:
    for line in table:
       (key, val) = line.split()
       Huffman_table[key] = val
index = 0
output = open("output_decode.txt", "w")
code_length = 2
while index < len(decode):

    if decode[index] in Huffman_table:
        output.write(Huffman_table[decode[index]])
        index += 1
        code_length = 1
    elif decode[index: index+code_length] in Huffman_table:
        output.write(Huffman_table[decode[index: index+code_length]])
        index += code_length
        code_length = 1
    code_length += 1

output.close()