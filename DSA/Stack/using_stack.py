class Stack:
    def __init__(self, capacity) -> None:
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, data):
        if self.is_full():
            print('Stack overflow')
            return 
        
        self.top += 1
        self.stack[self.top] = data
    

    def pop(self):
        if self.is_empty():
            print('Stack Overflow')
            return
        popped = self.stack[self.top]
        self.top -= 1

        return popped

    def is_full(self):
        return self.top == self.capacity -1
    
    def is_empty(self):
        return self.top == -1
    
    def display(self):
        print(self.stack[:self.top+1])

s = Stack(10)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.pop())
print(s.is_empty())
print(s.is_full())
s.display()