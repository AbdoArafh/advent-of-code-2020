input = open("input.txt", "r")
groups = input.read().split("\n\n")
input.close()

alphabet = list("abcdefghijklmnopqrstuvwxyz")
count = 0

for g in groups:
    people = g.split("\n")
    counter = [0] * len(alphabet)
    for p in people:
        for l in range(len(alphabet)):
            if p.find(alphabet[l]) != -1:
                counter[l] += 1
            if counter[l] == len(people):
                # print(alphabet[l])
                count += 1

print(count)

# a one liner, and not mine of course 😁😁
# print(sum(len(set.intersection(*map(set, entry.split()))) for entry in open("input.txt").read().split("\n\n")))








# for g in groups:
#     length = len(g.split("\n"))
#     counter = 0
#     for i in g.split("\n"):
#         for l in alphabet:
#             if g.find(l) != -1:
#                 counter += 1
#     if counter == len:
#         count += 1