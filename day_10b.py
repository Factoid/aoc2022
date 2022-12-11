f = open("input_10.txt")
data = [l.strip() for l in f.readlines()]
#data = ["noop","addx 3","addx -5"]

x_reg = 1
signals = []
cycle = 0

def checkCycle(cnum, reg, sig):
    p = cnum%40
    if p >= reg and p < reg + 3:
        sig.append("#")
    else:
        sig.append(".")
        
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

n = len(signals)//40
for i in range(0,n):
    print("".join(signals[i*40:(i+1)*40]))

#print(signals,sum(signals))