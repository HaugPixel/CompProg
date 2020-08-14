import sys


def splitCases(lines):
    cases = []
    for x in lines:
        if not x:
            cases.append([])
        else:
            cases[len(cases)-1].append(x)
    return cases


def interprate(command, num):
    return 0


def solve(cases):
    for case in cases:
        num = 0
        for command in case:
            num = interprate(command, num)

        print(num)
        print()


def getInputV1():
    with open('test.txt', 'r') as fil:
        n = int(fil.readline())
        lines = [i.strip() for i in fil.readlines()]
    return splitCases(lines)

def getInputV2():
    firstline = int(sys.stdin.read(1))
    lines = []
    while True:
        newline = sys.stdin.read(1)
        first = sys.stdin.read(1)
        if first == "\\n":
            lines.append([])
            break
        else:
            rest = sys.stdin.read(2)
            lines[len(lines)-1].append(first+rest)

    return lines


def main():
    print(getInputV1())


if __name__ == '__main__':
    main()
