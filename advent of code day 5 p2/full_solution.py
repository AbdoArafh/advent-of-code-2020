input = open("input.txt", "r")
seqs = input.read().split("\n")
input.close()
def findCol(command):
    low = 0;
    high = 7;
    mid = -1;
    for i in command:
        mid = low + ((high - low) / 2)
        if i == "R":
            low = mid + 1
        elif i == "L":
            high = mid
    return int(low + ((high - low) / 2))
def findRow(command):
    low = 0
    high = 127
    mid = -1
    for i in command:
        mid = round(low + ((high - low) / 2))
        if i == "B":
            low = mid
        else:
            high = mid
    return int(low + (high - low) / 2)

ids = []
for s in seqs:
    rseq = s[:7]
    cseq = s[7:]
    rows = findRow(rseq)
    cols = findCol(cseq)
    print(rows, end=" ")
    print(cols)
    ids.append((int(rows) * 8) + int(cols))

rep = open("rep2.txt", "w+")
for i in range(1024):
    if i in ids:
        rep.write("x")
    else:
        rep.write(".")
        # print(i)
    if (i + 1) % 128 == 0:
        rep.write("\n")
rep.close()