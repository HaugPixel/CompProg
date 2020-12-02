import sys

d = {}


def findMaxCycle(i, k):
    """Find maxlength of lists of i..k made with 3n+1 Algorithm"""
    return max([algorithm(j) for j in range(min(i, k), max(i, k) + 1)])


def algorithm(n):
    """Collatz"""
    length = d.get(n)
    if length:
        return length
    elif n == 1:
        return 1
    elif n % 2:
        length = 1 + algorithm((3 * n) + 1)
    else:
        length = 1 + algorithm(n / 2)

    d[n] = length
    return length


def main():
    """Takes care of input, output and function structure"""
    pairList = sys.stdin.readlines()  # input for judge
#    with open("test.txt", "r") as fil:  # input for txtfile
#       pairList = fil.readlines()

    for x in pairList:
        i, k = (int(i) for i in x.strip().split())
        print(i, k, findMaxCycle(i, k))


main()