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



def create_fianl_reult_and_csv_file():
    final_result = {player: {t: 0 for t in times} for player in players}
    experiments = open('experiments.csv', 'w')
    for p1 in players:
        for p2 in players:
            if p1 == p2:
                continue
            for time in times:
                file_name = 'temp/' + p1 + p2+time+'.txt'
                with open(file_name, 'r') as file:
                    for line in file.readlines():
                        print('line is:{}'.format(line))
                        winner = re.split('\n', line)[0].split(' ')[-1]
                        winner += "_player"
                        p1_score = '0.5'
                        p2_score = '0.5'
                        if winner == p1:
                            p1_score = '1'
                            p2_score = '0'
                        elif winner == p2:
                            p1_score = '0'
                            p2_score = '1'
                        final_result[p1][time] += float(p1_score)
                        final_result[p2][time] += float(p2_score)
                        line_to_print = p1 + ',' + p2 + ',' + time + ',' + \
                                p1_score + ',' + p2_score + '\n'
                        experiments.write(line_to_print)

    experiments.close()
    return final_result


def create_graph_and_table(final_result):
    table = open('table.csv', 'w')
    headers = 't = 2, t = 10, t = 50, player_name\n'
    table.write(headers)
    plt.figure()
    x = [int(t) for t in times]
    plt.title('Scores as a function of t')
    for player in players:
        time_to_point = final_result[player]
        y = [time_to_point[t] for t in times]
        line = ''
        for point in y:
            line += str(point) + ','
        line += player + '\n'
        table.write(line)
        plt.plot(x, y, '.-', label=player)
    table.close()
    plt.legend()
    plt.show()


def main():

    final_result = create_fianl_reult_and_csv_file()
    create_graph_and_table(final_result)

    #if os.path.isdir('temp'):
    #    shutil.rmtree('temp')


if __name__ == '__main__':
    main()
