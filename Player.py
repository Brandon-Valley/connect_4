try:
    import sl4a #only for finding hardware #need???????????????????????????????????
    hardware = 'phone'
except:
    hardware = 'pc'

import ui


#player
class Player:
    def __init__(self, player_type, chip):
      self. chip= chip
      self. player_type = player_type
    
    def get_move (self, board):
      if self.player_type == 'human':
        return self.human_get_move(board)
      else: #AI
        return self.ai_get_move(board)
    
    def human_get_move (self, board):
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

    def ai_get_move(self, board):
      pass
    

