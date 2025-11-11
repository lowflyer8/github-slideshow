class hashtable:
    
    def __init__(self,size=10):
        self.size = size
        self.table = [[]for _ in range(size)]
        
    def hashfunction(self,key):
        return key % self.size
    
    def insert(self , key , value):
        index = self.hashfunction(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"updated key {key} with value {value}")
                return
        self.table[index].append([key, value])
        print(f"inserted key {key} with value {value}")
        
    def search(self,key):
        index = self.hashfunction(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
            
        return None
    
    def delete(self,key):
        index= self.hashfunction(key)
        for i ,pair in enumerate(self.table[index]):
            if pair[0] == key :
                del self.table[index][i]
                print(f"deleted key {key}")
                return
        print(f"{key} not found for deletion.")
        
    def display(self):
        print("In hash table:")
        for i, bucket in enumerate(self.table):
            print(f"index{i}:{bucket}")
            
ht = hashtable()

ht.insert(15,"apple")
ht.insert(25,"banana")
ht.insert(35,"cherry")

print("search 25:",ht.search(25))

ht.delete(25)

print("search 25 after deletion:", ht.search(25))

ht.display()