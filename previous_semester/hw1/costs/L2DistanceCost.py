from . import Cost
from ways.tools import compute_distance

class L2DistanceCost(Cost):
    roads = None

    def __init__(self, roads):
        self.roads = roads

    # Returns the L2 aerial distance between two states
    def compute(self, fromState, toState):
        return compute_distance(self.roads[fromState.junctionIdx].coordinates, self.roads[toState.junctionIdx].coordinates)
