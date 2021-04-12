from time import time

data = [0,8,15,2,12,1,4]

def take_turns(turns):
    spoken = {}
    for i, v in enumerate(data):
        spoken[v] = i + 1

    turn = len(spoken) + 1
    value = 0

    while turn < turns:

        if value in spoken:
            diff = turn - spoken[value]
        else:
            diff = 0

        spoken[value] = turn
        value = diff
        turn += 1

    return value

start = time()
print(f"part 1: {take_turns(2020)} and it took: {time() - start} seconds")
start = time()
print(f"part 1: {take_turns(30000000)} and it took: {time() - start} seconds")
