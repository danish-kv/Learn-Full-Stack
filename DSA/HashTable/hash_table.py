class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
    
    def hash_funtion(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_funtion(key)

        if self.table[index] is None:
            self.table[index] = (key,value)
        else:
            self.table[index].append(key,value)

    def search(self, key):
        index = self.hash_funtion(key)
        
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
                
        return None
    
    def remove(self, key):
        index = self.hash_funtion(key)

        if self.table[index] is not None:
            for i, (k,_) in enumerate(self.table[index]):
                if key == k:
                    del self.table[index][i]
                    return
        
        return None
    
        
