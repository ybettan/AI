
import functools

def is_perfect(x):
    dividers = [d for d in range(1, x) if x % d == 0]
    return functools.reduce(lambda x, y: x + y, dividers) == x

print(is_perfect(6))
