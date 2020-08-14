import math


def calculateExhange(spendingList):
    avg = math.fsum(spendingList) / float(len(spendingList))
    l1 = math.fsum([int((avg-i)*100)/100 for i in spendingList if i < avg])
    l2 = math.fsum([int((i-avg)*100)/100 for i in spendingList if i > avg])
    res = max(l1, l2)
    print('$'+'{:.2f}'.format(res))


def main():
    while True:
        n = int(input())
        if not n:
            return
        spendings = [float(input()) for _ in range(n)]
        calculateExhange(spendings)


main()
