#data = "ABAABABBAABAABAAAABABBBBBBBB"
data = input("Enter data to compress: ")
tags = []
dectionaryindex = []
dectionaryval = []
index = 0
i = 0
found = -1
while index < len(data):
    if index == 0:
        dectionaryval.append(data[0:2])
        dectionaryindex.append(i + 128)
        tags.append(ord(data[index]))
    else:
        c1 = 2
        c2 = 0
        while index < len(data):
            f = found
            if (data[index:index + c1]) in dectionaryval:
                found = dectionaryval.index((data[index:index + c1]))
                c2 += 1
                f = found
            else:
                found = -1
            if found == -1 or (index + c1) >= len(data):
                if (index + c1) < len(data):
                    dectionaryval.append(data[index:(index + c1)])
                    dectionaryindex.append(i + 128)

                if c1 == 2 and found == -1:
                    tags.append(ord(data[index]))
                else:
                    tags.append(dectionaryindex[f])
                index += c2
                break
            c1 += 1

    index += 1
    i += 1

print(tags)
