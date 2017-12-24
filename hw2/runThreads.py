from subprocess import call
import threading
import re
from matplotlib import pyplot as plt
import os
import shutil
import time
import sys

args = sys.argv[1:]
DEBUG = False
if args and args[0] == "--debug":
    #if args[0] == '--debug'
    DEBUG = True

players = [ \
           'simple_player', \
           'better_player', \
           'min_max_player', \
           'alpha_beta_player' \
          ]
times = ['2', '10', '50']
num_of_games = 5

if DEBUG:
    players = [ \
               'min_max_player', \
               'alpha_beta_player' \
              ]
    times = ['2']
    num_of_games = 1

print(players, times, num_of_games)

def callto(time, p1, p2):
    file_name = 'temp/' + p1 + p2 + time + '.txt'

    file = open(file_name, 'w+')

    print('python run_game.py 2 {} 5 n {} {}'.format(time, p1, p2))
    call(['python', 'run_game.py', '2', time, '5', 'n', p1, p2], stdout=file)

    file.close()


def run_threads():
    threads = []

    for p1 in players:
        for p2 in players:
            if p1 == p2:
                continue
            for time in times:
                for _ in range(num_of_games):
                    t = threading.Thread(target=callto, args=[time, p1, p2])
                    threads.append(t)
                    t.start()

    for t in threads:
        t.join()



def main():

    begin = time.time()
    if not os.path.isdir('temp'):
        os.mkdir('temp')

    run_threads()
    end = time.time()
    print("==========================================")
    print("total time =", end-begin/60)
    print("==========================================")






if __name__ == '__main__':
    main()
