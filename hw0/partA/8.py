import functools

def my_add(x, y):
    return x + y

def my_sum(l):
    return functools.reduce(my_add, l)


l = [1, 2, 3]
print(my_sum(l))
