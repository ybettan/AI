from heuristics import Heuristic

# TODO : Implement as explained in the instructions
class TSPCustomHeuristic(Heuristic):
    _distMat = None
    _junctionToMatIdx = None

    # TODO : You can add parameters if you need them
    def __init__(self, roads, initialState):
        super().__init__()

    # Estimate heuristically the minimal cost from the given state to the problem's goal
    def estimate(self, problem, state):
        raise NotImplementedError