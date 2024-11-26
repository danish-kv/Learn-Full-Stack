class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self) -> None:
        self.head = None

    
    def add_anywhere(self, data, pos):
        new_node = Node(data)
        if pos < 0:
            if self.head is None:
                self.head = new_node
            else:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
            return
        n = self.head
        c = 0

        while n is not None and c < pos -1 :
            n = n.next
            c += 1
        
        if n is None or n.next is None:
            n.next = new_node
            new_node.prev = n
        else:
            new_node.next = n.next
            new_node.prev = n
            n.next.prev = new_node
            n.next = new_node
            
    def display(self):
        if self.head is None:
            print('DLL not found')
        else:
            n = self.head
            while n  is not None:
                print(n.data,  end=' ')
                n = n.next

d = DLL()
d.add_anywhere(10, -1)
d.add_anywhere(110, -2)
d.add_anywhere(10, 6)
d.display()