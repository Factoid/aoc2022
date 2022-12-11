class Monkey:
    limit = 1
    def __init__(self, n, items, op, div):
        self.id = n
        self.items = items
        self.op = op
        self.div = div
        self.inspected = 0
        Monkey.limit*=div
        
    def setup(self, trueTarget, falseTarget):
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        
    def inspect(self):
        self.inspected += len(self.items)
        self.items = [self.op(i)%(Monkey.limit) for i in self.items]
        for i in self.items:
            if i%self.div == 0:
                self.trueTarget.add(i)
            else:
                self.falseTarget.add(i)
        self.items = []
        
    def add(self,n):
        self.items.append(n)

def testList():
    mList = [Monkey(0,[79,98],lambda x: x*19, 23),
         Monkey(1,[54,65,75,74],lambda x: x+6, 19),
         Monkey(2,[79,60,97],lambda x: x*x, 13),
         Monkey(3,[74],lambda x: x + 3, 17)]
    mList[0].setup(mList[2],mList[3])
    mList[1].setup(mList[2],mList[0])
    mList[2].setup(mList[1],mList[3])
    mList[3].setup(mList[0],mList[1])
    return mList

def realList():
    mList = [Monkey(0,[91,54,70,61,64,64,60,85], lambda x: x*13, 2), #0
           Monkey(1,[82],lambda x: x+7, 13), #1
           Monkey(2,[84,93,70], lambda x: x+2, 5), #2
           Monkey(3,[78,56,85,93], lambda x: x*2, 3), #3
           Monkey(4,[64,57,81,95,52,71,58], lambda x: x*x, 11), #4
           Monkey(5,[58,71,96,58,68,90], lambda x: x+6, 17), #5
           Monkey(6,[56,99,89,97,81],lambda x: x + 1, 7), #6
           Monkey(7,[68,72], lambda x: x+8, 19)] #7
           
    mList[0].setup(mList[5],mList[2])
    mList[1].setup(mList[4],mList[3])
    mList[2].setup(mList[5],mList[1])
    mList[3].setup(mList[6],mList[7])
    mList[4].setup(mList[7],mList[3])
    mList[5].setup(mList[4],mList[1])
    mList[6].setup(mList[0],mList[2])
    mList[7].setup(mList[6],mList[0])
    return mList

mList = realList()
for i in range(1,10001):
    for m in mList:
        m.inspect()
    if i in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
        print("round",i)
        for m in mList:
            print(m.inspected)

mList.sort( key = lambda x: x.inspected, reverse = True )
print(mList[0].inspected*mList[1].inspected)