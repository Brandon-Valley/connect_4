try:
    import sl4a #only for finding hardware #need???????????????????????????????????
    hardware = 'phone'
except:
    hardware = 'pc'

import ui
import ai_funcs


#player
class Player:
    def __init__(self, player_type, chip, learn_bot = None):
        self.chip= chip
        self.player_type = player_type
        self.bot = learn_bot
    
    def get_move (self, board):
        if self.player_type == 'ai':
            return self.bot.get_move(board, self.chip)
        
        if self.player_type == 'human':
            prompt = 'Player ' + self.chip + ', your move: '
            x = ui.get_int(prompt) - 1
            
            valid_move_found = False
            while (valid_move_found == False):
              if (board.valid_move (x)):
                valid_move_found = True
              else:
                print ('Invalid Move')
                x = ui.get_int(prompt)
            return x
    


    

