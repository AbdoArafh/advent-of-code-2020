with open("input.txt", 'r') as file:
    instructions = file.read().split('\n')

# insted of making execute stupidly big
def run(index, acc):
    kind = instructions[index][:3]
    operation = instructions[index][4]
    amount = int(instructions[index][5:])
    if index not in visited:
        visited.append(index)
        accValues.append(acc)
        if kind == "acc":
            if "+" == operation:
                acc += amount
                execute(index + 1, acc)
            elif "-" == operation:
                acc -= amount
                execute(index + 1, acc)
        elif kind == "jmp":
            if "+" == operation:
                execute(index + amount, acc)
            elif "-" == operation:
                execute(index - amount, acc)
        elif kind == "nop":
            execute(index + 1, acc)
    else:
        print("it crashes when the acc is: " + str(acc))
        return

# executes teh instructions from the giving index
def execute(index, acc):
    try:
        run(index, acc)
    except IndexError:
        print("when it runs smoothly the accumulator is: " + str(acc))


visited = []
accValues = []
execute(0, 0)


def fix(index):
    if "nop" in instructions[index]:
        instructions[index] = instructions[index].replace("nop", "jmp")
    elif "jmp" in instructions[index]:
        instructions[index] = instructions[index].replace("jmp", "nop")
    return instructions

# testin g a few possiblities to see whitch of them works instead of a smart thing
for index in range(20):
    instructions = fix(visited[-index])
    visited = []
    execute(0, 0)
