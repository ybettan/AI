from . import Heuristic
from ways.tools import compute_distance
import numpy as np

class NullHeuristic(Heuristic):
    def estimate(self, problem, state):
        return 0

