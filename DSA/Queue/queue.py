class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.front = self.rear = 0
    

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

