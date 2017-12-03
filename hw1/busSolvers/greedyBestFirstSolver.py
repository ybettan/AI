from . import GreedySolver
import numpy as np

class GreedyBestFirstSolver(GreedySolver):
    def __init__(self, roads, astar, scorer):
        super().__init__(roads, astar, scorer)

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))

        return min(successors, key=lambda s: self._scorer.compute(currState, s))
