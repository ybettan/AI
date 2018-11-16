
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("my location is : ({}, {})".format(self.x, self.y))


p1 = Point(3, 4)
p1.show()

p2 = Point(1)
p2.show()

p3 = Point()
p3.show()
