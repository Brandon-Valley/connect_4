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
    game.hvh_game(b)
    
elif num_humans == 1:
    game.hvai_game(b)
    
elif num_humans == 0:
    game.ai_train_session()
    
