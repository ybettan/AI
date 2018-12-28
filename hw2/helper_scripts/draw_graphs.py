import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from prettytable import PrettyTable

ALL_DEPTHS = [0, 1, 2, 3, 4, 5]
NUM_LAYOUTS = 10

# Score(depth)
total_avg_score_reflex = [0, 0, 0, 0, 0, 0]
total_avg_score_better = [0, 0, 0, 0, 0, 0]
total_avg_score_minimax = [0, 0, 0, 0, 0, 0]
total_avg_score_alpha_beta = [0, 0, 0, 0, 0, 0]
total_avg_score_random_expectimax = [0, 0, 0, 0, 0, 0]

# TurnTime(depth)
avg_turn_time_score_reflex = [0, 0, 0, 0, 0, 0]
avg_turn_time_score_better = [0, 0, 0, 0, 0, 0]
avg_turn_time_score_minimax = [0, 0, 0, 0, 0, 0]
avg_turn_time_score_alpha_beta = [0, 0, 0, 0, 0, 0]
avg_turn_time_score_random_expectimax = [0, 0, 0, 0, 0, 0]



# read input from file
with open("experiments.csv", 'r') as f:
    for line in f:

        splited_line = line.split(",")
        assert len(splited_line) == 5

        agent = splited_line[0]
        depth = int(splited_line[1])
        layout = splited_line[2]
        avg_score = float(splited_line[3])
        avg_turn_time = float(splited_line[4])

        # reflex
        if agent == 'ReflexAgent':
            total_avg_score_reflex[depth] += avg_score
            avg_turn_time_score_reflex[depth] += avg_turn_time / NUM_LAYOUTS

        # better
        if agent == 'BetterAgent':
            total_avg_score_better[depth] += avg_score
            avg_turn_time_score_better[depth] += avg_turn_time / NUM_LAYOUTS

        # minimax
        if agent == 'MinMaxAgent':
            total_avg_score_minimax[depth] += avg_score
            avg_turn_time_score_minimax[depth] += avg_turn_time / NUM_LAYOUTS
            if layout == 'minimaxClassic':
                if depth == 4:
                    avg_score_minimaxClassic_depth_4_minimax = avg_score
            elif layout == 'trappedClassic':
                if depth == 4:
                    avg_score_trappedClassic_depth_4_minimax = avg_score

        # alpha_beta
        if agent == 'AlphaBetaAgent':
            total_avg_score_alpha_beta[depth] += avg_score
            avg_turn_time_score_alpha_beta[depth] += avg_turn_time / NUM_LAYOUTS
            if layout == 'minimaxClassic':
                if depth == 4:
                    avg_score_minimaxClassic_depth_4_alpha_beta = avg_score
            elif layout == 'trappedClassic':
                if depth == 4:
                    avg_score_trappedClassic_depth_4_alpha_beta = avg_score

        # random_expectimax
        if agent == 'RandomExpectimaxAgent':
            total_avg_score_random_expectimax[depth] += avg_score
            avg_turn_time_score_random_expectimax[depth] += avg_turn_time / NUM_LAYOUTS
            if layout == 'minimaxClassic':
                if depth == 4:
                    avg_score_minimaxClassic_depth_4_random_expectimax = avg_score
            elif layout == 'trappedClassic':
                if depth == 4:
                    avg_score_trappedClassic_depth_4_random_expectimax = avg_score



#==============================================================================
#                               Score(depth)
#==============================================================================

plt.plot(ALL_DEPTHS[1:2], total_avg_score_reflex[1:2], label='ReflexAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[1:2], total_avg_score_better[1:2], label='BetterAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[2:5], total_avg_score_minimax[2:5], label='MinMaxAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[2:5], total_avg_score_alpha_beta[2:5], label='AlphaBetaAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[2:5], total_avg_score_random_expectimax[2:5], \
        label='RandomExpectimaxAgent', linestyle="-", marker="o")

