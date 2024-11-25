"""simple generotr"""

def gen():
    yield 1
    yield 2
    yield 3

generator = gen()
generator2 = gen()

print(generator.__next__()) 
print(generator.__next__())  
print(generator.__next__())  
print(generator2.__next__())  



def gen2(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for i in gen2(22):
    print(i)





def read_file(file):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_file('error.logs'):
    print(line)
    if line.startswith('ERROR'):
        print('Found error, stopping')
        break

