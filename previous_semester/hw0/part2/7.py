#!/bin/python3 -tt



import re
import sys


def string2real(str):
    res = re.split(r'\.', str)
    return list(map(int, res))


def main():
    str = sys.argv[1]
    res = string2real(str)
    print(res[0] + res[1])



if __name__ == '__main__':
    main()

