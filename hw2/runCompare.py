from subprocess import call
import threading
import re
from matplotlib import pyplot as plt
import os
import shutil
import time
import sys


players = [ \
           'old_competition_player' \
          ]
times = ['2', '10', '50']

OLD = "old_competition_player"
NEW = "competition_player"


def callto(thread_num):

    counter = 0
    for t in times:
        for it in range(100):

            # competition VS old_competition
            filename = "compare_competition/{}_VS_{}_time_{}_iteration_{}_t{}.txt" \
                    .format(NEW, OLD, t, it, thread_num)
            file = open(filename, 'w+')

            start = time.time()
            call(['python', 'run_game.py', '2', t, '5', 'n', NEW, OLD], stdout=file)
            end = time.time()
            print('python run_game.py 2 {} 5 n {} {}\t--> {} sec'\
                    .format(t, NEW, OLD, end-start))

            file.close()

            # old_competition VS competition 
            filename = "compare_competition/{}_VS_{}_time_{}_iteration_{}_t{}.txt" \
                    .format(OLD, NEW, t, it, thread_num)
            file = open(filename, 'w+')

            start = time.time()
            call(['python', 'run_game.py', '2', t, '5', 'n', OLD, NEW], stdout=file)
            end = time.time()
            print('python run_game.py 2 {} 5 n {} {}\t--> {} sec'\
                    .format(t, OLD, NEW, end-start))

            file.close()

            counter += 2

    assert(counter == 600)


def run_threads():
    threads = []

    for opponent in players:
        for i in range(4):
            t = threading.Thread(target=callto, args=[i])
            threads.append(t)
            t.start()

    assert(len(threads) == 4)
    for t in threads:
        t.join()



def main():

    begin = time.time()

    if os.path.isdir('compare_competition'):
        shutil.rmtree('compare_competition')
    os.mkdir('compare_competition')

    run_threads()
    end = time.time()
    print("==========================================")
    print("total time =", (end-begin)/60)
    print("==========================================")






if __name__ == '__main__':
    main()
