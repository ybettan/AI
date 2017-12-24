from subprocess import call
import threading
import re
from matplotlib import pyplot as plt
import os
import shutil
import time
import sys

#args = sys.argv[1:]
#DEBUG = False
#if args and args[0] == "--debug":
#    #if args[0] == '--debug'
#    DEBUG = True
#
#players = [ \
#           'simple_player', \
#           'better_player', \
#           'min_max_player', \
#           'alpha_beta_player' \
#          ]
#times = ['2', '10', '50']
#num_of_games = 5
#
#if DEBUG:
#    players = [ \
#               'min_max_player', \
#               'alpha_beta_player' \
#              ]
#    times = ['2']
#    num_of_games = 1

players = [ \
           'simple_player', \
           'better_player', \
           'min_max_player', \
           'alpha_beta_player' \
          ]
times = ['2', '10', '50']
iterations = ['1', '2', '3', '4', '5']

def callto(p1, p2):

    counter = 0
    for time in times:
        for it in iterations:

            # p1 VS p2
            filename = "temp/{}_{}_time_{}_iteration_{}.txt".format(p1, p2, \
                    time, it)
            file = open(filename, 'w+')

            print('python run_game.py 2 {} 5 n {} {}'.format(time, p1, p2))
            call(['python', 'run_game.py', '2', time, '5', 'n', p1, p2], stdout=file)
            #call(['python', 'run_game.py', '2', time, '5', 'n', p1, p2])

            file.close()

            # p2 VS p1
            filename = "temp/{}_{}_time_{}_iteration_{}.txt".format(p2, p1, \
                    time, it)
            file = open(filename, 'w+')

            print('python run_game.py 2 {} 5 n {} {}'.format(time, p2, p1))
            call(['python', 'run_game.py', '2', time, '5', 'n', p2, p1], stdout=file)
            #call(['python', 'run_game.py', '2', time, '5', 'n', p2, p1])

            file.close()

            counter += 2

    assert(counter == 30)

#def callto(time, p1, p2, iteration):
#    file_name = 'temp/' + p1 + "_" + p2 + "_time_" + time + "_iteration_" + \
#            iteration + '.txt'
#
#    file = open(file_name, 'w+')
#
#    print('python run_game.py 2 {} 5 n {} {}'.format(time, p1, p2))
#    call(['python', 'run_game.py', '2', time, '5', 'n', p1, p2], stdout=file)
#
#    file.close()


def run_threads():
    threads = []

    for p1 in players:
        for p2 in players[players.index(p1)+1:]:
            if p1 == p2:
                continue
            t = threading.Thread(target=callto, args=[p1, p2])
            threads.append(t)
            t.start()

    assert(len(threads) == 6)
    for t in threads:
        t.join()

#def run_threads():
#    threads = []
#
#    for p1 in players:
#        for p2 in players:
#            if p1 == p2:
#                continue
#            for time in times:
#                for i in range(num_of_games):
#                    t = threading.Thread(target=callto, \
#                            args=[time, p1, p2, str(i+1)])
#                    threads.append(t)
#                    t.start()
#
#    for t in threads:
#        t.join()



def main():

    begin = time.time()
    if not os.path.isdir('temp'):
        os.mkdir('temp')

    run_threads()
    end = time.time()
    print("==========================================")
    print("total time =", (end-begin)/60)
    print("==========================================")






if __name__ == '__main__':
    main()
