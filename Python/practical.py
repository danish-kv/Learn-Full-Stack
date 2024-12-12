# word = "wwoppopdbdhsblolkkokk"
# c = 0
# for i in range(len(word)):
#     temp = ''
#     for j in range(i+1,len(word)):
#         temp += word[j]
#         if len(temp) > 1:
#             if temp == temp[::-1]:
#                 c += 1
# # print(c)


# arr = [[1, 2], [3, [4, 5]], 6]
# # [6, [[5, 4], 3], [2, 1]
# def rev(arr):
#     res=[]
#     arr.reverse()
#     for i in arr:
#         if isinstance(i, list):
#             res.append(rev(i))
#         else:
#             res.append(i)
#     return res

# print(rev(arr))










""" Find Prime Number"""

# num = 7

# for i in range(2, num):
#     if num % i == 0:
#         print("Not a prime")
#         break
# else:
#     print("Yes its a prime")


"""Longest Consecutive Alphabetical Sequence"""

def long_consecutive_alpha(words):
    # words = 'abcdeacbdlmnopqrstuvwxyz'
    long = ''
    curr = words[0] if words else ""

    for i in range(1, len(words)):
        if ord(words[i]) == ord(words[i-1])+1:
            curr += words[i]
        else:
            if len(curr) > len(long):
                long = curr
            curr = words[i]
        
    return long



"""Longest Consecutive Repeated Characters"""

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



"""Custom Iterator for Fibnocci"""

class Fibnocci:
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
    
# fib = Fibnocci(10)

# for num in fib:
#     print(num)


""" SImple decorator"""
def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res[0].upper() + res[1]
    return wrapper


@decorator
def upper(a, b):
    return str(a), str(b)




""" Simple generator"""

def gen(limit):
    num = 1
    while num < limit:
        yield num
        num += 1
c = gen(10)
# for i in c:
#     print(i)

# print(next(c))

