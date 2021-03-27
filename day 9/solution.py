with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

preamble = 25
def check(index):
    if index < preamble:
        return True
    for i in range(index - preamble, index):
        for j in range(index - preamble, index):
            if data[i] + data[j] == data[index]:
                return True
    return False

data = list(map(int, data))
for i, number in enumerate(data):
    if not check(i):
        print(number)