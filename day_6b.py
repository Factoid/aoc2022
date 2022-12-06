f = open( 'input_6a.txt')
data = f.read()

i = 0
while len(set(data[i:i+14])) < 14:
    i += 1
    
print(i+14,data[i:i+14])