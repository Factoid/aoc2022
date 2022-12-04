f = open( "input_3a.txt" )

total = 0
group = []

for l in f.readlines():
    l = l.strip()
    group.append(set(l))
    if len(group) == 3:
        c = list(group[0].intersection(group[1],group[2]))[0]
#        print(c)
        
        if c >= 'a' and c <= 'z':
            p = ord(c) - ord('a') + 1
        elif c >= 'A' and c <= 'Z':
            p = ord(c) - ord('A') + 27
        total += p
        group = []
    
print(total)