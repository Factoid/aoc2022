class Monkey:
    def __init__(self, items, op, test):
        self.items = items
        self.op = op
        self.test = test
        self.inspected = 0
        
    def setup(self, trueTarget, falseTarget):
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        
    def inspect(self):
        self.inspected += len(self.items)
        self.items = [self.op(i)//3 for i in self.items]
        for i in self.items:
            if self.test(i):
                self.trueTarget.add(i)
            else:
                self.falseTarget.add(i)
        self.items = []
        
    def add(self,n):
        self.items.append(n)
        
#monkeys = [Monkey([79,98],lambda x: x*19, lambda x: x%23==0),
#           Monkey([54,65,75,74],lambda x: x+6, lambda x: x%19==0),
#           Monkey([79,60,97],lambda x: x*x, lambda x: x%13==0),
#           Monkey([74],lambda x: x + 3, lambda x: x%17==0)]
#monkeys[0].setup(monkeys[2],monkeys[3])
#monkeys[1].setup(monkeys[2],monkeys[0])
#monkeys[2].setup(monkeys[1],monkeys[3])
#monkeys[3].setup(monkeys[0],monkeys[1])

mList = [Monkey([91,54,70,61,64,64,60,85], lambda x: x*13, lambda x: x%2==0), #0
           Monkey([82],lambda x: x+7, lambda x: x%13==0), #1
           Monkey([84,93,70], lambda x: x+2, lambda x: x%5==0), #2
           Monkey([78,56,85,93], lambda x: x*2, lambda x: x%3==0), #3
           Monkey([64,57,81,95,52,71,58], lambda x: x*x, lambda x: x%11==0), #4
           Monkey([58,71,96,58,68,90], lambda x: x+6, lambda x: x%17==0), #5
           Monkey([56,99,89,97,81],lambda x: x + 1, lambda x: x%7==0), #6
           Monkey([68,72], lambda x: x+8, lambda x: x%19==0)] #7
           
mList[0].setup(mList[5],mList[2])
mList[1].setup(mList[4],mList[3])
mList[2].setup(mList[5],mList[1])
mList[3].setup(mList[6],mList[7])
mList[4].setup(mList[7],mList[3])
mList[5].setup(mList[4],mList[1])
mList[6].setup(mList[0],mList[2])
mList[7].setup(mList[6],mList[0])
         
for i in range(0,20):
    for m in mList:
        m.inspect()
        
mList.sort( key = lambda x: x.inspected, reverse = True )

for m in mList:
    print(m.inspected)
    
print(mList[0].inspected*mList[1].inspected)