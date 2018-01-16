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
    
    tie_found = False
    #main game loop
    while (win == False):
        if (moves % 2 == 0):
            c_player = player1
        else:
            c_player = player2
          
        #check for tie
        tie_found = True
        for col in board.chips:
            if tie_found == True:
                if len(col) < board.height:
                    tie_found = False
        if tie_found == True:
            print('tie')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return False
        
        x = c_player. get_move(board)
        board. play (c_player.chip, x)
        
        moves += 1
        if show_board == True:
            board.display()
        win = board.win_check(WIN_NUM)

    return c_player
    
    
def hvh_game(board):
    player1 = Player. Player ('human', CHIP1)    
    player2 = Player. Player ('human', CHIP2)
    winner = core_game(board, player1, player2)    
    print ('PLAYER '+ winner.chip +" WINS!!!")


def hvai_game(board):
    player1 = Player. Player ('human', CHIP1)    
    player2 = Player. Player ('ai_funcs', CHIP2)
    winner = core_game(board, player1, player2)    
    print ('PLAYER '+ winner.chip +" WINS!!!")


    
    