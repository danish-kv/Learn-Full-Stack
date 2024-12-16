# Section 1: Palindrome Substrings

def count_palindromic_substrings(word):
    count = 0
    for i in range(len(word)):
        temp = ''
        for j in range(i + 1, len(word)):
            temp += word[j]
            if len(temp) > 1 and temp == temp[::-1]:
                count += 1
                print(temp)
    return count

# Example Usage
# word = "wwoppopdbdhsblolkkokk"
# print(count_palindromic_substrings(word))

# Section 2: Reverse Nested List

def reverse_nested_list(arr):
    arr.reverse()
    res = []
    for i in arr:
        if isinstance(i, list):
            res.append(reverse_nested_list(i))
        else:
            res.append(i)
    return res

# Example Usage
# nested_list = [[1, 2], [3, [4, 5]], 6]
# print(reverse_nested_list(nested_list))

# Section 3: Prime Number Check

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example Usage
# print(is_prime(7))



# Section 4: Longest Consecutive Alphabetical Sequence

def long_consecutive_repeated(words):
    # words = 'aaccbbuuuu'
    long = ''
    curr = words[0] if words else ''

    for i in range(1, len(words)):
        if words[i] == words[i-1]:
            curr += words[i]
            print(curr)
        else:
            if len(curr) > len(long):
                long = curr
            curr = words[i]

    if len(curr) > len(long):
        long = curr

    return long



def second_largest(arr=[1, 42, 3, 9, 23, 0, 11, 67, 50]):
    lar = sec = float('-inf')

    for i in range(len(arr)):
        if arr[i] > lar:
            sec = lar
            lar = arr[i]
        elif arr[i] < lar and arr[i] > sec:
            sec = arr[i]
    return sec



# Section 7: Fibonacci Iterator

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration

        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

# Example Usage
# for num in Fibonacci(10):
#     print(num)

# Section 8: Simple Decorator

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[0].upper() + result[1]
    return wrapper

@decorator
def sample_function(a, b):
    return str(a), str(b)

# Example Usage
# print(sample_function("hello", "world"))

# Section 9: Simple Generator

def simple_generator(limit):
    num = 1
    while num < limit:
        yield num
        num += 1

# Example Usage
# for value in simple_generator(10):
#     print(value)


# Section 10: Frequency Count of Each Character

def freq_count_each_char(words):
    # words = '`111233300866111'
    i = 0
    res = {}
    while i < len(words):
        temp = words[i]
        c = 0
        j = i
        word = ''
        while j < len(words) and temp == words[j]:
            word += temp
            c += 1
            j += 1
        
        if word in res:
            res[word] += 1
        else:
            res[word] = 1

        i = j
    return res

# print(res)




        
"""
 nested list reverse
"""

my_list = [1,2,[2,4,6],3,6,[9,[8],10]]


def nested_reverse(my_list):
    res = []
    for i in my_list:
        if isinstance(i, list):
            res.append(nested_reverse(i))
        else:
            res.append(i)
    
    return res[::-1]

# print(nested_reverse(my_list))


"""
 find how many palindrome strings
"""

def count_of_palindrom(words):
    # words = 'aadaalplooqqe'
    i  = 0
    c = 0
    while i < len(words):
        w = ''
        j = i
        while j < len(words):
            w += words[j]
            j += 1

            if w == w[::-1] and len(w) > 1:
                c += 1
                print(w)
        i += 1

    return c


"""
Interchange keys and values in dict
"""

my_dict = {'name' : 'danish', 'age' : 10}

# print({v : k for k, v in my_dict.items()})

for k, v in my_dict.items():
    val = v
    del my_dict[k]
    my_dict[val] = k

# print(my_dict)



"""
Remove duplicates from list (O(1) space complexity)
"""
my_list = [1, 2, 3, 4, 1, 3,12 , 1 ]

def remove_dup(nums):
    nums.sort()
    j = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        
    del nums[j+1:]
remove_dup(my_list)
# print(my_list)

"""
 count of days until new year
"""
from datetime import datetime

today = datetime.now()
next_year = datetime(year=today.year+1, month=1, day=1)

days_until_new_year = (next_year-today).days

# print(days_until_new_year)




# Q16: Print Prime Numbers Up to N

def print_primes_upto(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

# Example Usage
# print_primes_upto(10)



# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# def validate_age(age):
#     if age < 18:
#         raise CustomError('Age must be older than 18')
#     print('Valid age')

# validate_age(10)







# class Addition:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         return Addition(self.x + other.x , self.y + other.y)



# a1 = Addition(2, 3)
# a2 = Addition(4, 5)
# res = a1 + a2




my_dict = {'name': 'danish', 'place' : 'malappuram'}
long_val = 0
key = ''
for k, v in my_dict.items():
    if len(v) > long_val:
        long_val = len(v)
        key = k
my_dict.pop(key)
print(key)
print(my_dict)


squre = lambda x : x * x
squre_root = lambda x : x ** 0.5

print(squre(10))
print(squre_root(100))


res = 0
arr = [1, 'two', 'three', 4, 5]

for i in arr:
    if type(i) == int:
        res += i
print(res)











class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_next_even(self):
        if self.head is None:
            return False

        n = self.head
        while n.next:
            if n.next.val % 2 == 0:
                n.next = n.next.next
            else:
                n = n.next

        return True

    
    def delete_prev_even(self):
        if self.head and self.head.next is None:
            return False

        prev = None
        curr = self.head

        while curr:
            if curr.data % 2 == 0:
                if prev:
                    prev.next = curr.next