#ui
import sl4a

droid = sl4a.Android()


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
  title = 'Number Of Players'
  message = ('Select Number Of Players')
  droid.dialogCreateAlert(title, message)
  droid.dialogSetPositiveButtonText('2: Human vs Human')
  droid.dialogSetNegativeButtonText('0: AI vs AI')
  droid.dialogSetNeutralButtonText('1: Human vs AI')
  droid.dialogShow()
  response = droid.dialogGetResponse().result
  #return response['which'] in ('positive', 'negative')
  if response ['which'] == 'positive':
    return 2
  elif response ['which'] == 'negative':
    return 0
  else: # neutral
    return 1
    


def ask_if_standard_board():
  title = 'Board Size'
  message = ('Select board size: Width x Height')
  droid.dialogCreateAlert(title, message)
  droid.dialogSetPositiveButtonText('Standard: 7 x 6')
  droid.dialogSetNegativeButtonText('Custom')
  #droid.dialogSetNeutralButtonText('Cancel')
  droid.dialogShow()
  response = droid.dialogGetResponse().result
  #return response['which'] in ('positive', 'negative')
  if response ['which'] == 'positive':
    return True
  else:
    return False


def get_int(prompt, dialog_box = False):
  if dialog_box:
    intstr = droid.dialogGetInput(prompt).result
  else:
    intstr = input (prompt)
  integer = int(intstr)
  return integer





