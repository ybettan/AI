##########################################
# No need to edit this file, only run it
# and copy the outputs.
##########################################
from consts import Consts
from ways import load_map_from_csv
from problems import BusProblem, MapProblem
from matplotlib import pyplot as plt
from ways.draw import plotPath, plotOrders
from astar import AStar
from heuristics import L2DistanceHeuristic
from path import Path

# Read files
roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("TLV_5.in"))

mapAstar = AStar(L2DistanceHeuristic(), shouldCache=True)

# Plot the orders
plotOrders(roads, prob.orders)
plt.title("Showing orders. Click to show path")
plt.title("Showing orders. Click to show path")
plt.show(block=False)
plt.waitforbuttonpress()

colors = ['red', 'blue', 'green', 'orange', 'grey']

plt.title("Showing paths")

totalDistance = 0
# Plot each order at a time
for i,order in enumerate(prob.orders):
    # Create a sub-problem to solve with A* (getting the optimal path for each order separately)
    subProblem = MapProblem(roads, order[0], order[1])

    subPath, distance, _, _ = mapAstar.run(subProblem)

    print("Shortest distance for order from #{} to #{}: {:.2f}km".format(order[0], order[1], distance / 1000))
    totalDistance += distance

    # Plot the path
    plotPath(Path(roads, [s.junctionIdx for s in subPath]), color=colors[i])
    plt.show(block=False)
    plt.waitforbuttonpress()

print("Total distance: {:.2f}km".format(totalDistance / 1000    ))

