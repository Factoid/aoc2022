import itertools
from functools import cmp_to_key
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
data = []
for l in f.readlines():
    l=l.strip()
    if l == "": continue
    #print(l)
    e = eval(l)
    if( e != None ):
        data.append(e)
        
data.append([[2]])
data.append([[6]])
data.sort(key=cmp_to_key(lambda a,b: -1 if ordered(a,b) == True else 1))
#for i in data:
#    print(i)   
a = data.index([[2]]) + 1
b = data.index([[6]]) + 1
print(a*b)