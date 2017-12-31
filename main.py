import game
import ui
import Board

DO_INTRO = True


if DO_INTRO == True:
    num_humans = ui. get_num_humans ()
    size = ui. get_board_size ()
else:
    num_humans = 2
    size = {'height': 6, 'width': 7}
    print('starting game...')
    
    
b = Board.Board (size ['width'], size ['height'])
b. display ()

if num_humans == 2:
    player1_type = 'human'
    player2_type = 'human'
    winning_chip = game.game(b, player1_type, player2_type)    
    print ('PLAYER '+ winning_chip +" WINS!!!")
    
elif num_humans == 1:
    player1_type = 'human'
    player2_type = 'ai'
    winning_chip = game.game(b, player1_type, player2_type)    
    print ('PLAYER '+ winning_chip +" WINS!!!")
    
elif num_humans == 0:
    if DO_INTRO == True:
        num_games = input('Input number of games: ')
        show_board = input('Show final board(s): ')
    else:
        num_games = TEST_NUM_GAMES
        show_board = TEST_SHOW_BOARD
        
    player1_type = 'ai'
    player2_type = 'ai'  
        
    #train
