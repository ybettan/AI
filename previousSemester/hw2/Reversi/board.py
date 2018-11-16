"""A game-specific implementations of utility functions.
"""
from __future__ import print_function, division
from .consts import *

class GameState:
    def __init__(self):
        """ Initializing the board and current player.
        """
        self.board = []
        for i in range(BOARD_COLS):
            self.board.append([EM] * BOARD_ROWS)

        for x in range(BOARD_COLS):
            for y in range(BOARD_ROWS):
                self.board[x][y] = EM
        
        # Starting pieces:
        self.board[3][3] = X_PLAYER
        self.board[3][4] = O_PLAYER
        self.board[4][3] = O_PLAYER
        self.board[4][4] = X_PLAYER
                    
        self.curr_player = X_PLAYER
    
    def isOnBoard(self, x, y):
    # Returns True if the coordinates are located on the board.
        return x >= 0 and x <= 7 and y >= 0 and y <=7

    def isValidMove(self, xstart, ystart):
        if self.board[xstart][ystart] != EM or not self.isOnBoard(xstart, ystart):
            return False

        self.board[xstart][ystart] = self.curr_player # temporarily set the tile on the board.

        tilesToFlip = []
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x, y = xstart, ystart
            x += xdirection # first step in the direction
            y += ydirection # first step in the direction
            if self.isOnBoard(x, y) and self.board[x][y] == OPPONENT_COLOR[self.curr_player]:
                # There is a piece belonging to the other player next to our piece.
                x += xdirection
                y += ydirection
                if not self.isOnBoard(x, y):
                    continue
                while self.board[x][y] == OPPONENT_COLOR[self.curr_player]:
                    x += xdirection
                    y += ydirection
                    if not self.isOnBoard(x, y): # break out of while loop, then continue in for loop
                        break
                if not self.isOnBoard(x, y):
                    continue
                if self.board[x][y] == self.curr_player:
                    # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])

        self.board[xstart][ystart] = EM # restore the empty space
        if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
            return False
        return tilesToFlip


    def get_possible_moves(self):
        validMoves = []

        for x in range(BOARD_COLS):
            for y in range(BOARD_ROWS):
                if self.isValidMove(x, y) != False:
                    validMoves.append([x, y])
        return validMoves

    def perform_move(self, xstart, ystart):       
        tilesToFlip = self.isValidMove(xstart, ystart)
        if tilesToFlip == False:
            return False
        
        self.board[xstart][ystart] = self.curr_player
        for x, y in tilesToFlip:
            self.board[x][y] = self.curr_player
        # Updating the current player.
        self.curr_player = OPPONENT_COLOR[self.curr_player]
        return True
    
    def get_winner(self):
        my_u = 0
        op_u = 0
        for x in range(BOARD_COLS):
            for y in range(BOARD_ROWS):
                if self.board[x][y] == self.curr_player:
                    my_u += 1
                if self.board[x][y] == OPPONENT_COLOR[self.curr_player]:
                    op_u += 1
        if my_u > op_u:
            return self.curr_player
        elif my_u < op_u:
            return OPPONENT_COLOR[self.curr_player]
        else:
            return TIE

        
    def draw_board(self):
    # This function prints out the board that it was passed. Returns None.
        HLINE = '  +---+---+---+---+---+---+---+---+'
        VLINE = '  |   |   |   |   |   |   |   |   |'

        print(HLINE)
        for y in range(BOARD_COLS):
            #print(VLINE)
            print(y, end=' ')
            for x in range(BOARD_ROWS):
                print('| %s' % (self.board[x][y]), end=' ')
            print('|')
            #print(VLINE)
            print(HLINE)
        print('    0   1   2   3   4   5   6   7')
        print("\n" + self.curr_player + " Player Turn!\n\n")

    def __hash__(self):
        """This object can be inserted into a set or as dict key. NOTICE: Changing the object after it has been inserted
        into a set or dict (as key) may have unpredicted results!!!
        """
        return hash(','.join([self.board[(i,j)]
                              for i in range(BOARD_ROWS)
                              for j in range(BOARD_COLS)] + [self.curr_player]))

    def __eq__(self, other):
        return isinstance(other, GameState) and self.board == other.board and self.curr_player == other.curr_player

