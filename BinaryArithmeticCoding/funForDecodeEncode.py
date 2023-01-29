def calc_range(probabilities):
    i = 1
    interval = [0]
    # while i < len(probabilities):
    for x in probabilities.values():
        if i == 1:
            interval.append(round(float(x), 5))
        else:
            interval.append(round((float(x) + interval[i-1]), 5))
        i += 1
    return interval

def Range(lower, upper):
    if upper < 0.5 or lower > 0.5:
        return False
    return True

def binaryToDecimal(code, k):
    decimalValue = int(code, 2)
    decimalValue /= pow(2, int(k))
    return decimalValue

def codeRange(code, interval, probabilities):
    i = 1
    for x in probabilities:
        if code < interval[i]:
            return x
        i += 1
    # for x in probabilities:
    #     if code < float(probabilities[x]):
    #         return x