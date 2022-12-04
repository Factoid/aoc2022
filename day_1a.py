f = open( "input_1a.txt", "rt" )

curElf = 0
bestTotal = 0
for l in f.readlines():
    if l == '\n':
        if curElf > bestTotal:
            bestTotal = curElf
        curElf = 0
    else:
        curElf += int(l)

print(bestTotal)
