def vannPaaSten(x, y, startGrid):
    startGrid[y][x] = "V"
    if startGrid[y+1][x] == ".":
        startGrid[y+1][x] = "V"
    elif y < rows and x < columns and startGrid[y+1][x] == "#":
        if x+1 < columns and startGrid[y][x+1] == ".":
            startGrid = vannPaaSten(x+1, y, startGprid)
        if 0 < x-1 and startGrid[y][x-1] == ".":
            startGrid = vannPaaSten(x-1, y, startGprid)
    return startGrid


rows, columns = [int(i) for i in input().split()]
grid = [['' for _ in range(columns)] for _ in range(rows)]

startGprid = []
for k in range(rows):
    startGprid.append([])
    for j in input():
        startGprid[len(startGprid)-1].append(j)

for y, linje in enumerate(startGprid):
    for x, ele in enumerate(linje):
        if ele == "V":
            startGprid = vannPaaSten(x, y, startGprid)


