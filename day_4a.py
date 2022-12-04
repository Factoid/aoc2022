f = open( "input_4a.txt" )

total = 0
group = []

def mkRange(s):
    a_s, a_e = s.split('-')
    return set(range(int(a_s),int(a_e)+1))
    
for l in f.readlines():
    l = l.strip()
    a,b = l.split(',')
    ar = mkRange(a)
    br = mkRange(b)
    if ar.issubset(br) or ar.issuperset(br):
        total += 1
        
print(total)