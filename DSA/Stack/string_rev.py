stack = []
words = 'my name is dansh'

for i in words:
    stack.append(i)

res = ''
while stack:
    # print(stack.pop())
    res += stack.pop()

print(res)