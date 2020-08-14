
def handleInputV1():
    """
    Reads Australian election testdoc, and returns election data
    :return: List of tuples (Candidates, Votes)
    """
    cases = []

    with open("easytest.txt", "r") as fil:
        n = int(fil.readline().strip())
        fil.readline()

        for x in range(n):
            num = int(fil.readline().strip())
            candidates = [fil.readline().strip() for _ in range(num)]
            votes = []
            line = None
            while line != "":
                if line:
                    votes.append(line)
                line = fil.readline().strip()

            cases.append((candidates, votes))

    return cases


def solveVote(case):
    """
    :param case: Tuple (Candidate, Votes)
    :return: List of winners of election
    """
    return []


def main():
    cases = handleInputV1()
    for case in cases:
        voteWinners = solveVote(case)
        for winningCandidate in voteWinners:
            print(winningCandidate)




if __name__ == '__main__':
    main()
