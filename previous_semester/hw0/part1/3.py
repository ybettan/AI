#!/bin/python3 -tt



import sys

def power(x, y):
    return x ** y




def main():
    print(power(int(sys.argv[1]), int(sys.argv[2])))




if __name__ == '__main__':
    main()

