f = open( "input_2a.txt", "rt" )

score = 0
for l in f.readlines():
    a, b = l.strip().split(' ')
    
    if b == 'X': #Lose
        if a == 'A': #Rock
            score += 3 #Scissors loses
        elif a == 'B': #Paper
            score += 1 #Rock loses
        elif a == 'C': #Scissors
            score += 2 #Paper loses
    elif b == 'Y': #Draw
        score += 3
        if a == 'A': #Rock
            score += 1
        elif a == 'B': #Paper
            score += 2
        elif a == 'C': #Scissors
            score += 3
    elif b == 'Z': #Win
        score += 6
        if a == 'A': #Rock
            score += 2 #Paper wins
        elif a == 'B': #Paper
            score += 3 #Scissors wins
        elif a == 'C': #Scissors
            score += 1 #Rock wins
                
print(score)
