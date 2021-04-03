import re

with open('test.txt', 'r') as file:
    problems = file.read().strip().split("\n")[0]

# results = []
# for problem in problems:
#     exec('results.append(' + problem + ')')

# print(results)

# print(re.search(r"\(.+\)", problems[0]).group())

def solve(problem):
    if '(' in problem:
        # print(problem[:re.search(r"\(.+\)", problem).start()])
        # print(re.search(r"\(.+\)", problem).group()[1:-1])
        # print(problem[re.search(r"\(.+\)", problem).end():])
        return solve(problem[:re.search(r"\(.+\)", problem).start()] + solve(re.search(r"\(.+\)", problem).group()[1:-1])
            + problem[re.search(r"\(.+\)", problem).end():])

    if len(problem) >= 5:
        loc = {}
        # print(" ".join(problem.split(" ")[:3]))
        exec("x = " + " ".join(problem.split(" ")[:3]), loc)
        x = loc['x']
        try:
            # return solve(str(x) + problem[3:])
            return solve(str(x) + " " + " ".join(problem.split(" ")[3:]))
        except IndexError:
            return str(x)
    else:
        return problem
        
# print(sum[int(solve(problem)) for problem in problems])
# print(sum([int(solve(x)) for x in problems]))
print(solve(problems))