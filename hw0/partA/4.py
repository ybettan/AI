import sys


a = int(sys.argv[1])
b = int(sys.argv[2])

a, b = b, a
print(a, b)
