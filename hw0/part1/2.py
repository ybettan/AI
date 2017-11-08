#!/bin/python3 -tt


import sys


def func(b):
    if b:
        return 1
    else:
        return -1



def main():
    res = func(int(sys.argv[1]) == 1)
    print(res)



if __name__ == "__main__":
    main()


