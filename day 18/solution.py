import re
from sys import exit

with open('test.txt', 'r') as file:
    problems = file.read().strip().split("\n")[5]

# results = []
# for problem in problems:
#     exec('results.append(' + problem + ')')

# print(results)

# print(re.search(r"\(.+\)", problems[0]).group())

def solve(problem):
    if '(' in problem:
        # exep = r'(\((\(.+\)*)+\))'
        # exep = r'\((.*\(.+\).*)+?\)'
        exep = r'\((.*?\(.*?\).*?)+?\)'
        if bool(re.search(exep, problem)):
            matchObject = re.search(exep, problem)
            start = matchObject.start()
            end = matchObject.end()
            group = matchObject.group()[1:-1]
            # print(f"condition matched in: {problem} and group {group}")
        else:
            try:
                start = re.search(r'\(', problem).start()
                end = re.search(r'\)', problem).end()
                group = problem[start+1:end-1]
            except AttributeError:
                print(problem)
                exit()
            # print(f"condition didn't matched in: {problem}")
        # print(group)
        # try:
        return solve(problem[:start] + solve(group) + problem[end:])
        # except AttributeError:
        #     print(start, end, group)
        #     return problem

    exep = re.search(r'\d+ ?\D+? ?\d+', problem)
    if bool(exep):
        loc = {}
        exec("x = " + problem[exep.start():exep.end()], loc)
        x = loc['x']
        return solve(str(x)+ problem[exep.end():])
        # except IndexError:
            # return str(x)  
    else:
        return problem


print(solve(problems))
# print(sum([int(solve(x).strip()) for x in problems]))
# print([solve(x) for x in problems])