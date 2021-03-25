with open("input.txt", "r") as input:
    bags = input.read().split("\n")

shiny = "shiny gold"
counter = 0
bagsDict = {}

for bag in rules:
    bag = bag.replace(" bags", "").strip(".").replace(" bag", "")
    bag = bag.split(" contain ")
    try:
        bs = bag[1].split(", ")
    except:
        print(bag)
    if len(bs) > 0:
        try:
            bagsDict[bag[0]] = [bs[0][2:], bs[1][2:]]
        except:
            bagsDict[bag[0]] = [bs[0][2:], None]

broke = False
for i in bagsDict.values():
    for j in i:
        if broke:
            broke = False
            break
        try:
            b = bagsDict[j]
        except KeyError:
            continue
        if j == shiny:
            counter += 1
            break
        for k in b:
            if k == shiny:
                counter += 1
                broke = True;

print(counter)