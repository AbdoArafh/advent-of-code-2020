n = 10
grid = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
grid[0][0][0] = 1


def countNeighbors(x, y, z):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                neighbors += grid[x + i][y + j][z + k]
    return neighbors - grid[x][y][z]


def generate():
    global grid
    next = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    for x in range(1, n-1):
        for y in range(1, n-1):
            for z in range(1, n-1):
                neighbors = countNeighbors(x, y, z)
                next[x][y][z] = fate(neighbors, grid[x][y][z])
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
                counter += grid[i][j][k]
    return counter


with open("test.txt", 'r') as file:
    startingCells = file.read()

for i in range(6):
    print("the number of cells in the generation {} is: ".format(
        i + 1) + str(generate()))


print("number remaining = " + str(count()))
