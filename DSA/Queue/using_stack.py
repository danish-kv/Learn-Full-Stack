class QueueUsingStack:
    def __init__(self) -> None:
        self.q1 = []
        self.q2 = []
    
    def enqueue(self, data):
        self.q1.append(data)
    
    def dequeue(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop())
        
        popped = self.q1.pop()

        while self.q2:
            self.q1.append(self.q2.pop())
        
        return popped