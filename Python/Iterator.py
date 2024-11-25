"""Simple Iterator"""

my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3



"""Custom Iterator"""

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        raise StopIteration

for num in MyIterator([10, 20, 30]):
    print(num)
