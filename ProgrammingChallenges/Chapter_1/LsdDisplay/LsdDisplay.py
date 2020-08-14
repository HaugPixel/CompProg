
def printOne(n):
    printArea = []
    printArea.append(' ' * (n + 2))
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' * (n + 2))
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' * (n + 2))
    return printArea


def printTwo(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * (n + 1))for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    return printArea


def printThree(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    return printArea


def printFour(n):
    printArea = []
    printArea.append(' ' * (n + 2))
    [printArea.append('|' + ' ' * n + '|')for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' * (n + 2))
    return printArea

def printFive(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * (n + 1))for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    return printArea


def printSix(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * (n + 1))for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * n + '|')for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    return printArea

def printSeven(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' * (n + 2))
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' * (n + 2))

    return printArea

def printEight(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * n + '|')for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * n + '|')for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    return printArea

def printNine(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * n + '|')for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append(' ' * (n + 1) + '|') for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    return printArea

def printZero(n):
    printArea = []
    printArea.append(' ' + '-' * n + ' ')
    [printArea.append('|' + ' ' * n + '|')for _ in range(n)]
    printArea.append(' ' * (n + 2))
    [printArea.append('|' + ' ' * n + '|')for _ in range(n)]
    printArea.append(' ' + '-' * n + ' ')
    return printArea

def printSpace(n):
    printArea = []
    [printArea.append(' ') for _ in range((2*n)+-3)]
    return printArea


def choosePrint(num, n):
    """Choosing function"""
    if num == 1:
        return printOne(n)
    if num == 2:
        return printTwo(n)
    if num == 3:
        return printThree(n)
    if num == 4:
        return printFour(n)
    if num == 5:
        return printFive(n)
    if num == 6:
        return printSix(n)
    if num == 7:
        return printSeven(n)
    if num == 8:
        return printEight(n)
    if num == 9:
        return printNine(n)
    if num == 0:
        return printZero(n)


def main():
    while True:
        n, numberString = input().split()  # numbersize, and numbers to print
        n = int(n)
        if not n:
            return

        printArea = [[] for _ in range(2*n+3)]
        for num in numberString:
            newprint = choosePrint(int(num), n)
            for k in range(len(printArea)):
                printArea[k].append(newprint[k])

        for x in printArea:
            print(' '.join(x))
        print()


main()