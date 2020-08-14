


def main():
    with open("easytest.txt", "r") as fil:
        n = int(fil.readline().strip())
        fil.readline()

        for x in range(n):
            num = int(fil.readline().strip())
            candidates = [fil.readline().strip() for _ in range(num)]
            line = None
            while line != "":
                if line:
                    votes.append(line.strip())
                line = fil.readline()
                vote


if __name__ == '__main__':
    main()
