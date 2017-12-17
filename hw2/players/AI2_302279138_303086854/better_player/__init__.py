
#===============================================================================
# Imports
#===============================================================================

import abstract
from utils import INFINITY, run_with_limited_time, ExceededTimeError
from Reversi.consts import EM, OPPONENT_COLOR, BOARD_COLS, BOARD_ROWS
import time
import copy
from collections import defaultdict

#===============================================================================
# Player
#===============================================================================

class Player(abstract.AbstractPlayer):
    '''
    for now this class is an exact copy of players.simple_player.Player
    except the utils function (the heuristic)
    FIXME: remove the comment if i changed anything
    '''
    def __init__(self, setup_time, player_color, time_per_k_turns, k):
        abstract.AbstractPlayer.__init__(self, setup_time, player_color, time_per_k_turns, k)
        self.clock = time.time()

        # We are simply providing (remaining time / remaining turns) for each turn in round.
        # Taking a spare time of 0.05 seconds.
        self.turns_remaining_in_round = self.k
        self.time_remaining_in_round = self.time_per_k_turns
        self.time_for_current_move = self.time_remaining_in_round / self.turns_remaining_in_round - 0.05

    def get_move(self, game_state, possible_moves):
        self.clock = time.time()
        self.time_for_current_move = self.time_remaining_in_round / self.turns_remaining_in_round - 0.05
        if len(possible_moves) == 1:
            return possible_moves[0]

        best_move = possible_moves[0]
        next_state = copy.deepcopy(game_state)
        next_state.perform_move(best_move[0],best_move[1])
        # Choosing an arbitrary move
        # Get the best move according the utility function
        for move in possible_moves:
            new_state = copy.deepcopy(game_state)
            new_state.perform_move(move[0],move[1])
            if self.utility(new_state) > self.utility(next_state):
                next_state = new_state
                best_move = move

        if self.turns_remaining_in_round == 1:
            self.turns_remaining_in_round = self.k
            self.time_remaining_in_round = self.time_per_k_turns
        else:
            self.turns_remaining_in_round -= 1
            self.time_remaining_in_round -= (time.time() - self.clock)

        return best_move

#------------------------------------------------------------------------------

    def __end_utility(self, state):
        my_u = 0
        op_u = 0
        for x in range(BOARD_COLS):
            for y in range(BOARD_ROWS):
                if state.board[x][y] == self.color:
                    my_u += 1
                if state.board[x][y] == OPPONENT_COLOR[self.color]:
                    op_u += 1

        return my_u - op_u

    class NonEdgeIndex:
        pass

    def __is_stable(self, state, J, I):

        # a corner is always stable
        if (I == 0 or I == BOARD_ROWS) and (J == 0 or J == BOARD_COLS):
            return True
        
        elif I == 0 or I == BOARD_ROWS-1:
            res1 = True
            res2 = True
            for j in range(J): 
                if state.board[j][I] == OPPONENT_COLOR[self.color]:
                    res1 = False
                    break
            for j in range(J, BOARD_COLS): 
                if state.board[j][I] == OPPONENT_COLOR[self.color]:
                    res2 = False
                    break
            return res1 or res2

        elif J == 0 or J == BOARD_COLS-1:
            res1 = True
            res2 = True
            for i in range(I): 
                if state.board[J][i] == OPPONENT_COLOR[self.color]:
                    res1 = False
                    break
            for i in range(I, BOARD_ROWS): 
                if state.board[J][i] == OPPONENT_COLOR[self.color]:
                    res2 = False
                    break
            return res1 or res2

        # don't let this method be applied on a non-edge index
        else:
            raise NonEdgeIndex

    def __score_utility(self, state):
        CORNER_FAC = 100
        STABLE_EDGE_FAC = 20
        EDGE_FAC = 5
        INTER_FAC = 1

        my_u = 0
        op_u = 0
        for x in range(BOARD_COLS):
            for y in range(BOARD_ROWS):

                # is a corner
                if (x == 0 or x == BOARD_COLS-1) and (y == 0 or y == BOARD_ROWS-1):
                    if state.board[x][y] == self.color:
                        my_u += CORNER_FAC
                    elif state.board[x][y] == OPPONENT_COLOR[self.color]:
                        op_u += CORNER_FAC

                # is an edge 
                elif x == 0 or x == BOARD_COLS-1 or y == 0 or y == BOARD_ROWS-1:

                    # is stable
                    if self.__is_stable(state, x, y):
                        if state.board[x][y] == self.color:
                            my_u += STABLE_EDGE_FAC
                        elif state.board[x][y] == OPPONENT_COLOR[self.color]:
                            op_u += STABLE_EDGE_FAC

                    # is not stable
                    else:
                        if state.board[x][y] == self.color:
                            my_u += EDGE_FAC
                        elif state.board[x][y] == OPPONENT_COLOR[self.color]:
                            op_u -= EDGE_FAC

                # is internal
                else:
                        if state.board[x][y] == self.color:
                            my_u += INTER_FAC
                        elif state.board[x][y] == OPPONENT_COLOR[self.color]:
                            op_u -= INTER_FAC

        if my_u == 0:
            # I have no tools left
            return -INFINITY
        elif op_u == 0:
            # The opponent has no tools left
            return INFINITY
        else:
            return my_u - op_u


    def __mobility_utility(self, state):
        MOBILITY_FAC = 1

        # when this function is called the current player is already the 
        # opponent so we will change it to our player, check the value and 
        # return it as it was
        op_moves = len(state.get_possible_moves())
        state.curr_player = OPPONENT_COLOR[state.curr_player]
        my_moves = len(state.get_possible_moves())
        state.curr_player = OPPONENT_COLOR[state.curr_player]

        return (my_moves - op_moves) * MOBILITY_FAC

    # FIXME: can i remove? for now it is not used
    def __is_final_state(self, state):
        for x in range(BOARD_COLS):
            for y in range(BOARD_ROWS):
                if state.board[x][y] == EM:
                    return False
        return True

    def utility(self, state):
        if len(state.get_possible_moves()) == 0:
            return INFINITY if state.curr_player != self.color else -INFINITY

        # FIXME: can i remove?
        #if self.__is_final_state(state):
        #    return self.__end_utility(state)
            

        mobility_fac = 1
        score_fac = 1
        mobility_res = self.__mobility_utility(state) 
        score_res = self.__score_utility(state)
        #FIXME: give different whigts according to T 
        #print("mobility_res = {}".format(mobility_res))
        #print("score_res = {}\n".format(score_res))
        return mobility_res*mobility_fac + score_res*score_fac
#------------------------------------------------------------------------------

    def selective_deepening_criterion(self, state):
        # Simple player does not selectively deepen into certain nodes.
        return False

    def no_more_time(self):
        return (time.time() - self.clock) >= self.time_for_current_move

    def __repr__(self):
        return '{} {}'.format(abstract.AbstractPlayer.__repr__(self), 'better')

# c:\python35\python.exe run_game.py 3 3 3 y simple_player random_player
