import abc
from problems import MapProblem

class BusSolver(metaclass=abc.ABCMeta):
    roads = None
    astar = None

    def __init__(self, roads, astar):
        self.roads = roads
        self.astar = astar

    # Finds the picking order to pick all orders
    @abc.abstractmethod
    def _findPickingOrder(self, problem):
        raise NotImplementedError

    # Solve the bus problem. Return the picking path
    def solve(self, problem):
        pickingOrder = self._findPickingOrder(problem)

        pickingPath = [problem.initialState.junctionIdx]

        # Build the picking path itself using A* between every two locations in the picking order
        for source, target in zip(pickingOrder[:-1], pickingOrder[1:]):
            mapSubProblem = MapProblem(self.roads, source, target)
            statesSubpath = self.astar.run(mapSubProblem)[0]

            delta = [s.junctionIdx for s in statesSubpath[1:]]

            pickingPath = pickingPath + delta

        from path import Path
        return Path(self.roads, pickingPath)