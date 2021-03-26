import math
n = 50
grid = [[[[0 for k in range(n)] for j in range(n)] for i in range(n)] for w in range(n)]

def loadStart():
    with open("test.txt", 'r') as file:
        cells = file.read().split()
    cols = len(cells)
    rows = len(cells[0])
    for i in range(cols):
        for j in range(rows):
            x = math.floor(n/2 - (cols/2) + i)
            y = math.floor(n/2 - (rows/2) + j)
            z = math.floor(n/2)
            w = math.floor(n/2)
            if cells[i][j] == '#':
                grid[x][y][z][w] = 1


def countNeighbors(x, y, z, w):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    try:
                        neighbors += grid[x + i][y + j][z + k][w + l]
                    except IndexError:
                        neighbors += 0
    return neighbors - grid[x][y][z][w]


def generate():
    global grid
    next = [[[[0 for k in range(n)] for j in range(n)] for i in range(n)] for l in range(n)]
    for x in range(n):
        for y in range(n):
            for z in range(n):
                for w in range(n):
                    neighbors = countNeighbors(x, y, z, w)
                    next[x][y][z][w] = fate(neighbors, grid[x][y][z][w])
    grid = next
    return count()


def fate(neighbors, state):
    if neighbors == 3:
        return 1
    elif neighbors == 2 and state == 1:
        return 1
    else:
        return 0


def count():
    counter = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    counter += grid[i][j][k][l]
    return counter


loadStart()

print("number of cells in the initial state is: " + str(count()))
for i in range(6):
    print("the number of cells in the generation {} is: ".format(
        i + 1) + str(generate()))
