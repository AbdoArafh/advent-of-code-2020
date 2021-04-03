import re
import pandas as pd

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
    except TypeError:
        print(field, rule[0], rule[1])
    return False


def boundRule(field, rule):
    condition1 = int(field) >= int(
        rule[0][0]) and int(field) <= int(rule[0][1])
    condition2 = int(field) >= int(
        rule[1][0]) and int(field) <= int(rule[1][1])
    return condition1 or condition2


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

# part two _____________________________________________________________________________________________________

validTickets = difference(nearbyTickets, invalidTickets)
columnNames = [x.split(': ')[0] for x in rawRules]

def check(fields, rule):
    count = 0
    for field in fields:
        if boundRule(field, rule): count += 1
    if count == len(fields):
        return True
    return False

def order(tickets, rules):
    # todo please do it
    # df = pd.DataFrame(tickets, columns=columnNames)
    df = pd.DataFrame(tickets)
    order = list()
    for index in df.columns:
        col = list(map(int, df.loc[: ,index]))
        for ruleIndex, rule in enumerate(rules):
            if check(col, rule) and ruleIndex not in order:
                order.append(ruleIndex)
                break
    return order

def part2(order, ticket):
    sum = 1
    for i in range(6):
        try:
            sum *= int(ticket[order.index(i)])
        except ValueError:
            # pass
            print(f'value of not found index: {i}')
    print(f'part two: {sum}')


orderedRules = order(validTickets, lowsAndHighs)
print(orderedRules)
myTicket = data[1].split('\n')[1].split(',')
part2(orderedRules, myTicket)





# def order(tickets, rules):
#     # print(len(tickets), len(rules), len(tickets[0]))
#     order = []
#     for rule in rules:
#         count = [0] * len(tickets[0])
#         for ticket in tickets:
#             for fieldIndex, field in enumerate(ticket):
#                 if boundRule(field, rule):
#                     count[fieldIndex] += 1
#         # order.append(count.index(max(count)))
#         order.append(count.index(len(tickets)))
#     return order