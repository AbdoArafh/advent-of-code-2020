#one liner in a dirty way for part 1
print("part 1: " + str([x for x in [[i * j for j in list(map(int, open("input.txt", 'r').read().strip().split("\n"))) if i + j == 2020] for i in list(map(int, open("input.txt", 'r').read().strip().split("\n")))] if x != []][0])[1:-1])

# dirty and slow one liner for part 2
print("part 2: " + str([value for value in [[_ for _ in r if _ != []] for r in [[[x * y * z for z in list(map(int, open("input.txt", 'r').read().strip().split("\n"))) if x + y + z == 2020] for y in list(map(int, open("input.txt", 'r').read().strip().split("\n")))] for x in list(map(int, open("input.txt", 'r').read().strip().split("\n")))]] if value != []][0][0])[1:-1])


# three liner in clean way
    # input = list(map(int, open("input.txt", 'r').read().strip().split("\n")))
    # raw = [[x * y for y in input if x + y == 2020] for x in input]
    # print("part 1: " + str([x for x in raw if x != []][0])[1:-1])


#a bit clean three liner for part 2
    # input = list(map(int, open("input.txt", 'r').read().strip().split("\n")))
    # raw = [[[x * y * z for z in input if x + y + z == 2020] for y in input] for x in input]
    # print("part 2: " + str([value for value in [[_ for _ in r if _ != []] for r in raw] if value != []][0][0])[1:-1])


def part1():
    for i in open('input.txt').read().split('\n'):
        for j in open('input.txt').read().split('\n'):
            try:
                if int(i) + int(j) == 2020:
                    print("part one: " + str(int(i) * int(j)))
                    return
            except ValueError:
                pass

def part2():
    for i in open('input.txt').read().split('\n'):
        for j in open('input.txt').read().split('\n'):
            for k in open('input.txt').read().split('\n'):
                try:
                    if int(i) + int(j) + int(k) == 2020:
                        print("part one: " + str(int(i) * int(j) * int(k)))
                        return
                except ValueError:
                    pass

# part1()
# part2()


