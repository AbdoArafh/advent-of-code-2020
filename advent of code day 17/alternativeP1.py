from sys import argv

with open(argv[1], 'r') as file:
    seedCells = file.read().strip().split('\n')

def generate(active):
    new = set()
    xvals = [x[0] for x in active]
    yvals = [y[1] for y in active]
    zvals = [z[2] for z in active]

    for x in range(min(xvals) - 1, max(xvals) + 2):
        for y in range(min(yvals) - 1, max(yvals) + 2):
            for z in range(min(zvals) - 1, max(zvals) + 2):
                neighbors = 0
                for xoff in range(-1, 2):
                    for yoff in range(-1, 2):
                        for zoff in range(-1, 2):
                            if (x + xoff, y + yoff, z + zoff) in active:
                                neighbors += 1
                if (x, y, z) in active:
                    neighbors -= 1
                if (x, y, z) in active and neighbors == 2 or neighbors == 3:
                    new.add((x, y, z))
                elif (x, y, z) in active and neighbors == 3:
                    new.add((x, y, z))
    return new

active = set()
for row, c in enumerate(seedCells):
    for col, cell in enumerate(c):
        if (cell) == '#':
            active.add((row, col, 0))

for i in range(6):
    active = generate(active)
    print(f'the living cells in generation number {i + 1} is: {len(active)}')