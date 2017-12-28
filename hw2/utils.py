"""Generic utility functions
"""
# from __future__ import print_function
from threading import Thread
from multiprocessing import Queue
import time
import copy
import sys
from Reversi.consts import *

INFINITY = float(6000)


class ExceededTimeError(RuntimeError):
    """Thrown when the given function exceeded its runtime.
    """
    pass


def function_wrapper(func, args, kwargs, result_queue):
    """Runs the given function and measures its runtime.

    :param func: The function to run.
    :param args: The function arguments as tuple.
    :param kwargs: The function kwargs as dict.
    :param result_queue: The inter-process queue to communicate with the parent.
    :return: A tuple: The function return value, and its runtime.
    """
    start = time.time()
    try:
        result = func(*args, **kwargs)
    except MemoryError as e:
        result_queue.put(e)
        return

    runtime = time.time() - start
    result_queue.put((result, runtime))


def run_with_limited_time(func, args, kwargs, time_limit):
    """Runs a function with time limit

    :param func: The function to run.
    :param args: The functions args, given as tuple.
    :param kwargs: The functions keywords, given as dict.
    :param time_limit: The time limit in seconds (can be float).
    :return: A tuple: The function's return value unchanged, and the running 
        time for the function.
    :raises PlayerExceededTimeError: If player exceeded its given time.
    """
    q = Queue()
    t = Thread(target=function_wrapper, args=(func, args, kwargs, q))
    t.start()

    # This is just for limiting the runtime of the other thread, so we stop 
    #   eventually.
    # It doesn't really measure the runtime.
    t.join(time_limit)

    if t.is_alive():
        raise ExceededTimeError

    q_get = q.get()
    if isinstance(q_get, MemoryError):
        raise q_get
    return q_get



class MiniMaxAlgorithm:

    def __init__(self, utility, my_color, no_more_time, selective_deepening):
        """Initialize a MiniMax algorithms without alpha-beta pruning.

        :param utility: The utility function. Should have state as parameter.
        :param my_color: The color of the player who runs this MiniMax search.
        :param no_more_time: A function that returns true if there is no more 
            time to run this search, or false if there is still time left.
        :param selective_deepening: A functions that gets the current state, and
            returns True when the algorithm should continue the search for the 
            minimax value recursivly from this state.
            optional
        """
        self.utility = utility
        self.my_color = my_color
        self.no_more_time = no_more_time
        self.selective_deepening = selective_deepening

    def search(self, state, depth, maximizing_player):
        """Start the MiniMax algorithm.

        :param state: The state to start from.
        :param depth: The maximum allowed depth for the algorithm.
        :param maximizing_player: Whether this is a max node (True) or a min 
            node (False).
        :return: A tuple: (The min max algorithm value, The move in case of 
            max node or None in min mode)
        """

        if self.no_more_time():
            raise ExceededTimeError

        possible_moves = state.get_possible_moves()

        if self.no_more_time():
            raise ExceededTimeError

        # if all moves where played - count result
        if len(possible_moves) == 0:
            my_u = 0
            op_u = 0
            for x in range(BOARD_COLS):
                for y in range(BOARD_ROWS):
                    if state.board[x][y] == self.my_color:
                        my_u += 1
                    if state.board[x][y] == OPPONENT_COLOR[self.my_color]:
                        op_u += 1
            return my_u - op_u, None

        # if we have reached max depth return huristic function
        if depth == 0:
            return self.utility(state), None

        best_move = None
        if maximizing_player:
            curr_max = -INFINITY

            for move in possible_moves:
                state_copy = copy.deepcopy(state)
                state_copy.perform_move(move[0], move[1])

                if self.no_more_time():
                    raise ExceededTimeError
                    curr_max = v
                    best_move = move
            if self.no_more_time():
                raise ExceededTimeError
            return curr_max, best_move
        else:
            curr_min = INFINITY
            for move in possible_moves:
                state_copy = copy.deepcopy(state)
                state_copy.perform_move(move[0], move[1])
                if self.no_more_time():
                    raise ExceededTimeError
            if self.no_more_time():
                raise ExceededTimeError
            return curr_min, None
        


class MiniMaxWithAlphaBetaPruning:

    def __init__(self, utility, my_color, no_more_time, selective_deepening):
        """Initialize a MiniMax algorithms with alpha-beta pruning.

        :param utility: The utility function. Should have state as parameter.
        :param my_color: The color of the player who runs this MiniMax search.
        :param no_more_time: A function that returns true if there is no more 
            time to run this search, or false if there is still time left.
        :param selective_deepening: A functions that gets the current state, and
            returns True when the algorithm should continue the search for the 
            minimax value recursivly from this state.
            optional
        """
        self.utility = utility
        self.my_color = my_color
        self.no_more_time = no_more_time
        self.selective_deepening = selective_deepening

    def search(self, state, depth, alpha, beta, maximizing_player):
        """Start the MiniMax algorithm.

        :param state: The state to start from.
        :param depth: The maximum allowed depth for the algorithm.
        :param alpha: The alpha of the alpha-beta pruning.
        :param beta: The beta of the alpha-beta pruning.
        :param maximizing_player: Whether this is a max node (True) or a min 
            node (False).
        :return: A tuple: (The alpha-beta algorithm value, The move in case of 
            max node or None in min mode)
        """

        if self.no_more_time():
            raise ExceededTimeError

        possible_moves = state.get_possible_moves()

        if self.no_more_time():
            raise ExceededTimeError

        # if all moves where played - count result
        if len(possible_moves) == 0:
            my_u = 0
            op_u = 0
            for x in range(BOARD_COLS):
                for y in range(BOARD_ROWS):
                    if state.board[x][y] == self.my_color:
                        my_u += 1
                    if state.board[x][y] == OPPONENT_COLOR[self.my_color]:
                        op_u += 1
            return my_u - op_u, None

        # if we have reached max depth return huristic function
        if depth == 0:
            return self.utility(state), None

        best_move = None
        if maximizing_player:
            curr_max = -INFINITY

            for move in possible_moves:
                state_copy = copy.deepcopy(state)
                state_copy.perform_move(move[0], move[1])

                if self.no_more_time():
                    raise ExceededTimeError
                v, _ = self.search(state_copy, depth-1, alpha, beta, \
                        not maximizing_player)
                if v > curr_max:
                    curr_max = v
                    best_move = move
                alpha = max(curr_max, alpha)
                if curr_max >= beta:
                    return INFINITY, None
            if self.no_more_time():
                raise ExceededTimeError
            return curr_max, best_move
        else:
            curr_min = INFINITY
            for move in possible_moves:
                state_copy = copy.deepcopy(state)
                state_copy.perform_move(move[0], move[1])
                if self.no_more_time():
                    raise ExceededTimeError
                v, _ = self.search(state_copy, depth-1, alpha, beta, \
                        not maximizing_player)
                curr_min = min(v, curr_min)
                beta = min(curr_min, beta)
                if curr_min <= alpha:
                    return -INFINITY,None
            if self.no_more_time():
                raise ExceededTimeError
            return curr_min, None
