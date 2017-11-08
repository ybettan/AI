#!/bin/python3 -tt


import functools
import sys

def myadd(x, y):
    return x + y


def is_perfect(num):
    dividers = [x for x in range(1, num) if num % x == 0]
    return functools.reduce(myadd, dividers) == num

def main():
    print (is_perfect(int(sys.argv[1])))


if __name__ == '__main__':
    main()


