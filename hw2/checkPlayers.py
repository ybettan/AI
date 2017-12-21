import sys
import subprocess
import copy
from Reversi.consts import TIE

def main():

    full_players = sys.argv[1:]
    if len(full_players) != 2:
        print("usage: python {} <player1> <player2>".format(sys.argv[0]))
        sys.exit(1)

    # don't let the same agent play against itself
    if full_players[0] == full_players[1]:
        print("don't use the same agent twice")
        sys.exit(1)

    # WARNING:
    #if full_players[0] != "simple_player":
    #    if input("\nWARRNING: first player isn't 'simple_player', would you like \
#to continue ? [y/n] ") != 'y':
    #        sys.exit(1)

    # cut the AI2_id1_id2 part of the string
    players = copy.deepcopy(full_players)
    for i in range(2):
        if players[i].find("AI2") != -1:
            players[i] = players[i][24:]
        if players[i].find("_player") != -1:
            players[i] = players[i][:len(players[i]) - 7]
            
    #print("full_players[0] = {}\nfull_players[1] = {}".format(full_players[0], full_players[1]))
    #print("players[0] = {}\nplayers[1] = {}".format(players[0], players[1]))
    res = {players[0]:0, players[1]:0, TIE:0}
    for i in range(1):
        tmp = str(subprocess.check_output(["python", "run_game.py", "2", "10", "5", \
                                  "n", full_players[0], full_players[1] ]))

        if tmp.find("The game ended in a tie!") != -1:
            res[TIE] += 1
            continue

        winner = tmp.split(" ")[4].split("\\")[0]
        #print("winner is {}".format(winner))
        if players[0] == winner:
            res[players[0]] += 1
        elif players[1] == winner:
            res[players[1]] += 1
        else:
            print("ERROR : the winner cannot be '{}'".format(winner))
            print("tmp = '{}'".format(tmp))
            sys.exit(1)

    player0_wins = int(res[players[0]]/(res[players[0]]+res[players[1]]+res[TIE])*100)
    player1_wins = int(res[players[1]]/(res[players[0]]+res[players[1]]+res[TIE])*100)
    ties = int(res[TIE]/(res[players[0]]+res[players[1]]+res[TIE])*100)
    print("\n{} won {}% of the games".format(players[0], player0_wins))
    print("{} won {}% of the games".format(players[1], player1_wins))
    print("there is {}% of ties".format(ties))



     







if __name__ == '__main__':
    main()

