from utils import MiniMaxAlgorithm
import sys


class State:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, value):
        self.left = State(value)

    def set_right(self, value):
        self.right = State(value)

    def print_tree(self):
        if self.left == None or self.right == None:
            return
        print("{}.left = {} {}.right = {}".format(self.value, self.left.value, \
                self.value, self.right.value))
        self.left.print_tree()
        self.right.print_tree()

def utility(state):
    return state.value

def no_more_time():
    return False

def no_more_time2():
    no_more_time2.time -= 1
    if no_more_time2.time <= 0:
        return True
    else:
        return False

def asssert(cond):
    if not cond:
        print("ERROR")
        sys.exit(1)

#asssert(no_more_time2.time == 5)
#asssert(no_more_time2() == False)
#asssert(no_more_time2.time == 4)
#asssert(no_more_time2() == False)
#asssert(no_more_time2.time == 3)
#asssert(no_more_time2() == False)
#asssert(no_more_time2.time == 2)
#asssert(no_more_time2() == False)
#asssert(no_more_time2.time == 1)
#asssert(no_more_time2() == True)
#asssert(no_more_time2.time == 0)
#asssert(no_more_time2() == True)
#asssert(no_more_time2.time == -1)

# set up tree
root = State(1)
root.set_left(2)
root.set_right(3)
root.left.set_left(4)
root.left.set_right(5)
root.right.set_left(6)
root.right.set_right(7)
root.left.left.set_left(8)
root.left.left.set_right(9)
root.left.right.set_left(10)
root.left.right.set_right(11)
root.right.left.set_left(12)
root.right.left.set_right(13)
root.right.right.set_left(14)
root.right.right.set_right(15)


# chek min-max without time consideration
mma = MiniMaxAlgorithm(utility, 'X', no_more_time, None)
res1 = mma.search(root, 10, True)
res2 = mma.search(root, 10, False)
res3 = mma.search(root, 2, True)
res4 = mma.search(root, 2, False)

asssert(res1[0] == 13)
asssert(res2[0] == 10)
asssert(res3[0] == 6)
asssert(res4[0] == 5)


# chek min-max with time consideration
time = 5
mma2 = MiniMaxAlgorithm(utility, 'X', no_more_time2, None)
no_more_time2.time = 38
res5 = mma2.search(root, 10, True)
no_more_time2.time = 38
res6 = mma2.search(root, 10, False)












