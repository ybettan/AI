from subprocess import call
import threading
import re
from matplotlib import pyplot as plt
import os
import shutil
import time
import sys


players = [ \
           'simple_player', \
           'better_player', \
           'min_max_player', \
           'alpha_beta_player' \
          ]
times = ['2', '10', '50']
iterations = ['1', '2', '3', '4', '5']


def callto(opponent):

    counter = 0
    for t in times:
        for it in iterations:

            # competition VS opponent
            filename = "competition/competition_player_VS_{}_time_{}_iteration_{}.txt" \
                    .format(opponent, t, it)
            file = open(filename, 'w+')

            start = time.time()
            call(['python', 'run_game.py', '2', t, '5', 'n', \
                    'competition_player', opponent], stdout=file)
            end = time.time()
            print('python run_game.py 2 {} 5 n competition_player {}\t--> {} sec'\
                    .format(t, opponent, end-start))

            file.close()

            # opponent VS competition 
            filename = "competition/{}_VS_competition_player_time_{}_iteration_{}.txt" \
                    .format(opponent, t, it)
            file = open(filename, 'w+')

            start = time.time()
            call(['python', 'run_game.py', '2', t, '5', 'n', \
                    opponent, 'competition_player'], stdout=file)
            end = time.time()
            print('python run_game.py 2 {} 5 n {} competition_player\t--> {} sec'\
                    .format(t, opponent, end-start))

            counter += 2

    assert(counter == 30)


def run_threads():
    threads = []

    for opponent in players:
        t = threading.Thread(target=callto, args=[opponent])
        threads.append(t)
        t.start()

    assert(len(threads) == 4)
    for t in threads:
        t.join()



def main():

    begin = time.time()

    if os.path.isdir('competition'):
        shutil.rmtree('competition')
    os.mkdir('competition')

    run_threads()
    end = time.time()
    print("==========================================")
    print("total time =", (end-begin)/60)
    print("==========================================")






if __name__ == '__main__':
    main()
