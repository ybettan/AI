from heuristics import Heuristic
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial.distance import pdist, squareform
from ways.tools import compute_distance

# An MST is a lower bound for a TSP result
class MSTHeuristic(Heuristic):
    _distMat = None
    _junctionToMatIdx = None

    def __init__(self, roads, initialState, metric):
        super().__init__()
        locations = [initialState.junctionIdx] + [o[0] for o in initialState.waitingOrders] + \
                    [o[1] for o in initialState.waitingOrders]

        self._initDistanceMatrix(roads, locations, metric)

    def _initDistanceMatrix(self, roads, locations, metric):
        junctionIds = list(set(locations))

        self._junctionToMatIdx = {j: i for i,j in enumerate(junctionIds)}

        pointsMat = np.zeros((2, len(junctionIds)))

        pointsMat[0, :] = [roads[p].lat for p in junctionIds]
        pointsMat[1, :] = [roads[p].lon for p in junctionIds]

        print("MST heuristic is computing required metadata...")

        self._distMat = np.zeros((len(junctionIds), len(junctionIds)))
        from states import MapState
        for i in range(len(junctionIds)):
            for j in range(len(junctionIds)):
                if i == j:
                    continue

                self._distMat[i,j] = \
                    metric.compute(MapState(junctionIds[i], roads[junctionIds[i]].coordinates),
                                 MapState(junctionIds[j], roads[junctionIds[j]].coordinates))

    def estimate(self, problem, state):
        # Get indices of active orders in the given state
        if len(state.waitingOrders) + len(state.ordersOnBus) <= 1:
            return 0

        activeLocations = set(np.hstack([state.junctionIdx] +
                                        [[o[0],o[1]] for o in state.waitingOrders] +
                                        [o[1] for o in state.ordersOnBus]))

        indices = np.array([self._junctionToMatIdx[o] for o in activeLocations])
        row_idx = indices
        col_idx = indices

        # Compute MST, which is the shortest possible weight of a path between all vertices
        mst = minimum_spanning_tree(self._distMat[row_idx[:, None], col_idx], overwrite=False)

        return np.sum(mst)