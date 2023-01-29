encoded = [65, 66, 65, 128, 128, 129, 131, 134, 130, 129, 66, 138, 139, 138]
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = str(input())
#
#     encoded.append(ele)
decode = []
dectionaryindex = []
dectionaryval = []
i = 0
l = 0
while i < len(encoded):
    if encoded[i] <= 127 and i == 0:
        decode.append(chr(encoded[i]))
    elif encoded[i] <= 127 and i > 0:
        dectionaryindex.append(l + 128)
        l += 1
        decode.append(chr(encoded[i]))
        dectionaryval.append(decode[i-1] + decode[i])
    elif encoded[i] > 127:
        dectionaryindex.append(l + 128)
        l += 1
        found = dectionaryindex.index(encoded[i])
        dectionaryval.append(decode[i - 1]+decode[i - 1][0])
        decode.append(dectionaryval[found])
    i += 1

for x in decode:
    print(x, end="")