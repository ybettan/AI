
def my_reverce1(l):
    return list(reversed(l))

def my_reverce2(l):
    l.reverse()

def add_2(l, x, y):
    l.append(x)
    l.append(y)


l = []
add_2(l, 2, 4)
reversed_l = my_reverce1(l)
print(reversed_l)

l = []
add_2(l, 3, 5)
my_reverce2(l)
print(l)
