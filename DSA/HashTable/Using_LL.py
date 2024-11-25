class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity) -> None:
        self.table = [None] * capacity
        self.size = capacity

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value ):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]

            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            
            current.next = Node(key, value)

    
    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            
            current = current.next
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False


h = HashTable(10)
h.insert('name','danish')
h.insert('name','sahal')
print(h.get('name'))
print(h.delete('name'))