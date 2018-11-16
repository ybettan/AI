#!/bin/python3 -tt


class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print('my location is : ({}, {})'.format(self.x, self.y))




def main():
    
    p1 = Point(4,1)
    p1.show()

    p2 = Point(7,2)
    p2.show()

    p3 = Point()
    p3.show()

    p4 = Point(5)
    p4.show()

if __name__ == '__main__':
    main()
    
