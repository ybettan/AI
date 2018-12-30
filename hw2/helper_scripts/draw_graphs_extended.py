import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


# Score(layout)
score_for_layouts_reflex_random_ghost = dict()
score_for_layouts_better_random_ghost = dict()
score_for_layouts_minimax_random_ghost = dict()
score_for_layouts_alpha_beta_random_ghost = dict()
score_for_layouts_random_expectimax_random_ghost = dict()
score_for_layouts_directional_expectimax_random_ghost = dict()
score_for_layouts_competition_random_ghost = dict()

score_for_layouts_reflex_directional_ghost = dict()
score_for_layouts_better_directional_ghost = dict()
score_for_layouts_minimax_directional_ghost = dict()
score_for_layouts_alpha_beta_directional_ghost = dict()
score_for_layouts_random_expectimax_directional_ghost = dict()
score_for_layouts_directional_expectimax_directional_ghost = dict()
score_for_layouts_competition_directional_ghost = dict()

# TurnTime(layout)
turn_time_for_layouts_reflex_random_ghost = dict()
turn_time_for_layouts_better_random_ghost = dict()
turn_time_for_layouts_minimax_random_ghost = dict()
turn_time_for_layouts_alpha_beta_random_ghost = dict()
turn_time_for_layouts_random_expectimax_random_ghost = dict()
turn_time_for_layouts_directional_expectimax_random_ghost = dict()
turn_time_for_layouts_competition_random_ghost = dict()

turn_time_for_layouts_reflex_directional_ghost = dict()
turn_time_for_layouts_better_directional_ghost = dict()
turn_time_for_layouts_minimax_directional_ghost = dict()
turn_time_for_layouts_alpha_beta_directional_ghost = dict()
turn_time_for_layouts_random_expectimax_directional_ghost = dict()
turn_time_for_layouts_directional_expectimax_directional_ghost = dict()
turn_time_for_layouts_competition_directional_ghost = dict()

# TotalTime(layout)
total_time_for_layouts_reflex_random_ghost = dict()
total_time_for_layouts_better_random_ghost = dict()
total_time_for_layouts_minimax_random_ghost = dict()
total_time_for_layouts_alpha_beta_random_ghost = dict()
total_time_for_layouts_random_expectimax_random_ghost = dict()
total_time_for_layouts_directional_expectimax_random_ghost = dict()
total_time_for_layouts_competition_random_ghost = dict()

total_time_for_layouts_reflex_directional_ghost = dict()
total_time_for_layouts_better_directional_ghost = dict()
total_time_for_layouts_minimax_directional_ghost = dict()
total_time_for_layouts_alpha_beta_directional_ghost = dict()
total_time_for_layouts_random_expectimax_directional_ghost = dict()
total_time_for_layouts_directional_expectimax_directional_ghost = dict()
total_time_for_layouts_competition_directional_ghost = dict()


