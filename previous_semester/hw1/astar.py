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
        parents = {source: None}  # The map of navigated nodes.

        # Save the g_score and f_score for the open nodes
        g_score = {source: 0}
        open_set = {source: self.heuristic.estimate(problem, problem.initialState)}

        developed = 0
        while open_set is not {}:
            #take the state with min h+g val in open
            c_state = self._getOpenStateWithLowest_f_score(open_set)
            #remove selected state from open
            open_set.pop(c_state)
            #add state to close
            closed_set.add(c_state)
            #check if we found the target
            if problem.isGoal(c_state):
                path = self._reconstructPath(parents, c_state)
                res = (path, g_score[c_state], self.heuristic.estimate(problem, source), developed)
                if self.shouldCache:
                    self._storeInCache(problem, res)
                return res
            developed += 1
            for n_state, potential_cost in problem.expandWithCosts(c_state, self.cost):
                #calc new g value for next state
                update_g = g_score[c_state] + potential_cost
                #check if next state in closr and need to move to open
                if n_state in closed_set:
                    if update_g < g_score[n_state]:
                        #update state values
                        self._setStateVals(n_state, c_state, parents, g_score, update_g)
                        #remove from close
                        closed_set.remove(n_state)
                        #update the h+g val to open
                        open_set[n_state] = self.heuristic.estimate(problem, n_state) + update_g
                #check if next state in open and need to update g
                elif n_state in open_set:
                    if update_g < g_score[n_state]:
                        #update the h+g val by removing old g and adding the new
                        open_set[n_state] = open_set[n_state] - g_score[n_state] + update_g
                        #update state values
                        self._setStateVals(n_state, c_state, parents, g_score, update_g)
                #if next state never visited
                else:
                    #update state values
                    self._setStateVals(n_state, c_state, parents, g_score, update_g)
                    #add to open
                    open_set[n_state] = self.heuristic.estimate(problem, n_state) + update_g
        return None

    def _getOpenStateWithLowest_f_score(self, open_set):
        return min(open_set.items(), key=lambda o: o[1])[0]

    def _setStateVals(self, state, parent, parents, g_score, g):
        parents[state] = parent
        g_score[state] = g


    # Reconstruct the path from a given goal by its parent and so on
    def _reconstructPath(self, parents, goal):
        path = []
        while goal is not None:
            path.insert(0, goal)
            goal = parents[goal]
        return path



