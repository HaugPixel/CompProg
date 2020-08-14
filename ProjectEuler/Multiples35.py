import math


def findSum(n, multiple):
    k = math.ceil(n/multiple)
    summ = multiple * ((k * (k-1)) // 2)
    return summ


print(findSum(15, 3))