# read input from file
with open("data_files/experiments_extended.csv", 'r') as f:
    for line in f:

        splited_line = line.split(",")
        assert len(splited_line) == 7

        agent = splited_line[0]
        depth = int(splited_line[1])
        ghost = splited_line[2]
        layout = splited_line[3]
        avg_score = float(splited_line[4])
        avg_turn_time = float(splited_line[5])
        avg_total_time = float(splited_line[6])

        # reflex
        if agent == 'ReflexAgent':
            if ghost == 'RandomGhost':
                score_for_layouts_reflex_random_ghost[layout] = avg_score
                turn_time_for_layouts_reflex_random_ghost[layout] = avg_turn_time
                total_time_for_layouts_reflex_random_ghost[layout] = avg_total_time
            else:
                score_for_layouts_reflex_directional_ghost[layout] = avg_score
                turn_time_for_layouts_reflex_directional_ghost[layout] = avg_turn_time
                total_time_for_layouts_reflex_directional_ghost[layout] = avg_total_time

        # better
        if agent == 'BetterAgent':
            if ghost == 'RandomGhost':
                score_for_layouts_better_random_ghost[layout] = avg_score
                turn_time_for_layouts_better_random_ghost[layout] = avg_turn_time
                total_time_for_layouts_better_random_ghost[layout] = avg_total_time
            else:
                score_for_layouts_better_directional_ghost[layout] = avg_score
                turn_time_for_layouts_better_directional_ghost[layout] = avg_turn_time
                total_time_for_layouts_better_directional_ghost[layout] = avg_total_time

        # minimax
        if agent == 'MinMaxAgent':
            if ghost == 'RandomGhost':
                score_for_layouts_minimax_random_ghost[layout] = avg_score
                turn_time_for_layouts_minimax_random_ghost[layout] = avg_turn_time
                total_time_for_layouts_minimax_random_ghost[layout] = avg_total_time
            else:
                score_for_layouts_minimax_directional_ghost[layout] = avg_score
                turn_time_for_layouts_minimax_directional_ghost[layout] = avg_turn_time
                total_time_for_layouts_minimax_directional_ghost[layout] = avg_total_time

        # alpha beta
        if agent == 'AlphaBetaAgent':
            if ghost == 'RandomGhost':
                score_for_layouts_alpha_beta_random_ghost[layout] = avg_score
                turn_time_for_layouts_alpha_beta_random_ghost[layout] = avg_turn_time
                total_time_for_layouts_alpha_beta_random_ghost[layout] = avg_total_time
            else:
                score_for_layouts_alpha_beta_directional_ghost[layout] = avg_score
                turn_time_for_layouts_alpha_beta_directional_ghost[layout] = avg_turn_time
                total_time_for_layouts_alpha_beta_directional_ghost[layout] = avg_total_time

        # random expectimax
        if agent == 'RandomExpectimaxAgent':
            if ghost == 'RandomGhost':
                score_for_layouts_random_expectimax_random_ghost[layout] = avg_score
                turn_time_for_layouts_random_expectimax_random_ghost[layout] = avg_turn_time
                total_time_for_layouts_random_expectimax_random_ghost[layout] = avg_total_time
            else:
                score_for_layouts_random_expectimax_directional_ghost[layout] = avg_score
                turn_time_for_layouts_random_expectimax_directional_ghost[layout] = avg_turn_time
                total_time_for_layouts_random_expectimax_directional_ghost[layout] = avg_total_time

        # directional expectimax
        if agent == 'DirectionalExpectimaxAgent':
            if ghost == 'RandomGhost':
                score_for_layouts_directional_expectimax_random_ghost[layout] = avg_score
                turn_time_for_layouts_directional_expectimax_random_ghost[layout] = avg_turn_time
                total_time_for_layouts_directional_expectimax_random_ghost[layout] = avg_total_time
            else:
                score_for_layouts_directional_expectimax_directional_ghost[layout] = avg_score
                turn_time_for_layouts_directional_expectimax_directional_ghost[layout] = avg_turn_time
                total_time_for_layouts_directional_expectimax_directional_ghost[layout] = avg_total_time

        # competition
        if agent == 'CompetitionAgent':
            if ghost == 'RandomGhost':
                score_for_layouts_competition_random_ghost[layout] = avg_score
                turn_time_for_layouts_competition_random_ghost[layout] = avg_turn_time
                total_time_for_layouts_competition_random_ghost[layout] = avg_total_time
            else:
                score_for_layouts_competition_directional_ghost[layout] = avg_score
                turn_time_for_layouts_competition_directional_ghost[layout] = avg_turn_time
                total_time_for_layouts_competition_directional_ghost[layout] = avg_total_time



#==============================================================================
#               Agents preformence on all layouts
#==============================================================================


#------------------------------------------------------------------------------
#                  Score(layout) sum on 2 ghost types
#------------------------------------------------------------------------------

score_for_layouts_reflex_sum_ghost = \
        score_for_layouts_reflex_random_ghost.copy()
for key in score_for_layouts_reflex_directional_ghost.keys():
    score_for_layouts_reflex_sum_ghost[key] += \
            score_for_layouts_reflex_directional_ghost[key]

score_for_layouts_better_sum_ghost = \
        score_for_layouts_better_random_ghost.copy()
for key in score_for_layouts_better_directional_ghost.keys():
    score_for_layouts_better_sum_ghost[key] += \
            score_for_layouts_better_directional_ghost[key]

score_for_layouts_alpha_beta_sum_ghost = \
        score_for_layouts_alpha_beta_random_ghost.copy()
for key in score_for_layouts_alpha_beta_directional_ghost.keys():
    score_for_layouts_alpha_beta_sum_ghost[key] += \
            score_for_layouts_alpha_beta_directional_ghost[key]

score_for_layouts_random_expectimax_sum_ghost = \
        score_for_layouts_random_expectimax_random_ghost.copy()
for key in score_for_layouts_random_expectimax_directional_ghost.keys():
    score_for_layouts_random_expectimax_sum_ghost[key] += \
            score_for_layouts_random_expectimax_directional_ghost[key]

score_for_layouts_directional_expectimax_sum_ghost = \
        score_for_layouts_directional_expectimax_random_ghost.copy()
for key in score_for_layouts_directional_expectimax_directional_ghost.keys():
    score_for_layouts_directional_expectimax_sum_ghost[key] += \
            score_for_layouts_directional_expectimax_directional_ghost[key]

