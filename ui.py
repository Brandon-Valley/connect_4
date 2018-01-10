#ui
import phoneFuncs

try:
    import sl4a
    droid = sl4a.Android()
    hardware = 'phone'
except:
    hardware = 'pc'
    

def get_board_size():
  size = {}
  if (ask_if_standard_board () == True):
    size = {'width':  7,
            'height': 6}
  else:
    size ['width'] = get_int('Input board width:', True)
    size ['height']= get_int('Input board height:', True)
  return size


def get_num_humans():
    if hardware == 'phone':
        return(phoneFuncs.get_num_humans())
    
    return int(input('Input number of humans (0-2): '))


def ask_if_standard_board():
    if hardware == 'phone':
        return(phoneFuncs.ask_if_standard_board())
    
    return get_tf('Standard Board? (7x6) (y/n): ')
        
        
def get_int(prompt, dialog_box = False):
    if hardware == 'phone':
        return(phoneFuncs.get_int(prompt, dialog_box))

    return int(input(prompt))


def get_tf(prompt):
    while(1):
        choice = input(prompt)
        
        if choice == 'y':
            return True
        elif choice =='n':
            return False
        else:
            print('ERROR WRONG INPUT TRY AGAIN')





