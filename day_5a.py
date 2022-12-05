import re

f = open( 'input_5a.txt')

doneHeader = False
stacks = {}
while True:
    l = f.readline()[1::4]
    if l[0] == '1':
        break
    for i in range(1,len(l)+1):
        if i not in stacks:
            stacks[i] = []
        if l[i-1] != ' ':
            stacks[i].insert(0,l[i-1])

print(stacks)
prog = re.compile( "move (\d+) from (\d+) to (\d+)" )
for l in f.readlines():
    m = prog.match(l.strip())
    if m == None:
        continue
    
    n, s, d = [int(x) for x in m.groups()]
    for i in range(0,n):
        v = stacks[s].pop()
        stacks[d].append(v)
print(stacks)
out = [ x[-1] for x in stacks.values()]
print(''.join(out))