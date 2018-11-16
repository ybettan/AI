from consts import Consts
from astar import AStar
from ways import load_map_from_csv
from busSolvers import GreedyBestFirstSolver, GreedyStochasticSolver
from problems import BusProblem
from costs import L2DistanceCost
from heuristics import L2DistanceHeuristic
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

REPEATS = 150

# Load the files
roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("HAIFA_100.in"))

mapAstar = AStar(L2DistanceHeuristic(), shouldCache=True)

scorer = L2DistanceCost(roads)

# Run the greedy solver
pickingPath = GreedyBestFirstSolver(roads, mapAstar, scorer).solve(prob)
greedyDistance = pickingPath.getDistance() / 1000
print("Greedy solution: {:.2f}km".format(greedyDistance))

# Run the stochastic solver #REPATS times
solver = GreedyStochasticSolver(roads, mapAstar, scorer,
                                Consts.STOCH_INITIAL_TEMPERATURE,
                                Consts.STOCH_TEMPERATURE_DECAY_FUNCTION,
                                Consts.STOCH_TOP_SCORES_TO_CONSIDER)
results = np.zeros((REPEATS,))
print("Stochastic repeats:")
for i in range(REPEATS):
    print("{}..".format(i+1), end=" ", flush=True)
    results[i] = solver.solve(prob).getDistance() / 1000

print("\nDone!")

x_line = [x+1 for x in range(REPEATS)]

Y_greedy = [greedyDistance for x in range(REPEATS)]
plt.plot(x_line, Y_greedy, label='Greedy')

y_results = [min(results[0:idx+1]) for idx in range(REPEATS)]
plt.plot(x_line, y_results, label='Stochastic')

plt.legend(loc='upper right')
plt.xlabel('Number Of Repeats')
plt.ylabel('Distance')
plt.show()

resAvg = sum(results)/REPEATS
vari = np.sqrt((1/REPEATS)*sum([(res-resAvg)**2 for res in results]))
_, p_value = stats.ttest_ind(results, Y_greedy)

print("average: {} ".format(resAvg))
print("variance: {} ".format(vari))
print("p-value: {} ".format(p_value))
