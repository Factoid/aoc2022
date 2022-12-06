f = open( 'input_6a.txt')
data = f.read()

i = 0
while len(set(data[i:i+4])) < 4:
    i += 1
    
print(i+4,data[i:i+4])