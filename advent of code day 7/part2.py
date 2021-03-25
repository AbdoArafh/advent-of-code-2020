with open("input.txt", 'r') as file:
    bags = file.read().split(".\n")

bagDict = {}

def countChildren(parentBag):
    childrenBags = bagDict[parentBag];
    for child in childrenBags:
        bagName = child[2:]
        bagCount = int(child[:2])
        if bagName in counterDict:
            counterDict[bagName] += bagCount
        else:
            counterDict[bagName] = bagCount
        for i in range(bagCount):
            if bagName in bagDict:
                countChildren(bagName)

for bag in bags:
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
    bag = bag.split(" contain ")
    try:
        if "no other" in bag[1]:
            continue
        else:
            bagDict[bag[0]] = bag[1].split(", ")
    except:
        continue
    
counterDict = {}
countChildren("shiny gold")
print("number of bag that can eventually hold your bag is: " + str(sum(counterDict.values())))