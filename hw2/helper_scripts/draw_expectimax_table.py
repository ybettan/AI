import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from prettytable import PrettyTable



# read input from file
with open("experiments_random_vs_directional_expectimax.csv", 'r') as f:
    for line in f:

        splited_line = line.split(",")
        assert len(splited_line) == 4

        agent = splited_line[0]
        ghost = splited_line[1]
        avg_score = float(splited_line[2])
        avg_turn_time = float(splited_line[3])

        print("{}, {}, {}, {}".format(agent, ghost, avg_score, avg_turn_time))

        if agent == 'RandomExpectimaxAgent':
            if ghost == 'RandomGhost':
                total_avg_score_random_random = avg_score
                avg_turn_time_random_random = avg_turn_time
            elif ghost == 'DirectionalGhost':
                total_avg_score_random_directional = avg_score
                avg_turn_time_random_directional = avg_turn_time
            else:
                assert 1 == 0

        elif agent == 'DirectionalExpectimaxAgent':
            if ghost == 'RandomGhost':
                total_avg_score_directional_random = avg_score
                avg_turn_time_directional_random = avg_turn_time
            elif ghost == 'DirectionalGhost':
                total_avg_score_directional_directional = avg_score
                avg_turn_time_directional_directional = avg_turn_time
            else:
                assert 1 == 0



print("                                              Expectimax Table")
t = PrettyTable(['agent - result_type', 'RandomGhost', 'DirectionalGhost'])
t.add_row(['RandomExpectimaxAgent - avg_score', total_avg_score_random_random, \
        total_avg_score_random_directional])
t.add_row(['DirectionalExpectimaxAgent - avg_score', total_avg_score_directional_random, \
        total_avg_score_directional_directional])
t.add_row(['RandomExpectimaxAgent - avg_turn_time', avg_turn_time_random_random, \
        avg_turn_time_random_directional])
t.add_row(['DirectionalExpectimaxAgent - avg_turn_time', avg_turn_time_directional_random, \
        avg_turn_time_directional_directional])
print(t)




