from numpy import random

import game
import ui
import Board
import ai_funcs

random.seed(1)

DO_INTRO = True


if DO_INTRO == True:
    num_humans = ui. get_num_humans ()
    size = ui. get_board_size ()
else:
    num_humans = 0
    size = {'height': 6, 'width': 7}
    print('starting game...')
    

if num_humans == 2:
    b = Board.Board (size ['width'], size ['height'])
    b. display ()
    game.hvh_game(b)
    
elif num_humans == 1:
    b = Board.Board (size ['width'], size ['height'])
    b. display ()
    game.hvai_game(b, size)
    
elif num_humans == 0:
    if DO_INTRO == True:
        number_of_games = ui.get_int('Input number of games: ')
        show_the_board = ui.get_tf('Show final board(s) (y/n): ')
    else:
        number_of_games = 10
        show_the_board = True
    
    ai_funcs.train_session(size, number_of_games, show_the_board)
    
