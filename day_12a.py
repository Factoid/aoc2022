class Terrain:
    def __init__(self,data,width):
        self.hMap = data
        self.width = width
        self.height = len(data)//width

        i = self.hMap.index('S')
        self.start = [i%self.width,i//self.width]
        self.moves = [-1]*len(self.hMap)
        
        i = self.hMap.index('E')
        self.target = [i%self.width,i//self.width]
        print("start",self.start,"end",self.target)
       
    def printMap(self):
        for i in range(0,self.height):
            print( self.hMap[i*self.width:(i+1)*self.width])
        
    def printMoves(self):
        for i in range(0,self.height):
            print( self.moves[i*self.width:(i+1)*self.width])
            
    def totalCost(self):
        i = self.hMap.index('E')
        return self.moves[i]

    def get(self,pos,offset=[0,0]):
        x = pos[0] + offset[0]
        if x < 0 or x >= self.width: return None
        y = pos[1] + offset[1]
        if y < 0 or y >= self.height: return None
        
        v = self.hMap[y*self.width+x]
        if v == 'S':
            v = 'a'
        if v == 'E':
            v = 'z'
        return v
    
    def setCost(self,pos,cost):
        i = pos[1]*self.width+pos[0]
        if self.moves[i] == -1 or cost < self.moves[i]:
            self.moves[i] = cost
            return True
        
        return False
    
    def findPath(self):
        toVisit = [(self.start,0)]
        
        while len(toVisit) > 0:
            pos,cost = toVisit.pop(0)
            if self.setCost(pos,cost):
                #print("checking",pos)
                if pos[0] == self.target[0] and pos[1] == self.target[1]:
                    #print("found early")
                    return
        
                h = self.get(pos)
                hUp = self.get(pos,[0,-1])
                if hUp != None and ord(hUp)-ord(h) <= 1:
                    toVisit.append(([pos[0],pos[1]-1],cost+1))
        
                hDown = self.get(pos,[0,1])
                if hDown != None and ord(hDown)-ord(h) <= 1:
                    toVisit.append(([pos[0],pos[1]+1],cost+1))
             
                hLeft = self.get(pos,[-1,0])
                if hLeft != None and ord(hLeft)-ord(h) <= 1:
                    toVisit.append(([pos[0]-1,pos[1]],cost+1))
        
                hRight = self.get(pos,[1,0])
                if hRight != None and ord(hRight)-ord(h) <= 1:
                    toVisit.append(([pos[0]+1,pos[1]],cost+1))
 
f = open("input_12.txt")
width = 0
data = []
for l in f.readlines():
    l = l.strip()
    width = len(l)
    data.extend(l)

#data = list("Sbcdefghzzzzzzzzqrstuvwxyz") + list("abcdefghijklmnopqrstuvwxyz")*3 + list("abcdefghzzzzzzzzEzzzyxwxyE")
#width = 26
myMap = Terrain(data,width)
#myMap = Terrain(list("SabqponmabcryxxlaccszExkacctuvwjabdefghi"),8)
myMap.findPath()
print(myMap.totalCost())
#myMap.printMoves()
#myMap.printMap()