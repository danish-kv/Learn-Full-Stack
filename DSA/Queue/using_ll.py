class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    
    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front.next is None:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            