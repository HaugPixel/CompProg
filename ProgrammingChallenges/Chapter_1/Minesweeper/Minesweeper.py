def inBound(height, width, xCor, yCor):
    return (0 <= xCor < width) and (0 <= yCor < height)


def minefield(n, m, x, y, dynamiclist):
    dynamiclist[y][x] = 10
    if inBound(n, m, x, y - 1):
        dynamiclist[y - 1][x] += 1
    if inBound(n, m, x - 1, y - 1):
        dynamiclist[y - 1][x - 1] += 1
    if inBound(n, m, x + 1, y - 1):
        dynamiclist[y - 1][x + 1] += 1
    if inBound(n, m, x, y + 1):
        dynamiclist[y + 1][x] += 1
    if inBound(n, m, x - 1, y + 1):
        dynamiclist[y + 1][x - 1] += 1
    if inBound(n, m, x + 1, y + 1):
        dynamiclist[y + 1][x + 1] += 1
    if inBound(n, m, x - 1, y):
        dynamiclist[y][x - 1] += 1
    if inBound(n, m, x + 1, y):
        dynamiclist[y][x + 1] += 1


def printOutput(dynamiclist, case):
    # Handles output
    print("Field #" + str(case) + ":")
    for y in dynamiclist:
        for x in y:
            if x < 10:
                print(x, end='')
            else:
                print("*", end='')
        print()


def addMines(n, m, dynamiclist):
    for y in range(n):
        for x, ele in enumerate(input()):  # getline
            if ele == "*":
                minefield(n, m, x, y, dynamiclist)


def main():
    case = 1
    while True:
        # Checks for emptyline and skips
        streng = input()
        while not streng:
            streng = input()

        # Takes  in width and length (m,n)
        n, m = [int(i) for i in streng.split()]  # getline
        if n == 0:
            break
        if case > 1:  # Line between each case
            print()

        # Pre-made array n*m
        dynamiclist = [[0 for _ in range(m)] for _ in range(n)]
        addMines(n, m, dynamiclist)
        printOutput(dynamiclist, case)
        case += 1


if __name__ == '__main__':
    main()