plt.xlabel("Depth")
plt.ylabel("Total Avg Score")
plt.title("TotalAvgScore(Depth)")
plt.legend()
plt.grid()
plt.show()


print("                                              Score Table")
t = PrettyTable(['Agent', 'depth=1', 'depth=2', 'depth=3', 'depth=4'])
t.add_row(['ReflexAgent', total_avg_score_reflex[1], '', '', ''])
t.add_row(['BetterAgent', total_avg_score_better[1], '', '', ''])
t.add_row(['MinMaxAgent', '', total_avg_score_minimax[2], \
        total_avg_score_minimax[3], total_avg_score_minimax[4]])
t.add_row(['AlphaBetaAgent', '', total_avg_score_alpha_beta[2], \
        total_avg_score_alpha_beta[3], total_avg_score_alpha_beta[4]])
t.add_row(['RandomExpectimaxAgent', '', total_avg_score_random_expectimax[2], \
        total_avg_score_random_expectimax[3], total_avg_score_random_expectimax[4]])
print (t)



#==============================================================================
#                               Time(depth)
#==============================================================================

plt.plot(ALL_DEPTHS[1:2], avg_turn_time_score_reflex[1:2], label='ReflexAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[1:2], avg_turn_time_score_better[1:2], label='BetterAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[2:5], avg_turn_time_score_minimax[2:5], label='MinMaxAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[2:5], avg_turn_time_score_alpha_beta[2:5], label='AlphaBetaAgent', \
        linestyle="-", marker="o")
plt.plot(ALL_DEPTHS[2:5], avg_turn_time_score_random_expectimax[2:5], \
        label='RandomExpectimaxAgent', linestyle="-", marker="o")

plt.xlabel("Depth")
plt.ylabel("Avg Turn Time Score [sec]")
plt.title("AvgTurnTime(Depth)")
plt.legend()
plt.grid()
plt.show()


print("                                              Time Table")
t = PrettyTable(['Agent', 'depth=1', 'depth=2', 'depth=3', 'depth=4'])
t.add_row(['ReflexAgent', avg_turn_time_score_reflex[1], '', '', ''])
t.add_row(['BetterAgent', avg_turn_time_score_better[1], '', '', ''])
t.add_row(['MinMaxAgent', '', avg_turn_time_score_minimax[2], \
        avg_turn_time_score_minimax[3], avg_turn_time_score_minimax[4]])
t.add_row(['AlphaBetaAgent', '', avg_turn_time_score_alpha_beta[2], \
        avg_turn_time_score_alpha_beta[3], avg_turn_time_score_alpha_beta[4]])
t.add_row(['RandomExpectimaxAgent', '', avg_turn_time_score_random_expectimax[2], \
        avg_turn_time_score_random_expectimax[3], avg_turn_time_score_random_expectimax[4]])
print (t)


#==============================================================================
#               Agents preformence on minimaxClassic layout
#==============================================================================

print("Agents preformence on minimaxClassic layout")
t = PrettyTable(['Agent', 'Score'])
t.add_row(['MinMaxAgent', avg_score_minimaxClassic_depth_4_minimax])
t.add_row(['AlphaBetaAgent', avg_score_minimaxClassic_depth_4_alpha_beta])
t.add_row(['RandomExpectimaxAgent', avg_score_minimaxClassic_depth_4_random_expectimax])
print (t)

#==============================================================================
#               Agents preformence on trappedClassic layout
#==============================================================================

print("Agents preformence on trappedClassic layout")
t = PrettyTable(['Agent', 'Score'])
t.add_row(['MinMaxAgent', avg_score_trappedClassic_depth_4_minimax])
t.add_row(['AlphaBetaAgent', avg_score_trappedClassic_depth_4_alpha_beta])
t.add_row(['RandomExpectimaxAgent', avg_score_trappedClassic_depth_4_random_expectimax])
print (t)

