from . import BusSolver
import abc

class GreedySolver(BusSolver):
    _scorer = None

    def __init__(self, roads, astar, scorer):
        super().__init__(roads, astar)

        self._scorer = scorer

    # Find the next state to develop
    @abc.abstractmethod
    def _getNextState(self, problem, currState):
        raise NotImplementedError

    # Find the picking order for our orders
    def _findPickingOrder(self, problem):
        pickingOrder = [problem.initialState.junctionIdx]

        currState = problem.initialState

        while not problem.isGoal(currState):
            currState = self._getNextState(problem, currState)

            pickingOrder.append(currState.junctionIdx)

        return pickingOrder