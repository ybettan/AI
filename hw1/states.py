import abc

class State(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

class MapState(State):
    junctionIdx = None

    def __init__(self, currentLoc, coordinates):
        super().__init__()
        self.junctionIdx = currentLoc
        self.coordinates = coordinates

    def __hash__(self):
        return hash(self.junctionIdx)

    def __eq__(self, other):
        return self.junctionIdx == other.junctionIdx

class BusState(State):
    junctionIdx = None
    waitingOrders = None
    ordersOnBus = None
    finishedOrders = None

    def __init__(self, currentLoc:int, waitingOrders:list, ordersOnBus:list, finishedOrders:list):
        super().__init__()
        self.junctionIdx = currentLoc
        self.waitingOrders = waitingOrders
        self.ordersOnBus = ordersOnBus
        self.finishedOrders = finishedOrders

    def __hash__(self):
        # Two lists are enough to know all three
        return hash((self.junctionIdx, tuple(set(self.waitingOrders)), tuple(set(self.ordersOnBus))))

    def __eq__(self, other):
        # Two lists are enough to know all three
        return ((self.junctionIdx, self.waitingOrders, self.ordersOnBus) ==
                (other.junctionIdx, other.waitingOrders, other.ordersOnBus))

    def isGoal(self):
        ''' 
        return true if the waitingOrders and the ordersOnBus are complete
        and the current junction is a order-target juction 
        '''
        return (not self.waitingOrders) and \
               (not self.ordersOnBus) and \
               (self.junctionIdx in [x[1] for x in self.finishedOrders])
