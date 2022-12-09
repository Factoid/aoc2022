lRope = 10
rope = []
for i in range(0,lRope):
    rope.append([0,0])

visited = set()
visited.add(tuple(rope[-1]))

def moveTail(h,t):
    dx = h[0]-t[0]
    dy = h[1]-t[1]
    #print(h,t)
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
    elif( dx > 1 ):
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
            
    #print(h,t)
        
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
    
f = {"U":moveUp, "D":moveDown,"L":moveLeft,"R":moveRight}

file = open("input_9.txt")
commands = [l.strip() for l in file.readlines()]
#commands = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]

for c in commands:
    d,n = c.split(" ")
    n = int(n)
    #print(d,n)
    for i in range(0,n):
        a = rope[0]
        b = rope[1]
        #print("moving head")
        f[d](a,b)
        for i in range(1,len(rope)-1):
            #print("updating",i,i+1)
            a = rope[i]
            b = rope[i+1]
            moveTail(a,b)
        #print(rope)
        visited.add(tuple(rope[-1]))

print(len(visited))