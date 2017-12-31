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

def core_game(board, player1, player2, show_board = True):
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
      
    return c_player
    
def hvh_game(board):
    player1 = Player. Player ('human', CHIP1)    
    player2 = Player. Player ('human', CHIP2)
    winner = core_game(board, player1, player2)    
    print ('PLAYER '+ winner.chip +" WINS!!!")


def hvai_game(board):
    player1 = Player. Player ('human', CHIP1)    
    player2 = Player. Player ('ai', CHIP2)
    winner = core_game(board, player1, player2)    
    print ('PLAYER '+ winner.chip +" WINS!!!")

def ai_train_session(board):
    if DO_INTRO == True:
        num_games = input('Input number of games: ')
        show_board = input('Show final board(s): ')
    else:
        num_games = TEST_NUM_GAMES
        show_board = TEST_SHOW_BOARD
        
    #this will get existing weights later
    if True:# no weights exist
        #make the 2 first Learn_bots
        synaptic_weights_1 = 2 * random.random((board.width, 1)) - 1
        synaptic_weights_2 = 2 * random.random((board.width, 1)) - 1
        
        lb1 = Learn_bot.Learn_bot(board, synaptic_weights_1)
        lb2 = Learn_bot.Learn_bot(board, synaptic_weights_2)
        
        p1 = Player.Player(board, 'ai', CHIP1, lb1)
        p2 = Player.Player(board, 'ai', CHIP2, lb2)
        
        
    else:
        #get weights
        pass
        
