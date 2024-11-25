def square(x):
    return x * x

def my_map(func, args_list):
    res = []
    for i in args_list:
        res.append(func(i))    
    return res

print(my_map(square,[2, 6,2, 6, 16, 86]))