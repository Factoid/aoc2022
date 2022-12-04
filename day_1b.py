f = open( "input_1a.txt", "rt" )

curElf = 0
totals = []
for l in f.readlines():
    if l == '\n':
        totals.append(curElf)
        curElf = 0
    else:
        curElf += int(l)
totals.sort()
print(totals[-1],totals[-2],totals[-3])
print(totals[-1]+totals[-2]+totals[-3])
