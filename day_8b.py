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
#data = [random.randint(0,9) for x in range((w)*(h))]
#print(len(data))

vis = [1] * len(data)

def get(x,y,l):
    global w
    i = (y*w)+x
    if i < 0 or i >= len(l):
        print("Error:",x,y,"out of range")
        return -1
    return l[i]

def multVis(x,y,v):
    global vis,w
    vis[(y*w)+x] *= v
    
def getRow(y, l):
    global w
    return l[y*w:(y+1)*w]

def getCol(x, l):
    global w,h
    return l[x:h*w+x:w]

def calcScore(x,y):
    global data,vis,w,h
    
    v = get(x,y,data)
    c = getCol(x,data)
    r = getRow(y,data)
    
    n = 0
    for i in range(x-1,-1,-1):
        n += 1
        if get(i,y,data) >= v: break
    multVis(x,y,n)
    n = 0
    for i in range(x+1,w):
        n += 1
        if get(i,y,data) >= v: break 
    multVis(x,y,n)
    n = 0
    for i in range(y-1,-1,-1):
        n += 1
        if get(x,i,data) >= v: break
    multVis(x,y,n)        
    n = 0
    for i in range(y+1,h):
        n += 1
        if get(x,i,data) >= v: break
    multVis(x,y,n)
        
for x in range(0,w):
    for y in range(0,h):
        calcScore(x,y)

#for y in range(0,h):
#    print( "".join([str(i) for i in getRow(y,data)]))
#    
#print()
#
#for y in range(0,h):
#    print(getRow(y,vis))
#    line = Back.BLACK
#    for x in range(0,w):
#        if get(x,y,vis) == 1:
#            line += Fore.GREEN
#        else:
#            line += Fore.RED
#        line += str(get(x,y,data))
#    print(line+Style.RESET_ALL)
    
#print(Style.RESET_ALL)

print( max(vis) )