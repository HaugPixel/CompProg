import sys


def inBound(xCor, yCor, width, height):
    return (0 <= xCor < width) and (0 <= yCor < height)


def newImage(width, height):
    # Returns 2d array of O's
    return [['O' for _ in range(width)] for _ in range(height)]


def clearImage(array):
    if array:
        height = len(array)
        width = len(array[0])
        return newImage(width, height)
    else:
        return array


def colorPixel(array, x, y, color):
    array[y][x] = color
    return array


def drawVertilcal(array, x, y1, y2, color):
    for y in range(min(y1, y2), max(y1, y2)+1):
        array[y][x] = color
    return array


def drawHorizontal(array, x1, x2, y, color):
    for x in range(min(x1, x2), max(x1, x2)+1):
        array[y][x] = color
    return array


def colorFill(array, x, y, color):
    heigth = len(array)
    width = len(array[0])
    oldColor = array[y][x]
    if color == oldColor:
        return array
    array[y][x] = color

    # Finding Adjacent
    adjacentAdd = [(xAdd, yAdd) for xAdd in [-1, 0, 1] for yAdd in [-1, 0, 1] if abs(xAdd) != abs(yAdd)]
    adjecentCoords = [(x+xAdd, y+yAdd) for xAdd, yAdd in adjacentAdd if inBound(x+xAdd, y+yAdd, width, heigth)]

    # Depth First Search
    for xcor, ycor in adjecentCoords:
        if array[ycor][xcor] == oldColor:
            array = colorFill(array, xcor, ycor, color)
    return array


def drawSquare(array, x1, y1, x2, y2, color):
    square = [(xAdd, yAdd) for xAdd in range(min(x1, x2), max(x1, x2)+1) for yAdd in range(min(y1, y2), max(y1, y2)+1)]
    for x, y in square:
        array[y][x] = color
    return array


def imageEditor(cmdList, image=None):
    # Returns image according to commands

    if image is None:
        image = []
    array = image
    command = cmdList[0]
    
    if command == 'I':
        array = newImage(int(cmdList[1]), int(cmdList[2]))
    elif command == 'C':
        array = clearImage(array)
    elif command == 'L':
        array = colorPixel(array, int(cmdList[1])-1, int(cmdList[2])-1, cmdList[3])
    elif command == 'V':
        array = drawVertilcal(array, int(cmdList[1])-1, int(cmdList[2])-1, int(cmdList[3])-1, cmdList[4])
    elif command == 'H':
        array = drawHorizontal(array, int(cmdList[1])-1, int(cmdList[2])-1, int(cmdList[3])-1, cmdList[4])
    elif command == 'K':
        array = drawSquare(array, int(cmdList[1])-1, int(cmdList[2])-1, int(cmdList[3])-1, int(cmdList[4])-1, cmdList[5])
    elif command == 'F':
        array = colorFill(array, int(cmdList[1])-1, int(cmdList[2])-1, cmdList[3])
    elif command == 'S':
        print(cmdList[1])
        for y in array:
            print(''.join(y))
    elif command == 'X':
        sys.exit()
    return array


def main():
    image = []
    while True:
        command = sys.stdin.read(1)
        if command == 'X':
            sys.exit()
        xs = sys.stdin.readline()
        cmdlist = (command+xs).split()
        image = imageEditor(cmdlist, image)


main()
# print()
