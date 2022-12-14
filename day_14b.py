globalMinX = 500
globalMaxX = 500
globalMinY = 0
globalMaxY = 0
state = { (500,0) : '+' }

f = open("input_14.txt")
for l in f.readlines():
    l = l.strip()
    pairs = l.split(" -> ")
    prevX = -1
    prevY = -1
    for p in pairs:
        x,y = p.split(',')
        x = int(x)
        y = int(y)
        if x < globalMinX:
            globalMinX = x
        elif x > globalMaxX:
            globalMaxX = x
    
        if y < globalMinY:
            globalMinY = y
        elif y > globalMaxY:
            globalMaxY = y
            
        if prevX != -1:
            if x == prevX:
                min_Y = min(y,prevY)
                max_Y = max(y,prevY)
                for v in range(min_Y,max_Y+1):
                    state[(x,v)] = "#"
            else:
                min_X = min(x,prevX)
                max_X = max(x,prevX)
                for v in range(min_X,max_X+1):
                    state[(v,y)] = "#"
        prevX = x
        prevY = y

globalMinX -= 200
globalMaxX += 200
globalMaxY += 2
for x in range(globalMinX,globalMaxX):
    state[(x,globalMaxY)] = "#"
    
def dropSand(state,gY):
    p = [500,0]
    done = False
    while p[1] < gY+3:
        if (p[0],p[1]+1) not in state:
            p[1] += 1
        elif (p[0]-1,p[1]+1) not in state:
            p[0] -= 1
            p[1] += 1
        elif (p[0]+1,p[1]+1) not in state:
            p[0] += 1
            p[1] += 1
        else:
            state[tuple(p)] = "o"
            return p[0] != 500 or p[1] != 0
    
    print("failed!")
    return False

def printState(state):
    for y in range(globalMinY,globalMaxY+1):
        for x in range(globalMinX,globalMaxX+1):
            if (x,y) in state:
                print(state[(x,y)],end='')
            else:
                print(' ',end='')
        print()

i = 1
while dropSand(state,globalMaxY):
    #if i in [1,5,22,24]:
    #    print("at step",i)
    #    printState(state)
    i += 1
    
print(i)
#printState(state)