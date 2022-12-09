head = [0,0]
tail = [0,0]

visited = set()
visited.add(tuple(tail))

def moveTail(h,t):
    dx = h[0]-t[0]
    dy = h[1]-t[1]
    if( dy > 1 ):
        t[1] += 1
        if( dx > 0 ):
            t[0] += 1
        elif( dx < 0 ):
            t[0] -= 1
    elif dy < -1:
        t[1] -= 1
        if( dx > 0 ):
            t[0] += 1
        elif( dx < 0 ):
            t[0] -= 1
        
    if( dx > 1 ):
        t[0] += 1
        if( dy > 0 ):
            t[1] += 1
        elif( dy < 0 ):
            t[1] -= 1
    elif( dx < -1 ):
        t[0] -= 1
        if( dy > 0 ):
            t[1] += 1
        elif( dy < 0 ):
            t[1] -= 1
        
    #print( head, tail )
        
def moveUp(h,t):
    h[1] += 1
    moveTail(h,t)
    
def moveDown(h,t):
    h[1] -= 1
    moveTail(h,t)
    
def moveLeft(h,t):
    h[0] -= 1
    moveTail(h,t)

def moveRight(h,t):
    h[0] += 1
    moveTail(h,t)
    
#commands = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
f = {"U":moveUp, "D":moveDown,"L":moveLeft,"R":moveRight}

file = open("input_9.txt")
commands = [l.strip() for l in file.readlines()]

for c in commands:
    d,n = c.split(" ")
    n = int(n)
    for i in range(0,n):
        f[d](head,tail)
        visited.add(tuple(tail))

print(len(visited))