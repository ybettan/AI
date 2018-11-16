import random

def rand(x):
    rn = random.randint(0, 1000)
    if rn > x:
        return 0
    else:
        return rn

print(rand(0))
print(rand(100))
print(rand(500))
print(rand(1000))
