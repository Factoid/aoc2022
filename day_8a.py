import random
from colorama import Fore, Back, Style
f = open( "input_8a.txt" )
data = []

h = 0
for l in f.readlines():
    l = l.strip()
    w = len(l)
    h += 1
    data.extend( [int(c) for c in l] )

#w,h = 5,5
#data = [random.randint(0,9) for x in range((w+1)*(h+1))]

vis = [0] * len(data)

def get(x,y,l):
    global w
    return l[(y*w)+x]

def setVis(x,y):
    global vis,w
    vis[(y*w)+x] = 1
    
def getRow(y, l):
    global w
    return l[y*w:(y+1)*w]

def getCol(x, l):
    global w,h
    return l[x:h*w+x:w]

for x in range(0,w):
    c = getCol(x,data)
    print(len(c))
    print("".join([str(i) for i in c]))
    ma = -1
    mb = -1
    for y in range(0,h):
        if c[y] > ma:
            ma = c[y]
            setVis(x,y)
        yb = -(y+1)
        if c[yb] > mb:
            mb = c[yb]
            setVis(x,h+yb)

for y in range(0,h):
    r = getRow(y,data)
    #print("".join([str(i) for i in r]))
    ma, mb = -1, -1
    for x in range(0,w):
        if r[x] > ma:
            ma = r[x]
            setVis(x,y)
        xb = -(x+1)
        if r[xb] > mb:
            mb = r[xb]
            setVis(w+xb,y)
    #print("".join([str(i) for i in getRow(y,vis)]))
            
for y in range(0,h):
    line = Back.BLACK
    for x in range(0,w):
        if get(x,y,vis) == 1:
            line += Fore.GREEN
        else:
            line += Fore.RED
        line += str(get(x,y,data))
    print(line+Style.RESET_ALL)
    
print(Style.RESET_ALL)

print( vis.count(1) )