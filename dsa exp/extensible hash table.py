class bucket:
    def __init__(self,depth,size):
        self.depth = depth
        self.items = {}
        self.size = size
        
    def isfull(self):
        return len(self.items) >=self.size
    
    def insert(self,key,value):
        self.items[key]=value
        
    def delete(self,key):
        if key in self.items:
            del self.items[key]
            
    def search(self,key):
        return self.items.get(key,None)
    
class extendiblehashtable:
    def __init__(self , bucketsize=2):
        self.globaldepth = 1
        self.bucketsize = bucketsize
        self.directory = [bucket(self.globaldepth,bucketsize) for _ in range(2)]
        
    def hash(self,key):
        return hash(key) & ((1 << self.globaldepth) - 1)
    
    def insert(self,key,value):
        index = self.hash(key)
        bucket = self.directory[index]
        
        if key in bucket.items or not bucket.isfull():
            bucket.insert(key,value)
            print(f"inserted({key},{value}) into bucket {index}")
            return
        
        print(f"bucket {index} is full. splitting...")
        self.splitbucket(index)
        self.insert(key,value)
        
    def splitbucket(self,index):
        oldbucket = self.directory[index]
        localdepth = oldbucket.depth
        oldbucket.depth += 1
        
        if oldbucket.depth > self.globaldepth:
            self.doubledirectory()
            
        newbucket = bucket(oldbucket.depth , self.bucketsize)
        
        for i in range (len(self.directory)):
            if self.directory[i] is oldbucket and ((i >> localdepth) & 1):
                self.directory[i] = newbucket
                
        olditems = list(oldbucket.items.items())
        oldbucket.items.clear()
        
        for k , v in olditems :
            self.insert(k,v)
            
    def doubledirectory(self):
        print("doubling directory size.")
        self.directory += self.directory
        self.globaldepth += 1
        
    def search(self,key):
        index = self.hash(key)
        value= self.directory[index].search(key)
        
        if value is not None :
            print(f"found key {key} with value {value} in bucket {index}")
        else:
            print(f"key {key} not found")
            
        return value
    
    def delete(self,key):
        index = self.hash(key)
        bucket = self.directory[index]
        
        if key in bucket.items:
            bucket.delete(key)
            print(f"key {key} deleted from bucket {index}")
        else:
            print(f"key {key} not found for deletion.")
            
    def display(self):
        seen = set()
        print("in directory:")
        for i, bucket in enumerate(self.directory):
            if id(bucket) not in seen:
                seen.add(id(bucket))
                print(f"bucket {i} (depth = {bucket.depth}): {bucket.items}")
                
ht = extendiblehashtable(bucketsize=2)

ht.insert(1, "one")
ht.insert(2,"two")
ht.insert(3,"three")
ht.insert(4,"four")
ht.insert(5,"five")

ht.display()

ht.search(3)
ht.delete(3)
ht.search(3)

ht.display()