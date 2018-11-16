import re
import functools

def func(s):
    numbers = re.split(r'\.', s)
    numbers = map(int, numbers)
    return functools.reduce(lambda x, y: x+y, numbers, 0)

print(func("3.4"))
print(func("5.5"))
print(func("7.3"))
