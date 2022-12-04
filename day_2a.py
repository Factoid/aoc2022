f = open( "input_2a.txt", "rt" )

score = 0
for l in f.readlines():
    a, b = l.strip().split(' ')
    if b == 'X':
        score += 1
    elif b == 'Y':
        score += 2
    elif b == 'Z':
        score += 3
        
    if a == 'A':
        if b == 'Y':
            score += 6
        elif b == 'X':
            score += 3
    elif a == 'B':
        if b == 'Z':
            score += 6
        elif b == 'Y':
            score += 3
    elif a == 'C':
        if b == 'X':
            score += 6
        elif b == 'Z':
            score += 3

print(score)
