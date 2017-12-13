import abstract
import random


class Player(abstract.AbstractPlayer):
    def __init__(self, setup_time, player_color, time_per_k_turns, k):
        abstract.AbstractPlayer.__init__(self, setup_time, player_color, time_per_k_turns, k)

    def get_move(self, game_state, possible_moves):
        idx = random.choice(range(len(possible_moves)))
        return possible_moves[idx]

    def __repr__(self):
        return '{} {}'.format(abstract.AbstractPlayer.__repr__(self), 'random')

# c:\python35\python run_game.py 3 3 3 y random_player random_player
