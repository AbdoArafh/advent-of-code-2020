import re

file = open("sorted_final_final.txt", "r")
ids = re.split("\n| ", file.read())
file.close()
for i in range(len(ids)-2, -1, -1):
    if ids[i].isdigit():
        ids[i] = int(ids[i])
    else:
        ids.remove(i)

rep = open("rep1.txt", "w+")
# for i in range(len(ids) - 1):
#     if ids[i] == ids[i+1] - 2:
#         rep.write("x")
#     else:
#         rep.write(".")
for i in range(1024):
    if i in ids:
        rep.write("x")
    else:
        rep.write(".")
    if (i + 1) % 128 == 0:
        rep.write("\n")
rep.close()
