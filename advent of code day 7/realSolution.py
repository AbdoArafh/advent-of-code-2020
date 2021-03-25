with open("input.txt", 'r') as file:
    bags = file.read().split(".\n")

def parentBag(childBag):
    for bag in bagDict:
        content = bagDict[bag]
        if childBag in content:
            parentBag(bag)
            bagSet.add(bag)

bagSet = set()
bagDict = {}

for bag in bags:
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
    bag = bag.split(" contain ")
    try:
        bagDict[bag[0]] = bag[1]
    except:
        continue

parentBag("shiny gold")
print("number of bag that can eventually hold your bag is: " + str(len(bagSet)))