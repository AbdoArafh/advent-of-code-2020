def speak(list, target=2020):
    while len(list) != target:
        try:
            list.append(1 + list[::-1][1:].index(list[-1]))
        except ValueError:
            list.append(0)
    return list[-1]

print("part1: " + str(speak([0,8,15,2,12,1,4])))
print("part2: " + str(speak([0,8,15,2,12,1,4], 30000000)))

###########################################for testing in colors###################################
# input = open("test.txt", 'r').read().strip().split('\n\n')[0].split('\n')
# toCompare = list(map(int, open("test.txt", 'r').read().strip().split('\n\n')[1].split('\n')))
# for i, seq in enumerate(input):
    # value = speak(list(map(int, input[i].split(","))))
    # if value == toCompare[i]:
        # print('\033[92m' + "passed: " + str(value) + '\033[37m')
    # else:
        # print('\033[31m' + "failed: " + str(value) + '\033[37m')