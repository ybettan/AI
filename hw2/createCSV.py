import sys
import subprocess
#import copy
#from Reversi.consts import TIE

DEBUG = False

TO_NAME = {"simple_player":"simple_player", \
           "AI2_302279138_303086854.better_player":"better_player", \
           "AI2_302279138_303086854.min_max_player":"min_max_player", \
           "AI2_302279138_303086854.alpha_beta_player":"alpha_beta_player" \
          }

T = [2, 10, 50]
if DEBUG:
    iterations = 1
    players = [ \
               "simple_player", \
               "AI2_302279138_303086854.better_player" \
              ]
else:
    iterations = 5
    players = [ \
               "simple_player", \
               "AI2_302279138_303086854.better_player", \
               "AI2_302279138_303086854.min_max_player", \
               "AI2_302279138_303086854.alpha_beta_player" \
              ]

if DEBUG:
    f = open("experiments_debug.csv", 'w')
else:
    f = open("experiments.csv", 'w')

counter = 0
for t in T:
    t_per_turn = t/5
    for player_x in players:
        for player_o in players[players.index(player_x)+1:]:
            for i in range(iterations):
                counter += 2

                # first game
                res = str(subprocess.check_output(["python", "run_game.py", \
                        str(t_per_turn), str(t), "5", "n", player_x, player_o]))

                if res.find("X") != -1:
                    player_x_score = "1"
                    player_o_score = "0"
                elif res.find("O") != -1:
                    player_x_score = "0"
                    player_o_score = "1"
                elif res.find("tie") != -1:
                    player_x_score = "0.5"
                    player_o_score = "0.5"
                else:
                    print("canot determine game resulr")
                    sys.exit(1)

                line = "{},{},{},{},{}".format(TO_NAME[player_x], \
                        TO_NAME[player_o], t, player_x_score, player_o_score) 
                f.write(line + "\n")

                # second game
                res = str(subprocess.check_output(["python", "run_game.py", \
                        str(t_per_turn), str(t), "5", "n", player_o, player_x]))

                if res.find("X") != -1:
                    player_o_score = "1"
                    player_x_score = "0"
                elif res.find("O") != -1:
                    player_o_score = "0"
                    player_x_score = "1"
                elif res.find("tie") != -1:
                    player_x_score = "0.5"
                    player_o_score = "0.5"
                else:
                    print("canot determine game resulr")
                    sys.exit(1)

                line = "{},{},{},{},{}".format(TO_NAME[player_o], \
                        TO_NAME[player_x], t, player_o_score, player_x_score) 
                f.write(line + "\n")

                
if DEBUG:
    assert(counter == 6)
else:
    assert(counter == 180)

f.close

