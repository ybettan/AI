import sys

def func(b):
    if b:
        return 1
    else:
        return -1


arg = int(sys.argv[1])
print(func(arg))
