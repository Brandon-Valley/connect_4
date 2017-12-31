import Player
import Board

ADD_COLOR = False    
TEST_NUM_GAMES = 1
TEST_SHOW_BOARD = True

RED = '\x1b[0;37;41m'
BLUE = '\x1b[0;37;44m'
BLACK = '\x1b[0;37;40m'
WIN_NUM = 4


if ADD_COLOR == True:
    CHIP1 = BLUE + 'X' + BLACK
    CHIP2 = RED + 'O' + BLACK
else:
    CHIP1 = 'X'
    CHIP2 = 'O'

def game(board, p1_type, p2_type, show_board = True):
    player1 = Player. Player (p1_type, CHIP1)    
    player2 = Player. Player (p2_type, CHIP2)
    
    moves = 0
    win = False
    
    #main game loop
    while (win == False):
      if (moves % 2 == 0):
        c_player = player1
      else:
        c_player = player2
      
      x = c_player. get_move(board)
      board. play (c_player.chip, x)
      
      moves += 1
      if show_board == True:
          board. display ()
      win = board. win_check (WIN_NUM)
      
    return c_player.chip
    




