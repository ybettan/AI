from heuristics import Heuristic
from ways.tools import compute_distance

# TODO : Implement as explained in the instructions
class TSPCustomHeuristic(Heuristic):
    _distMat = None
    _junctionToMatIdx = None

    # TODO : You can add parameters if you need them
    def __init__(self, roads, initialState):
        self.roads = roads
        super().__init__()

    # Estimate heuristically the minimal cost from the given state to the problem's goal
    def estimate(self, problem, state):
        #calc all the distances for the wating list drom sorce to target for each order
        distanc = [compute_distance(self.roads[v[0]].coordinates,self.roads[v[1]].coordinates) for v in state.waitingOrders]
        #return the max val or 0 if there is none
        if len(distanc) > 0:
            return max(distanc)
        return 0
