f = open("input_10.txt")
data = [l.strip() for l in f.readlines()]
#data = ["noop","addx 3","addx -5"]

x_reg = 1
signals = []
cycle = 0

def checkCycle(cnum, reg, sig):
    targets = [20,60,100,140,180,220]
    if cnum in targets:
        #print("during cycle",cnum,"x_reg is",reg)
        sig.append(cnum*reg)
        
for d in data:
    if d == "noop":
        cycle += 1
        checkCycle(cycle,x_reg,signals)
    else:
        v = int(d.split(" ")[1])
        for n in range(0,2):
            cycle += 1
            checkCycle(cycle,x_reg,signals)
        x_reg += v
        #print( "after cycle",cycle,"x_reg is",x_reg)
        
print(signals,sum(signals))