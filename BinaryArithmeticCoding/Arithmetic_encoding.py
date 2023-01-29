from funForDecodeEncode import *
scalling_list = []
Read_file = open("input_encode.txt", "r")
data = Read_file.read()

probabilities = {}
with open("probabilities.txt") as prob_table:
    for line in prob_table:
       (key, val) = line.split()
       probabilities[key] = val

index = 1
interval = calc_range(probabilities)
lower = 0
upper = interval[1]
position = 0
while index < len(data):
    i = 0
    inrange = Range(lower, upper)

    while not inrange:
        if upper < 0.5:
            upper = round((upper * 2), 5)
            lower = round((lower*2), 5)

            scalling_list.append(0)
        else:
            upper = round(((upper - 0.5) * 2), 5)
            lower = round(((lower-0.5) * 2), 5)

            scalling_list.append(1)
        inrange = Range(lower, upper)

    for x in probabilities:
        if x == data[index]:
            position = i
            break
        i += 1

    l = lower
    u = upper
    # we should check last element (lower and upper) but while loop maybe end before that
    lower = round((l + (u-l) * interval[position]), 5)
    upper = round((l + (u - l) * interval[position + 1]), 5)
    index += 1

# 0.5 representation
min_prob = float(min(probabilities.values()))
power = 1
scalling_list.append(1)
while (1/pow(2, power)) > min_prob:
    power += 1
    scalling_list.append(0)
k = power
with open("output_encode.txt", "w") as Write_file:
    for x in scalling_list:
        Write_file.write(str(x))
Write_file.close()