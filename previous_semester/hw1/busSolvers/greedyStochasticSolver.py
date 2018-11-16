from . import GreedySolver
import numpy as np
import heapq

class GreedyStochasticSolver(GreedySolver):
    _TEMPERATURE_DECAY_FACTOR = None
    _INITIAL_TEMPERATURE = None
    _N = None

    def __init__(self, roads, astar, scorer, initialTemperature, temperatureDecayFactor, topNumToConsider):
        super().__init__(roads, astar, scorer)

        self._INITIAL_TEMPERATURE = initialTemperature
        self._TEMPERATURE_DECAY_FACTOR = temperatureDecayFactor
        self._N = topNumToConsider

    def _getSuccessorsProbabilities(self, currState, successors):
        # Get the scores
        X = np.array([self._scorer.compute(currState, target) for target in successors])

        # Initialize an all-zeros vector for the distribution
        P = np.zeros((len(successors),))

        #select N min scores
        min_index = heapq.nsmallest(self._N, enumerate(X), key=lambda s: s[1])
        min_n_score = [x for _, x in min_index]
        alpha = min(min_n_score)
        sumy = sum(np.power(min_n_score/alpha, -1/self.T))
        for i, s in min_index:
            P[i] = ((s/alpha)**(-1/self.T))/sumy

        # Update the temperature
        self.T *= self._TEMPERATURE_DECAY_FACTOR

        return P

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))
        P = self._getSuccessorsProbabilities(currState, successors)

        nextIdx = np.random.choice(range(len(P)), 1, None, P)[0]
        return successors[nextIdx]

    # Override the base solve method to initialize the temperature
    def solve(self, initialState):
        self.T = self._INITIAL_TEMPERATURE
        return super().solve(initialState)