from . import Heuristic
from ways.tools import compute_distance

# Use the L2 aerial distance (in meters)
class L2DistanceHeuristic(Heuristic):
    def estimate(self, problem, state):

        coord1 = problem.target.coordinates
        coord2 = state.coordinates
        return compute_distance(coord1, coord2)

