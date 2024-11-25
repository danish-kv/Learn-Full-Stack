class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self, data) -> None:
        self.head = None

    def _print(self):
        if self.head is None:
            print('LL is empty')
            return
        n = self.head
        while n is not None:
            print(n.data, '-->', end="")
            n = n.next

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is Node:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n = n.next
            
            n.next = new_node