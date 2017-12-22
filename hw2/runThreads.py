from subprocess import call
import threading
import re
from matplotlib import pyplot as plt
import os
import shutil

players = [ \
           'simple_player', \
           'better_player', \
           'min_max_player', \
           'alpha_beta_player' \
          ]
times = ['2', '10', '50']

def callto(time, p1, p2):
    file_name = 'temp/' + p1 + p2+time+'.txt'

    file = open(file_name, 'w+')

    for _ in range(5):
        print('python3 run_game.py 2 {} 5 n {} {}'.format(time, p1, p2))
        call(['python3', 'run_game.py', '2', time, '5', 'n', p1, p2], stdout=file)

    file.close()


def run_threads():
    threads = []

    for p1 in players:
        for p2 in players:
            if p1 == p2:
                continue
            for time in times:
                t = threading.Thread(target=callto, args=[time, p1, p2])
                threads.append(t)
                t.start()

    for t in threads:
        t.join()



def main():

    if not os.path.isdir('temp'):
        os.mkdir('temp')

    run_threads()






if __name__ == '__main__':
    main()
