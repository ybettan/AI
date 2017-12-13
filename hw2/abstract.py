"""Abstract classes. Your classes must inherit from these.
"""


class AbstractPlayer:
    """Your player must inherit from this class, and your player class name must be 'Player', as in the given examples.
Like this: 'class Player(abstract.AbstractPlayer):'
    """
    def __init__(self, setup_time, player_type, time_per_k_turns, k):
        """Player initialization.

        :param setup_time: Allowed setup time in seconds, float.
        :param player_color: A String representing this player's type.
        :param time_per_k_turns: Allowed move calculation time per k turns.
        :param k: The k above.
        """
        self.setup_time = setup_time
        self.color = player_type
        self.time_per_k_turns = time_per_k_turns
        self.k = k

    def get_move(self, game_state, possible_moves):
        """Chooses an action from the given actions.

        :param game_state: The current board state. It's always an amazons_board.amazonsBoard object.
        :param possible_moves: A list of possible moves.
        :return: The desired move in the list of possible moves.
        """
        raise NotImplementedError

    def __repr__(self):
        return self.color

