import random

def func(l, num):
    res = []
    for i in range(num):
        res.append(random.choice(l))
    return res

l = [x for x in range(100) if x % 2 == 0]
print(func(l, 3))
