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
           'alpha_beta_player', \
           'competition_player' \
          ]
times = ['2', '10', '50']
iterations = ['1', '2', '3', '4', '5']


def callto(it):

    counter = 0
    for p1 in players:
        for p2 in players[players.index(p1)+1:]:
            for t in times:

                # p1 VS p2
                filename = "temp/{}_{}_time_{}_iteration_{}.txt".format(p1, p2, \
                        t, it)
                file = open(filename, 'w+')

                start = time.time()
                call(['python', 'run_game.py', '2', t, '5', 'n', p1, p2], stdout=file)
                end = time.time()
                print('python run_game.py 2 {} 5 n {} {}\t\t--> {} sec'.format( \
                        t, p1, p2, end-start))

                file.close()

                # p2 VS p1
                filename = "temp/{}_{}_time_{}_iteration_{}.txt".format(p2, p1, \
                        t, it)
                file = open(filename, 'w+')

                start = time.time()
                call(['python', 'run_game.py', '2', t, '5', 'n', p2, p1], stdout=file)
                end = time.time()
                print('python run_game.py 2 {} 5 n {} {}\t\t--> {} sec'.format( \
                        t, p2, p1, end-start))

                file.close()

                counter += 2

    assert(counter == 60)

    #counter = 0
    #for t in times:
    #    for it in iterations:

    #        # p1 VS p2
    #        filename = "temp/{}_{}_time_{}_iteration_{}.txt".format(p1, p2, \
    #                t, it)
    #        file = open(filename, 'w+')

    #        start = time.time()
    #        call(['python', 'run_game.py', '2', t, '5', 'n', p1, p2], stdout=file)
    #        end = time.time()
    #        print('python run_game.py 2 {} 5 n {} {}\t\t--> {} sec'.format( \
    #                t, p1, p2, end-start))

    #        file.close()

    #        # p2 VS p1
    #        filename = "temp/{}_{}_time_{}_iteration_{}.txt".format(p2, p1, \
    #                t, it)
    #        file = open(filename, 'w+')

    #        start = time.time()
    #        call(['python', 'run_game.py', '2', t, '5', 'n', p2, p1], stdout=file)
    #        end = time.time()
    #        print('python run_game.py 2 {} 5 n {} {}\t\t--> {} sec'.format( \
    #                t, p2, p1, end-start))

    #        file.close()

    #        counter += 2

    #assert(counter == 30)


def run_threads():
    threads = []

    for it in iterations:
        t = threading.Thread(target=callto, args=[it])
        threads.append(t)
        t.start()

    assert(len(threads) == 5)
    for t in threads:
        t.join()

    #for p1 in players:
    #    for p2 in players[players.index(p1)+1:]:
    #        if p1 == p2:
    #            continue
    #        t = threading.Thread(target=callto, args=[p1, p2])
    #        threads.append(t)
    #        t.start()
    #
    #assert(len(threads) == 6)
    #for t in threads:
    #    t.join()



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
