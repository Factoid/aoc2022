f = open( "input_3a.txt" )

total = 0
for l in f.readlines():
    l = l.strip()
    si = len(l)//2
    #print(len(l), si)
    a = l[:si]
    b = l[si:]
    #print(a,b)
    setA = set(a)
    setB = set(b)
    #print(setA,setB)
    c = list(setA.intersection(setB))[0]
    if c >= 'a' and c <= 'z':
        p = ord(c) - ord('a') + 1
    elif c >= 'A' and c <= 'Z':
        p = ord(c) - ord('A') + 27
    total += p
    
print(total)