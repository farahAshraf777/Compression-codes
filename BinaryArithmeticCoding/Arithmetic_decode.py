from funForDecodeEncode import *

Read_file = open("input_decode.txt", "r")
data = Read_file.read()
k_digits = open("k.txt", "r")
k = k_digits.read()

probabilities = {}
with open("probabilities.txt") as prob_table:
    for line in prob_table:
       (key, val) = line.split()
       probabilities[key] = val

interval = calc_range(probabilities)
code = binaryToDecimal(data[0: int(k)], int(k))
character = []
character.append(codeRange(code, interval, probabilities))
step = 0
scal = 0
lower = 0
upper = interval[1]
index = 0
position = 0
# 110001100000
while scal <= int(k):
    i = 0

    inrange = Range(lower, upper)
    while not inrange:
        if upper < 0.5:
            upper = round((upper * 2), 5)
            lower = round((lower*2), 5)
        else:
            upper = round(((upper - 0.5) * 2), 5)
            lower = round(((lower-0.5) * 2), 5)
        step += 1
        scal += 1
        inrange = Range(lower, upper)

    if index == 0 and step == 0:
        code = round(((code - lower) / (upper - lower)), 5)
        character.append(codeRange(code, interval, probabilities))

    for x in probabilities:
        if x == (codeRange(code, interval, probabilities)):
            position = i
            break
        i += 1
    if step > 0:
        index += step
        code = binaryToDecimal(data[index: (index + int(k))], int(k))
        print(code)
        code = round(((code - lower) / (upper - lower)), 5)
        character.append(codeRange(code, interval, probabilities))
        print(code)

    step = 0
    l = lower
    u = upper
    # # we should check last element (lower and upper) but while loop maybe end before that
    lower = round((l + (u-l) * interval[position]), 5)
    upper = round((l + (u - l) * interval[position + 1]), 5)
print(character)