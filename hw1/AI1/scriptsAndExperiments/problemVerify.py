##########################################
# No need to edit this file, only run it
# and copy the outputs.
##########################################

from consts import Consts
from ways import load_map_from_csv
from problems import BusProblem, BusState

# Read files
roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("TLV_5.in"))

# Hard copy bus state
current = BusState(466524, [(23695, 33320), (851288, 533396)], [(32056, 834603)], [(47521, 606430), (466524, 29249)])

# Print the state's details
print("Junction idx: #{}\nwaiting for bus: {}\norders on bus: {}\nfinished orders: {}\n".format(
    current.junctionIdx, current.waitingOrders, current.ordersOnBus, current.finishedOrders))

# Print its successors
print("###### Successors: ######")
for s in prob.expand(current):
    print("Junction idx: #{}\nwaiting for bus: {}\norders on bus: {}\nfinished orders: {}".format(
        s.junctionIdx, s.waitingOrders, s.ordersOnBus, s.finishedOrders))
    print("Is goal? {}\n".format(prob.isGoal(s)))