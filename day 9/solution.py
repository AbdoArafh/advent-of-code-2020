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

value = int;
data = list(map(int, data))
for i, number in enumerate(data):
    if not check(i):
        value = number

print(value)

def weakness(length):
    if length == 100:
        return 0
    for i in range(len(data) - length):
        numbers = set()
        for j in range(length):
            numbers.add(data[i + j])
        if sum(numbers) == value:
            return numbers
    return weakness(length + 1)

values = weakness(2)
print('min:' + str(min(values)), 'max:' + str(max(values)), 'answer:' + str(min(values) + max(values)))