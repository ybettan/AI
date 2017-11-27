from consts import Consts
from busSolvers import GreedyStochasticSolver
from heuristics import L2DistanceHeuristic, NullHeuristic, MSTHeuristic, TSPCustomHeuristic
from costs import L2DistanceCost
from astar import AStar
from ways import load_map_from_csv
from busSolvers import GreedyBestFirstSolver
from problems import BusProblem
from costs.actualDistanceCost import ActualDistanceCost


roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("TLV_5.in"))

mapAstar = AStar(L2DistanceHeuristic(), shouldCache=True)

############ Greedy solver ############

greedyPickingPath = GreedyBestFirstSolver(roads, mapAstar, L2DistanceCost(roads)).solve(prob)
print("Greedy result: {:.2f}km".format(greedyPickingPath.getDistance() / 1000))


############ Stochastic solver ############

scorer = L2DistanceCost(roads)
solver = GreedyStochasticSolver(roads, mapAstar, scorer,
                                Consts.STOCH_INITIAL_TEMPERATURE,
                                Consts.STOCH_TEMPERATURE_DECAY_FUNCTION,
                                Consts.STOCH_TOP_SCORES_TO_CONSIDER)

REPEATS = 200
results = [solver.solve(prob).getDistance() / 1000 for _ in range(REPEATS)]

print("Stochastic ({} repetitions): {}km".format(REPEATS, min(results)))


############ A* solver ############

# Run A* with the zero heuristic
busAstar = AStar(NullHeuristic(), cost=ActualDistanceCost(roads, mapAstar))
_,gBus,hVal,developed = busAstar.run(prob)
print("A* (null heuristic):\tg(G)={:.2f}km, h(I)={:.2f}km, developed: {} states".format(gBus/1000, hVal/1000, developed))

# TODO : Remove exit() and re-run
exit()

# Run A* with the custom heuristic
customH = TSPCustomHeuristic(roads, prob.initialState)
busAstar = AStar(customH, cost=ActualDistanceCost(roads, mapAstar))
_,gBus,hVal,developed = busAstar.run(prob)
print("A* (Custom heuristic):\tg(G)={:.2f}km, h(I)={:.2f}km, developed: {} states".format(gBus/1000, hVal/1000, developed))

# TODO : Remove exit() and re-run
exit()

# Run A* with the MST heuristic
tspH = MSTHeuristic(roads, prob.initialState, ActualDistanceCost(roads, mapAstar))
busAstar = AStar(tspH, cost=ActualDistanceCost(roads, mapAstar))
_,gBus,hVal,developed = busAstar.run(prob)
print("A* (MST heuristic):\tg(G)={:.2f}km, h(I)={:.2f}km, developed: {} states".format(gBus/1000, hVal/1000, developed))