score_for_layouts_competition_sum_ghost = \
        score_for_layouts_competition_random_ghost.copy()
for key in score_for_layouts_competition_directional_ghost.keys():
    score_for_layouts_competition_sum_ghost[key] += \
            score_for_layouts_competition_directional_ghost[key]

plt.plot(score_for_layouts_reflex_sum_ghost.keys(), \
        score_for_layouts_reflex_sum_ghost.values(), \
        label='ReflexAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_better_sum_ghost.keys(), \
        score_for_layouts_better_sum_ghost.values(), \
        label='BetterAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_alpha_beta_sum_ghost.keys(), \
        score_for_layouts_alpha_beta_sum_ghost.values(), \
        label='AlphaBetaAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_random_expectimax_sum_ghost.keys(), \
        score_for_layouts_random_expectimax_sum_ghost.values(), \
        label='RandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_directional_expectimax_sum_ghost.keys(), \
        score_for_layouts_directional_expectimax_sum_ghost.values(), \
        label='DirectionalandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_competition_sum_ghost.keys(), \
        score_for_layouts_competition_sum_ghost.values(), \
        label='CompetitionAgent', \
        linestyle="-", \
        marker="o")


plt.xlabel("Layout")
plt.ylabel("Avg Score")
plt.title("AvgScore(Layout), depth=4, RandomGhost+DirectionalGhost")
plt.legend()
plt.grid()
plt.show()


#------------------------------------------------------------------------------
#                      Score(layout) random ghost
#------------------------------------------------------------------------------

plt.plot(score_for_layouts_reflex_random_ghost.keys(), \
        score_for_layouts_reflex_random_ghost.values(), \
        label='ReflexAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_better_random_ghost.keys(), \
        score_for_layouts_better_random_ghost.values(), \
        label='BetterAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_alpha_beta_random_ghost.keys(), \
        score_for_layouts_alpha_beta_random_ghost.values(), \
        label='AlphaBetaAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_random_expectimax_random_ghost.keys(), \
        score_for_layouts_random_expectimax_random_ghost.values(), \
        label='RandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_directional_expectimax_random_ghost.keys(), \
        score_for_layouts_directional_expectimax_random_ghost.values(), \
        label='DirectionalandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_competition_random_ghost.keys(), \
        score_for_layouts_competition_random_ghost.values(), \
        label='CompetitionAgent', \
        linestyle="-", \
        marker="o")


plt.xlabel("Layout")
plt.ylabel("Avg Score")
plt.title("AvgScore(Layout), depth=4, RandomGhost")
plt.legend()
plt.grid()
plt.show()

#------------------------------------------------------------------------------
#                      Score(layout) directional ghost
#------------------------------------------------------------------------------

plt.plot(score_for_layouts_reflex_directional_ghost.keys(), \
        score_for_layouts_reflex_directional_ghost.values(), \
        label='ReflexAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_better_directional_ghost.keys(), \
        score_for_layouts_better_directional_ghost.values(), \
        label='BetterAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_alpha_beta_directional_ghost.keys(), \
        score_for_layouts_alpha_beta_directional_ghost.values(), \
        label='AlphaBetaAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_random_expectimax_directional_ghost.keys(), \
        score_for_layouts_random_expectimax_directional_ghost.values(), \
        label='RandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_directional_expectimax_directional_ghost.keys(), \
        score_for_layouts_directional_expectimax_directional_ghost.values(), \
        label='DirectionalandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(score_for_layouts_competition_directional_ghost.keys(), \
        score_for_layouts_competition_directional_ghost.values(), \
        label='CompetitionAgent', \
        linestyle="-", \
        marker="o")


plt.xlabel("Layout")
plt.ylabel("Avg Score")
plt.title("AvgScore(Layout), depth=4, DirectionalGhost")
plt.legend()
plt.grid()
plt.show()



#------------------------------------------------------------------------------
#                      TurnTime(layout) random ghost
#------------------------------------------------------------------------------

plt.plot(turn_time_for_layouts_reflex_random_ghost.keys(), \
        turn_time_for_layouts_reflex_random_ghost.values(), \
        label='ReflexAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_better_random_ghost.keys(), \
        turn_time_for_layouts_better_random_ghost.values(), \
        label='BetterAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_alpha_beta_random_ghost.keys(), \
        turn_time_for_layouts_alpha_beta_random_ghost.values(), \
        label='AlphaBetaAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_random_expectimax_random_ghost.keys(), \
        turn_time_for_layouts_random_expectimax_random_ghost.values(), \
        label='RandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_directional_expectimax_random_ghost.keys(), \
        turn_time_for_layouts_directional_expectimax_random_ghost.values(), \
        label='DirectionalandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_competition_random_ghost.keys(), \
        turn_time_for_layouts_competition_random_ghost.values(), \
        label='CompetitionAgent', \
        linestyle="-", \
        marker="o")


plt.xlabel("Layout")
plt.ylabel("Avg Turn Time")
plt.title("AvgTurnTime(Layout), depth=4, RandomGhost")
plt.legend()
plt.grid()
plt.show()

#------------------------------------------------------------------------------
#                      TurnTime(layout) directional ghost
#------------------------------------------------------------------------------

plt.plot(turn_time_for_layouts_reflex_directional_ghost.keys(), \
        turn_time_for_layouts_reflex_directional_ghost.values(), \
        label='ReflexAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_better_directional_ghost.keys(), \
        turn_time_for_layouts_better_directional_ghost.values(), \
        label='BetterAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_alpha_beta_directional_ghost.keys(), \
        turn_time_for_layouts_alpha_beta_directional_ghost.values(), \
        label='AlphaBetaAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_random_expectimax_directional_ghost.keys(), \
        turn_time_for_layouts_random_expectimax_directional_ghost.values(), \
        label='RandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_directional_expectimax_directional_ghost.keys(), \
        turn_time_for_layouts_directional_expectimax_directional_ghost.values(), \
        label='DirectionalandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(turn_time_for_layouts_competition_directional_ghost.keys(), \
        turn_time_for_layouts_competition_directional_ghost.values(), \
        label='CompetitionAgent', \
        linestyle="-", \
        marker="o")


plt.xlabel("Layout")
plt.ylabel("Avg Turn Time")
plt.title("AvgTurnTime(Layout), depth=4, DirectionalGhost")
plt.legend()
plt.grid()
plt.show()

#------------------------------------------------------------------------------
#                      TotlaTime(layout) random ghost
#------------------------------------------------------------------------------

plt.plot(total_time_for_layouts_reflex_random_ghost.keys(), \
        total_time_for_layouts_reflex_random_ghost.values(), \
        label='ReflexAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_better_random_ghost.keys(), \
        total_time_for_layouts_better_random_ghost.values(), \
        label='BetterAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_alpha_beta_random_ghost.keys(), \
        total_time_for_layouts_alpha_beta_random_ghost.values(), \
        label='AlphaBetaAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_random_expectimax_random_ghost.keys(), \
        total_time_for_layouts_random_expectimax_random_ghost.values(), \
        label='RandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_directional_expectimax_random_ghost.keys(), \
        total_time_for_layouts_directional_expectimax_random_ghost.values(), \
        label='DirectionalandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_competition_random_ghost.keys(), \
        total_time_for_layouts_competition_random_ghost.values(), \
        label='CompetitionAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_competition_random_ghost.keys(), \
        [30] * len(total_time_for_layouts_competition_random_ghost.keys()), \
        label='Restriction', \
        color='black', \
        linestyle="dashed")


plt.xlabel("Layout")
plt.ylabel("Avg Total Time")
plt.title("AvgTotalTime(Layout), depth=4, RandomGhost")
plt.legend()
plt.grid()
plt.show()

#------------------------------------------------------------------------------
#                      TotlaTime(layout) directional ghost
#------------------------------------------------------------------------------

plt.plot(total_time_for_layouts_reflex_directional_ghost.keys(), \
        total_time_for_layouts_reflex_directional_ghost.values(), \
        label='ReflexAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_better_directional_ghost.keys(), \
        total_time_for_layouts_better_directional_ghost.values(), \
        label='BetterAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_alpha_beta_directional_ghost.keys(), \
        total_time_for_layouts_alpha_beta_directional_ghost.values(), \
        label='AlphaBetaAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_random_expectimax_directional_ghost.keys(), \
        total_time_for_layouts_random_expectimax_directional_ghost.values(), \
        label='RandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_directional_expectimax_directional_ghost.keys(), \
        total_time_for_layouts_directional_expectimax_directional_ghost.values(), \
        label='DirectionalandomExpectimaxAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_competition_directional_ghost.keys(), \
        total_time_for_layouts_competition_directional_ghost.values(), \
        label='CompetitionAgent', \
        linestyle="-", \
        marker="o")
plt.plot(total_time_for_layouts_competition_directional_ghost.keys(), \
        [30] * len(total_time_for_layouts_competition_directional_ghost.keys()), \
        label='Restriction', \
        color='black', \
        linestyle="dashed")


plt.xlabel("Layout")
plt.ylabel("Avg Total Time")
plt.title("AvgTotalTime(Layout), depth=4, DirectionalGhost")
plt.legend()
plt.grid()
plt.show()



