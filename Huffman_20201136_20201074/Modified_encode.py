from Tree_imp_modified import *
Read_file = open("input_encode.txt", "r")
data = Read_file.read()


Write_file = open("output_encode.txt", "w")
Write_file.write(encode(data))
Write_file.close()