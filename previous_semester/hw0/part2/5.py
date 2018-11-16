#!/bin/python3 -tt


import random
import sys


def is_random_bigger(n):
    rand = random.uniform(0, 1000)
    if rand > n:
        return 0
    else:
        return rand


def main():
    print(is_random_bigger(int(sys.argv[1])))


if __name__ == '__main__':
    main()

