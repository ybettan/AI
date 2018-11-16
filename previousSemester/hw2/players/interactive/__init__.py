import abstract
from Reversi.consts import *


class Player(abstract.AbstractPlayer):
    def __init__(self, setup_time, player_color, time_per_k_turns, k):
        abstract.AbstractPlayer.__init__(self, setup_time, player_color, time_per_k_turns, k)

    def get_move(self, game_state, possible_moves):
        print('Available moves:')
        for i, move in enumerate(possible_moves):
            print("({}) {}".format(i, str(move)))
        while True:
            # Trying to get the next move index from the user.
            idx = input('Enter the index of your move: ')
            try:
                idx = int(idx)
                if idx < 0 or idx >= len(possible_moves):
                    raise ValueError
                return possible_moves[idx]
            except ValueError:
                # Ignoring
                pass

    def __repr__(self):
        return '{} {}'.format(abstract.AbstractPlayer.__repr__(self), 'interactive')

# c:\python35\python run_game.py 3 3 3 y interactive interactive