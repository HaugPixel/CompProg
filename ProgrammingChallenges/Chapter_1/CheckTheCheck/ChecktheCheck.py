import sys


class ChessBoard:
    def __init__(self, cBoard, num):
        self.cBoard = cBoard
        self.num = num
        self.kinginCheck = "no"
        self.kingOnBoard = False

    def checkForCheck(self):
        for y, line in enumerate(self.cBoard):
            for x, ele in enumerate(line.strip()):
                self.checkTile(ele, x, y)

    def setKingInCheck(self, ele):
        if isWhite(ele):
            self.kinginCheck = "black"
        else:
            self.kinginCheck = "white"

    def checkTile(self, ele, x, y):
        if ele == ".":
            return
        elif ele == "p" or ele == "P":
            if checkPawn(ele, x, y, self.cBoard):
                self.setKingInCheck(ele)
        elif ele == "b" or ele == "B":
            if checkBishop(ele, x, y, self.cBoard):
                self.setKingInCheck(ele)
        elif ele == "r" or ele == "R":
            if checkRook(ele, x, y, self.cBoard):
                self.setKingInCheck(ele)
        elif ele == "n" or ele == "N":
            if checkKnight(ele, x, y, self.cBoard):
                self.setKingInCheck(ele)
        elif ele == "q" or ele == "Q":
            if checkQueen(ele, x, y, self.cBoard):
                self.setKingInCheck(ele)
        elif ele == "k" or ele == "K":
            self.kingOnBoard = True

    def printResult(self):
        if self.kingOnBoard:
            print("Game #", self.num, ": ", self.kinginCheck, " king is in check.", sep='')


def inBounds(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def isWhite(piece):
    return piece.isupper()


def isBlack(piece):
    return not piece.isupper()


def isWhiteKing(piece):
    return piece == 'K'


def isBlackKing(piece):
    return piece == 'k'


def handleInputV1():
    lines = sys.stdin.readlines()
    boards = []
    for i in range(0, len(lines), 9):
        boards.append([i.strip() for i in lines[i:i+8]])
    return boards


def handleInputV2():
    with open("simpleTest.txt", "r") as fil:
        lines = fil.readlines()
    boards = []
    for i in range(0, len(lines), 9):
        boards.append([i.strip() for i in lines[i:i+8]])
    return boards


def getKnightMoves(x, y):
    return [(x+i, y+k) for i, k in [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]]


def getDirections(x, y):
    n, w, s, e = (y - 1, x - 1, y + 1, x + 1)
    return n, w, s, e


def getDiagonals(x, y):
    nw = [(x-i, y-k) for i, k in zip(range(1, x+1), range(1, y+1))]
    ne = [(x+i, y-k) for i, k in zip(range(1, 8-x), range(1, y+1))]
    sw = [(x-i, y+k) for i, k in zip(range(1, x+1), range(1, 8-y))]
    se = [(x+i, y+k) for i, k in zip(range(1, 8-x), range(1, 8-y))]
    return [nw, ne, sw, se]


def getCross(x, y):
    n = [(x, y-i) for i in range(1, y+1)]
    w = [(x-i, y) for i in range(1, x+1)]
    s = [(x, y+i) for i in range(1, 8-y)]
    e = [(x+i, y) for i in range(1, 8-x)]
    return [n, w, s, e]


def checkPawn(pawn, x, y, board):
    n, w, s, e = getDirections(x, y)
    if isWhite(pawn):
        nw = inBounds(w, n) and isBlackKing(board[n][w])
        ne = inBounds(e, n) and isBlackKing(board[n][e])
        return nw or ne

    if isBlack(pawn):
        sw = inBounds(w, s) and isWhiteKing(board[s][w])
        se = inBounds(e, s) and isWhiteKing(board[s][e])
        return sw or se


def checkKnight(ele, x1, y1, board):
    area = getKnightMoves(x1, y1)
    for x, y in area:
        if inBounds(x, y):
            current = board[y][x]
            whitecheck = isWhite(ele) and current == "k"
            blackcheck = isBlack(ele) and current == "K"
            if whitecheck or blackcheck:
                return True
    return False


def checkBishop(piece, x, y, board):
    area = getDiagonals(x, y)
    return checkPiece(piece, board, area)


def checkRook(piece, x, y, board):
    area = getCross(x, y)
    return checkPiece(piece, board, area)


def checkQueen(piece, x, y, board):
    area = getDiagonals(x, y) + getCross(x, y)
    return checkPiece(piece, board, area)


def checkPiece(piece, board, area):
    for direction in area:
        for xCoord, yCoord in direction:
            current = board[yCoord][xCoord]
            whitecheck = isWhite(piece) and current == "k"
            blackcheck = isBlack(piece) and current == "K"
            if whitecheck or blackcheck:
                return True
            elif current != ".":
                break
    return False


def main():
    boards = handleInputV2()
    for val, board in enumerate(boards, 1):
        current = ChessBoard(board, val)
        current.checkForCheck()
        current.printResult()
    print()


if __name__ == '__main__':
    main()
