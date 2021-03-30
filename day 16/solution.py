import re

with open("test2.txt", 'r') as file:
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
    except TypeError:
        print(field, rule[0], rule[1])
    return False

def boundRule(field, rule):
    condition1 = int(field) >= int(rule[0][0]) and int (field) <= int(rule[0][1])
    condition2 = int(field) >= int(rule[1][0]) and int (field) <= int(rule[1][1])
    if condition1 or condition2:
        return True
    return False


def difference(firstList, secondSet):
    for i in range(len(firstList) - 1, -1, -1):
        if i in secondSet:
            firstList.pop(i)
    return firstList

def checkValidity(tickets, rules):
    valid = set()
    invalidTickets = set()
    invalid = list()
    for i, ticket in enumerate(tickets):
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
                invalidTickets.add(i)
    print(f"part one: {sumSet(invalid)}")
    return invalidTickets

nearbyTickets = [x.split(',') for x in rawTickets][1:]
titledRules = [re.split(': ', x)[1] for x in rawRules]
generalRules = [x.split(' or ') for x in titledRules]
lowsAndHighs = [[x.split('-') for x in y] for y in generalRules]
invalidTickets = checkValidity(nearbyTickets, lowsAndHighs)

# part two

validTickets = difference(nearbyTickets, invalidTickets)

def order(tickets, rules):
    order = []
    for i in range(len(tickets[0])):
        column = [x[i] for x in tickets]
        count = [0] * len(rules)
        for field in column:
            for j, rule in enumerate(rules):
                if boundRule(field, rule):
                    count[j] += 1
        for c in range(len(rules)):
            if count[c] == len(tickets):
                order.append(c)
                continue
    print(order)
    # print(len(rules))
    # print(rules)
    # print(count)

order(validTickets, lowsAndHighs)