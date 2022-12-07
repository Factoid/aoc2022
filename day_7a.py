class d_node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = { }
        self.files = { }
        self.sizeCache = None
    
    def add_dir(self, name ):
        self.dirs[name] = d_node(name,self)
    
    def add_file(self, name, size):
        self.files[name] = size
    
    def size(self):
        if( self.sizeCache == None ):
            self.sizeCache = sum(self.files.values()) + sum( [d.size() for d in self.dirs.values()] )
        return self.sizeCache
    
root = d_node("/", None)
cur = None

def parseCommand(l):
    global cur, root
    
    if( l == "$ cd /" ):
        cur = root
    elif( l == "$ cd .."):
        cur = cur.parent
    elif( l == "$ ls" ):
        pass
    else:
        dname = l[5:]
        cur = cur.dirs[dname]
        
def parseEntry(l):
    global cur
    
    if l.startswith("dir"):
        cur.add_dir( l[4:] )
    else:
        size_str, name = l.split(' ')
        size = int(size_str)
        cur.add_file( name, size )
        
f = open( "input_7a.txt" )
for l in f.readlines():
    l = l.strip()
    if( l[0] == "$" ):
        parseCommand(l)
    else:
        parseEntry(l)
        
walk = [root]
total = 0
while len(walk) > 0:
    c = walk[0]
    print( c.name, c.size() )
    if c.size() <= 100000:
        total += c.size()
    walk.pop(0)
    walk.extend( c.dirs.values() )
    
print(total)