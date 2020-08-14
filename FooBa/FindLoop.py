#   Single Iteration of algorithm
def flawedAlgorithm(streng, b):
    x = ''.join(sorted(streng, reverse=True))
    y = ''.join(sorted(streng))
    z = int(x, b) - int(y, b)
    return padToLen(baseConverter(z, b), len(streng))


#   Converts numberbase up to
def baseConverter(n, b):
    convert10 = "0123456789"
    if n < b:
        return convert10[n]
    else:
        return baseConverter(n // b, b) + convert10[n % b]


#   Pads with '0'
def padToLen(streng, length):
    pad = len(streng) < length
    return str("0" * pad) + streng


#   Checks for loop
def solution(streng, b):
    minionList = [streng]
    while True:
        newstring = flawedAlgorithm(streng, b)
        if newstring in minionList:
            return len(minionList) - minionList.index(newstring)
        minionList.append(newstring)
        streng = newstring
