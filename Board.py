# board
import Player
import ui

class Board:
  def __init__(self, width, height):
    self. width = width
    self. height = height
    self. chips= []
    
    for x in range (width):
      self.chips. append ([])
      
      
  def display (self):
    print ('\n' * 11)
    numbers = ''
    for x in range (self. width):
      numbers +=(' ' + str(x + 1))
    print (numbers)
    
    #upper_line= ' _' * self.width
    #print (upper_line)
    
    for y_opp in range (self. height):
      y = self. height - y_opp - 1
      line=['|']
      for x in range (self. width):
        if y < len(self.chips [x]):
          chip= self.chips [x][y]
        else:
          chip= '_'
        line. append (chip+'|')
        
      line_str = ''
      for element in line:
        line_str += element
      print (line_str)
    print (numbers)
    print ('')
      
      
  def play (self, chip, x):
    self.chips [x]. append (chip)
    
    
  def valid_move (self, x):
    if x <= self. width:
      if len(self.chips [x]) <= self. height:
        return True
    return False
    
    
  def get_chip (self, x, y):
    if y < len(self. chips [x]):
      chip = self. chips [x][y]
    else:
      chip = '_'
    return chip
   
      
  def win_check (self, win_num):
    for column in self. chips:
      if list_check (win_num, column):
        return True
        
    for y in range (self. height):
      row = []
      for x in range (self. width):
        chip = self. get_chip (x, y)
        row. append (chip)
      if list_check (win_num, row):
        return True
    
    
    c_type_list = ['height', 'width']
    for c_type in c_type_list:
      if c_type == 'height':
        c_range = self. height
        nc_range = self. width
      else: #width
        c_range = self. width
        nc_range = self. height
      #make dd = 1 and -1
      for ddnum in range (2):
        #print (ddnum)
        dd = 1 + (ddnum * (-2))
        #print ("c_range: %s  dd: %s" %(c_range, dd))
        
        for c in range (c_range):
          #find out if it's possible to win
          win_possible = True
          if dd == -1 and c_range == self. height:
            if not c >= win_num:
              win_possible= False
          elif dd == -1 and c_range == self. width:
            if c < win_num-1:
              win_possible = False
            #else:
              #print ("c + 1:", c + 1)
          else:
            if not c <= c_range - win_num:
              win_possible = False
          
          #if it is possible to win, do main loop
          if win_possible:
            count = 0
            #print ('set count:', count)
            diagonal = []          

           
            if dd == 0:
              if c_type == 'height':
                x = count #((nc_range -1)*(1-dd)/2) + (count * dd)
                y = c + count# (c_range*(1-dd)/2) + (c*dd) + count
              else: #width
                x = c + count#c + (count * dd)
                y = count
          
              chip = self.get_chip (int(x), int(y))
              diag. append (chip)
              count += 1
            
            '''
            if dd == 1:
              while ((count + c) < c_range) and (count <= nc_range):
                self.make_diagonal (dd, c, count, c_range, nc_range, c_type, diagonal)
            elif dd == -1 and c_type == 'width':
              while (count <= nc_range) and c - count>=0:
                self.make_diagonal (dd, c, count, c_range, nc_range, c_type, diagonal)
            elif dd == -1 and c_type == 'height':
              while c >= win_num and c_range - c + count <= c_range and count <= nc_range:
                self.make_diagonal (dd, c, count, c_range, nc_range, c_type, diagonal)
            '''
        
            if False:#fix!!!!!!!!!!!!!!!!!!!
              pass
            elif ( dd== -1 and c_type == 'width'):
              while (count <= nc_range) and c - count>=0:
                x = c - count
                y = count
          
                 # print ('x,y: (%s,%s) count = %s, c = %s '%(x+1, y+1, count, c))
                chip = self.get_chip (x, y)
                diagonal. append (chip)
                count += 1
       
            elif ( dd== -1 and c_type == 'height'):
              while c >= win_num and c_range - c + count <= c_range and count <= nc_range: #((count + c) >= 0) and (count >= 0) and (count < nc_range):
                #print ('checking d= %s, count = %s, c = %s '%(dd, count, c))
                x = nc_range -1 - count
                y = c_range - c + count

                #print ('x,y: (%s,%s) count = %s, c = %s '%(x+1, y+1, count, c))
                chip = self.get_chip (x, y)
                diagonal. append (chip)
                count += 1
            
          if list_check (win_num, diagonal):
            return True    
    return False
    
    
  def make_diagonal (self, dd, c, count, c_range, nc_range, c_type, diag):
    if c_type == 'height':
      x = ((nc_range -1)*(1-dd)/2) + (count * dd)
      y = (c_range*(1-dd)/2) + (c*dd) + count
    else: #width
      x = c + (count * dd)
      y = count
          
      chip = self.get_chip (int(x), int(y))
      diag. append (chip)
      count += 1
    
    
def list_check (num, row_list):
  count = 0
  check_chip =''
  for chip in row_list:
    if chip == check_chip and check_chip != '_':
      count += 1
    else:
      check_chip = chip
      count = 0
    if count == num - 1:
      return True
  return False