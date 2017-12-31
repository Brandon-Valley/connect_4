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

def core_game(board, p1_type, p2_type, show_board = True):
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
    
def hvh_game(board):
    player1_type = 'human'
    player2_type = 'human'
    winning_chip = core_game(board, player1_type, player2_type)    
    print ('PLAYER '+ winning_chip +" WINS!!!")


def hvai_game(board):
    player1_type = 'human'
    player2_type = 'ai'
    winning_chip = core_game(board, player1_type, player2_type)    
    print ('PLAYER '+ winning_chip +" WINS!!!")


def ai_train_session():
    if DO_INTRO == True:
        num_games = input('Input number of games: ')
        show_board = input('Show final board(s): ')
    else:
        num_games = TEST_NUM_GAMES
        show_board = TEST_SHOW_BOARD
        
    player1_type = 'ai'
    player2_type = 'ai'  
        
