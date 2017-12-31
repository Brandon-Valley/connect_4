import Player
import Board
import ui

def Hgame(board, num_humans):
  player1 = Player. Player ('human',CHIP1)
  if num_humans == 2:
      player2 = Player. Player ('human',CHIP2)
  elif num_humans == 1:
      player2 = Player. Player ('ai',CHIP2)
  
  moves = 0
  win = False

  #main game loop
  while (win == False):
    if (moves % 2 == 0):
      c_player = player1
    else:
      c_player = player2
    
    x = c_player. get_move(b)
    board. play (c_player.chip, x)
    
    moves += 1
    board. display ()
    win = board. win_check (WIN_NUM)
    
  print ('PLAYER '+c_player.chip+" WINS!!!")



DO_INTRO = True
ADD_COLOR = False    

RED = '\x1b[0;37;41m'
BLUE = '\x1b[0;37;44m'
BLACK = '\x1b[0;37;40m'
WIN_NUM = 4

#CHIP_LIST = [BLUE + 'X' + BLACK, RED + 'O' + BLACK]

if ADD_COLOR == True:
    CHIP1 = BLUE + 'X' + BLACK
    CHIP2 = RED + 'O' + BLACK
else:
    CHIP1 = 'X'
    CHIP2 = 'O'

if DO_INTRO == True:
    num_humans = ui. get_num_humans ()
    size = ui. get_board_size ()
else:
    num_humans = 2
    size = {'height': 6, 'width': 7}
    print('starting game...')
    
    
b = Board.Board (size ['width'], size ['height'])
b. display ()

if num_humans in {1,2}:
    Hgame (b, num_humans)
elif num_humans == 0:
    pass



