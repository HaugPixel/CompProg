
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

def newCount(votes):
    """
    Counts vote
    return list of candidates by
    """


def solveVote(case):
    """
    :param case: Tuple (Candidates, Votes)
    :return: List of winners of election
    """
    candidates, votes = case
    currentvote = []
    winners = []
    while not winners:
        currentvote = [0 for _ in range(len(candidates))]
        for vote in votes:
            currentvote[int(vote.split()[0])-1] += 1
        allVotesCount = len(votes)
        for pos, canditateVoteCount in enumerate(currentvote):
            if canditateVoteCount/allVotesCount >= 1/2:
                winners.append(candidates[pos])

    return winners


def main():
    cases = handleInputV1()
    for case in cases:
        print(case)
        voteWinners = solveVote(case)
        for winningCandidate in voteWinners:
            print(winningCandidate)


if __name__ == '__main__':
    main()
