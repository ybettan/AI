#targets:
#    * alpha beta
#    * remember extremum son in iterative depening for alpha beta


#===============================================================================
# Imports
#===============================================================================

import re
import abstract
from utils import INFINITY, run_with_limited_time, ExceededTimeError, \
        MiniMaxAlgorithm, MiniMaxWithAlphaBetaPruning
from Reversi.consts import EM, OPPONENT_COLOR, BOARD_COLS, BOARD_ROWS, O_PLAYER
from Reversi.board import GameState
import time
import copy
from collections import defaultdict
import sys

# for the opening book
TO_LETTER = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', \
             '8':'h'}
TO_DIGIT = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', \
            'h':'8'}
REVERSE_LETTER = {'a':'h', 'b':'g', 'c':'f', 'd':'e', 'e':'d', \
                  'f':'c', 'g':'b', 'h':'a'}

#===============================================================================
# Player
#===============================================================================

class ImpossibleBoardTransform(Exception):
    pass

class NonEdgeIndex(Exception):
    pass


class Player(abstract.AbstractPlayer):
    def __init__(self, setup_time, player_color, time_per_k_turns, k):
        abstract.AbstractPlayer.__init__(self, setup_time, player_color, \
                time_per_k_turns, k)
        self.clock = time.time()

        # We are simply providing (remaining time / remaining turns) for each \
        #       turn in round.
        # Taking a spare time of 0.05 seconds.
        self.turns_remaining_in_round = self.k
        self.time_remaining_in_round = self.time_per_k_turns
        self.time_for_current_move = self.time_remaining_in_round / \
                self.turns_remaining_in_round - 0.05
        # keep the game-moves as a string
        self.moves = ''
        self.last_state = GameState()

        # chose board configuration
        if self.color == O_PLAYER:
            # will be set after opponent first move
            self.book2reality = None
            self.reality2book = None
        else:
            self.book2reality = self.book2reality1
            self.reality2book = self.reality2book1

        self.alpha_beta_algorithm = MiniMaxWithAlphaBetaPruning(self.utility, \
                self.color, self.no_more_time, None)

        # for performence
        self.max_steps_left = 62

        # create opening book
        opening_book = {}
        f = open("best_70_opens.gam", 'r')
        # FIXME: remove error check before submmision
        if not f:
            print("cannot open file")
            sys.exit(1)

        # assume we play first and update otherwise
        first_move_index = 0
        if self.color == O_PLAYER:
            first_move_index = 1

        for line in f:
            tmp = line.split(' ')[1]
            tmp = re.split(r'[+-]', tmp)
            moves = ''.join(tmp)
            for i in range(first_move_index, 10, 2):
                tmp = re.split('r[+-]', moves)
                key = moves[0:2*i]
                if key not in opening_book:
                    opening_book[key] = moves[2*i:2*i+2]
        f.close()
        self.opening_book = opening_book

    def get_move(self, game_state, possible_moves):
        self.clock = time.time()
        self.time_for_current_move = self.time_remaining_in_round / \
                self.turns_remaining_in_round - 0.05

        self.max_steps_left -= 2

        # discover last move done by opponent
        opponent_move_str_format = ''
        for x in range(BOARD_COLS):
            for y in range(BOARD_ROWS):
                if self.last_state.board[x][y]==EM and game_state.board[x][y]!=EM:
                    opponent_move_str_format = TO_LETTER[str(x+1)] + str(y+1)
        
        # chose the board_configuration - firs opponent move became 'd3' in 
        # oppening book
        if self.book2reality == None:
            if opponent_move_str_format == 'd6':
                self.book2reality = self.book2reality1
                self.reality2book = self.reality2book1
            elif opponent_move_str_format == 'e3':
                self.book2reality = self.book2reality2
                self.reality2book = self.reality2book2
            elif opponent_move_str_format == 'c5':
                self.book2reality = self.book2reality3
                self.reality2book = self.reality2book3
            elif opponent_move_str_format == 'f4':
                self.book2reality = self.book2reality4
                self.reality2book = self.reality2book4
            else:
                raise ImpossibleBoardTransform

        # append opponent move to self.moves - this will represent the key.
        # if we play first we will append '' to '' (nothing will hapen)
        self.moves += self.reality2book(opponent_move_str_format)

        # this case is handled in run_game.py
        assert(len(possible_moves) != 0)

        # find the best move
        if len(possible_moves) == 1:
            best_move =  possible_moves[0]
        else:
            # check if next move can be determined from oppening book
            oppening_book_res = self.opening_move()
            if oppening_book_res != None:
                best_move = oppening_book_res
            else:
                curr_depth = 1

                # there is maximum max_steps_left steps in the game
                last_move = None
                while curr_depth < self.max_steps_left:
                    try:
                        _, best_move = self.alpha_beta_algorithm.search( \
                                game_state, curr_depth, -INFINITY*2, INFINITY*2, True)

                        if last_move != best_move:
                            game_state_copy = copy.deepcopy(game_state)
                            game_state_copy.perform_move(best_move[0], best_move[1])
                            self.last_state = game_state_copy

                        last_move = best_move
                        curr_depth += 1
                    except ExceededTimeError:
                        break

        to_be_append = TO_LETTER[str(best_move[0]+1)] + str(best_move[1]+1)
        self.moves += self.reality2book(to_be_append)

        if self.turns_remaining_in_round == 1:
            self.turns_remaining_in_round = self.k
            self.time_remaining_in_round = self.time_per_k_turns
        else:
            self.turns_remaining_in_round -= 1
            self.time_remaining_in_round -= (time.time() - self.clock)

        return best_move

    def opening_move(self):

        # check if we can find the next move in the oppening book
        if self.moves not in self.opening_book:
            return None

        res = self.book2reality(self.opening_book[self.moves])
        return [int(TO_DIGIT[res[0]])-1, int(res[1])-1]
        
    def book2reality1(self, str_move):
        old_digit = str_move[1]
        old_letter = str_move[0]
        new_digit = str(BOARD_ROWS-int(old_digit)+1)
        new_letter = old_letter
        return new_letter + new_digit

    def reality2book1(self, str_move):
        if str_move == '':
            return ''
        return self.book2reality1(str_move)
        
    def book2reality2(self, str_move):
        old_digit = str_move[1]
        old_letter = str_move[0]
        new_digit = old_digit
        new_letter = REVERSE_LETTER[old_letter]
        return new_letter + new_digit

    def reality2book2(self, str_move):
        if str_move == '':
            return ''
        return self.book2reality2(str_move)

    def book2reality3(self, str_move):
        old_digit = str_move[1]
        old_letter = str_move[0]
        new_digit = TO_LETTER[old_digit]
        new_letter = TO_DIGIT[REVERSE_LETTER[old_letter]]
        return new_digit + new_letter

    def reality2book3(self, str_move):
        if str_move == '':
            return ''
        return self.book2reality4(str_move)

    def book2reality4(self, str_move):
        old_digit = str_move[1]
        old_letter = str_move[0]
        new_digit = REVERSE_LETTER[TO_LETTER[old_digit]]
        new_letter = TO_DIGIT[old_letter]
        return new_digit + new_letter

    def reality2book4(self, str_move):
        if str_move == '':
            return ''
        return self.book2reality3(str_move)
#------------------------------------------------------------------------------


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


    def utility(self, state):
        assert(len(state.get_possible_moves()) != 0)

        mobility_fac = 1
        score_fac = 1 

        mobility_res = self.__mobility_utility(state) 
        score_res = self.__score_utility(state)

        return mobility_res*mobility_fac + score_res*score_fac

#------------------------------------------------------------------------------

    def selective_deepening_criterion(self, state):
        # Simple player does not selectively deepen into certain nodes.
        return False

    def no_more_time(self):
        return (time.time() - self.clock) >= self.time_for_current_move

    def __repr__(self):
        return '{} {}'.format(abstract.AbstractPlayer.__repr__(self), 'old_competition')

# c:\python35\python.exe run_game.py 3 3 3 y simple_player random_player
