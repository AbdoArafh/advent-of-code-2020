import re

with open("input.txt", 'r') as file:
    data = file.read().split('\n\n')

rawRules = data[0].split('\n')
rawTickets = data[2].split('\n')

def sumSet(strSet):
    sum = 0
    for i in strSet:
        try:
            sum += int(i)
        except ValueError:
            pass
    return sum

def bounded(field, rule):
    try:
        if int(field) >= int(rule[0]) and int(field) <= int(rule[1]):
            return True
    except ValueError:
        pass
    return False

def checkValidity(tickets, rules):
    valid = set()
    invalid = list()
    for ticket in tickets:
        for field in ticket:
            count = 0
            for rule in rules:
                for bound in rule:
                    if bounded(field, bound):
                        valid.add(field)
                    else:
                        count += 1
            if count == (len(rules) * len(rule)):
                invalid.append(field)
    return sumSet(invalid)

nearbyTickets = [x.split(',') for x in rawTickets][1:]
titledRules = [re.split(': ', x)[1] for x in rawRules]
generalRules = [x.split(' or ') for x in titledRules]
lowsAndHighs = [[x.split('-') for x in y] for y in generalRules]
answer = checkValidity(nearbyTickets, lowsAndHighs)
print(answer)
# print(sumSet(answer))
# print(lowsAndHighs)