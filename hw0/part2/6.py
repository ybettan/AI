#!/bin/python3 -tt


import sys
import random



def sub_list(list, num):
    
    res = []
    for i in range(num):
        res.append(random.choice(list)) 

    return res

def main():

    l = list(range(1, 10))
    num = int(sys.argv[1])
    print(sub_list(l, num))


if __name__ == '__main__':
    main()
    
