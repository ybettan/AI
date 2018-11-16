
#==============================================================================
# Game pieces
# - EM is an empty location on the board.
#==============================================================================
EM = ' '

X_PLAYER = 'X'
O_PLAYER = 'O'
TIE = 'tie'

#===============================================================================
# Board Shape
#===============================================================================
BOARD_ROWS = BOARD_COLS = 8

# The Opponent of each Player
OPPONENT_COLOR = {
    X_PLAYER: O_PLAYER,
    O_PLAYER: X_PLAYER
}
