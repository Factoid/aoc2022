import itertools

def ordered(left,right):
    #print("comparing",left,right)
    if type(left) == list and type(right) == list:
        for le,re in itertools.zip_longest(left,right):
            if le == None:
                return True
            if re == None:
                return False
            if type(le) == int and type(re) == int:
                if le < re:
                    return True
                if re < le:
                    return False
            elif type(le) == int:
                v = ordered([le],re)
                if v != None:
                    return v
            elif type(re) == int:
                v = ordered(le,[re])
                if v != None:
                    return v
            else:
                v = ordered(le,re)
                if v != None:
                    return v
                
    return None
    
f = open("input_13.txt")

index = 1
total = 0
while True:
    l = f.readline().strip()
    if l == "": break
    r = f.readline().strip()
    f.readline()
    
    left = eval(l)
    right = eval(r)
    
    #print("checking",left,right)
    if ordered(left,right):
        #print(left,right,"ordered!")
        total += index
    else:
        #print(left,right,"not ordered!")
        pass
    
    index += 1
    
print(total)