import numpy as np
import sys

class AStar:
    cost = None
    heuristic = None
    _cache = None
    shouldCache = None

    def __init__(self, heuristic, cost=None, shouldCache=False):
        self.heuristic = heuristic
        self.shouldCache = shouldCache
        self.cost = cost

        # Handles the cache. No reason to change this code.
        if self.shouldCache:
            self._cache = {}

    # Get's from the cache. No reason to change this code.
    def _getFromCache(self, problem):
        if self.shouldCache:
            return self._cache.get(problem)

        return None

    # Get's from the cache. No reason to change this code.
    def _storeInCache(self, problem, value):
        if not self.shouldCache:
            return

        self._cache[problem] = value

    # Run A*
    def run(self, problem):
        # Check if we already have this problem in the cache.
        # No reason to change this code.
        source = problem.initialState
        if self.shouldCache:
            res = self._getFromCache(problem)

            if res is not None:
                return res

        # Initializes the required sets
        closed_set = set()  # The set of nodes already evaluated.
        parents = {}  # The map of navigated nodes.

        # Save the g_score and f_score for the open nodes
        g_score = {source: 0}
        open_set = {source: self.heuristic.estimate(problem, problem.initialState)}

        developed = 0

        # TODO : Implement astar.
        # Tips:
        # - To get the successor states of a state with their costs, use: problem.expandWithCosts(state, self.cost)
        # - You should break your code into methods (two such stubs are written below)
        # - Don't forget to cache your result between returning it - TODO

        # TODO : VERY IMPORTANT: must return a tuple of (path, g_score(goal), h(I), developed)
        return ([], -1, -1, developed)

    def _getOpenStateWithLowest_f_score(self, open_set):
        # TODO : Implement
        raise NotImplementedError

    # Reconstruct the path from a given goal by its parent and so on
    def _reconstructPath(self, parents, goal):
        # TODO : Implement
        raise NotImplementedError
