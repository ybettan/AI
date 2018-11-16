import sys
from players.AI2_302279138_303086854.better_player import Player
from Reversi.board import GameState


## __init__ test
player = Player(2, 'X', 10, 5)
assert(player.moves == '')
assert(player.last_state == GameState())
assert(player.book2reality == player.book2reality1)

player = Player(2, 'O', 10, 5)
assert(player.moves == '')
assert(player.last_state == GameState())
assert(player.book2reality == None)


# book2reality1 test
assert(player.book2reality1('a1') == 'a8')
assert(player.book2reality1('f7') == 'f2')

# reality2book1 test
assert(player.reality2book1('a8') == 'a1')
assert(player.reality2book1('f2') == 'f7')
assert(player.reality2book1('d6') == 'd3')


# book2reality2 test
assert(player.book2reality2('a1') == 'h1')
assert(player.book2reality2('c4') == 'f4')

# reality2book2 test
assert(player.reality2book2('h1') == 'a1')
assert(player.reality2book2('f4') == 'c4')


# book2reality3 test
assert(player.book2reality3('c5') == 'e6')
assert(player.book2reality3('f2') == 'b3')

# reality2book3 test
assert(player.reality2book3('e6') == 'c5')
assert(player.reality2book3('b3') == 'f2')


# book2reality4 test
assert(player.book2reality4('b8') == 'a2')
assert(player.book2reality4('e1') == 'h5')

# reality2book4 test
assert(player.reality2book4('a2') == 'b8')
assert(player.reality2book4('h5') == 'e1')


# get_move check
player = Player(2, 'X', 10, 5)
state = GameState()
assert(player.moves == '')
assert(player.opening_move() == [3, 5]) # 'd3'->'d6'
possible_moves = []
assert(player.get_move(state, possible_moves) == [3, 5]) # 'd6'
assert(player.moves == 'd3')
state.perform_move(3,5)
state.perform_move(2,3)
assert(player.get_move(state, possible_moves) == [5, 2]) # 'd6'
assert(player.moves == 'd3c5f6')
state.perform_move(5,2)

player = Player(2, 'O', 10, 5)
state = GameState()
assert(player.moves == '')
possible_moves = []
state.perform_move(2,4) # book2reality3
assert(player.get_move(state, possible_moves) == [4, 5])
assert(player.book2reality == player.book2reality3)
assert(player.moves == 'd3c5')
state.perform_move(4,5)
state.perform_move(5,4)
assert(player.get_move(state, possible_moves) == [2, 3])
assert(player.moves == 'd3c5d6e3')
state.perform_move(2,3)


#state.draw_board()


