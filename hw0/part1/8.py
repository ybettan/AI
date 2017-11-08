#!/bin/python3 -tt

import functools

def myadd(x, y):
    return x + y


def mysum(mylist):
    return functools.reduce(myadd, mylist)


def main():
    l = list(range(1, 4))
    print(mysum(l))



if __name__ == '__main__':
    main()

