import re
import copy

DEBUG = True

scores = { \
          "simple":0, \
          "better":0, \
          "min_max":0, \
          "alpha_beta":0 \
         }

all_scores = { \
              2:copy.deepcopy(scores), \
              10:copy.deepcopy(scores), \
              50:copy.deepcopy(scores) \
             } 

if DEBUG:
    f = open("experiments_debug.csv", 'r')
else:
    f = open("experiments.csv", 'r')

T = [2, 10, 50]
for t in T:
    
    #f = open("experiments.csv", 'r')
    for line in f:
        match = re.search(r'(.*)_player,(.*)_player,\d+,(\d.*\d*),(\d.*\d*)',line)

        player_x_name = match.group(1)
        player_o_name = match.group(2)
        player_x_score = float(match.group(3))
        player_o_score = float(match.group(4))

        all_scores[t][player_x_name] += player_x_score
        all_scores[t][player_o_name] += player_o_score
        
f.close()

f = open("graphs.csv", 'w')

f.write("{},{},{},{},{}\n".format("t", "simple_player", "better_player", \
        "min_max_player", "alpha_beta_player"))
f.write("{},{},{},{},{}\n".format(2, all_scores[2]["simple"], \
        all_scores[2]["better"], all_scores[2]["min_max"], \
        all_scores[2]["alpha_beta"]))
f.write("{},{},{},{},{}\n".format(10, all_scores[10]["simple"], \
        all_scores[10]["better"], all_scores[10]["min_max"], \
        all_scores[10]["alpha_beta"]))
f.write("{},{},{},{},{}\n".format(50, all_scores[50]["simple"], \
        all_scores[50]["better"], all_scores[50]["min_max"], \
        all_scores[50]["alpha_beta"]))

f.close()
