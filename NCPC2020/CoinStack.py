def bigSmol(nums):
    biggest = [0, 0]
    smallest = [1001, 0]
    for i, ele in enumerate(nums):
        if ele > biggest[0]:
            biggest[0] = ele
            biggest[1] = i
        if ele <= smallest[0] and ele != 0:
            smallest[0] = ele
            smallest[1] = i
    return biggest, smallest


def main():
    n = input()
    numList = [int(i) for i in input().split()]
    summ = sum(numList)
    biggest, smallest = bigSmol(numList)

    if biggest[0] > summ-biggest[0]:
        print("no")
        return

    if summ % 2:
        print("no")
        return

    print("yes")

    while biggest[0] > 0:
        numList[biggest[1]] -= 1
        numList[smallest[1]] -= 1

        print(biggest[1]+1, smallest[1]+1)
        biggest, smallest = bigSmol(numList)

main()



