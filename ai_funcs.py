# from random import randint
from numpy import random
import os
   
from logger import logger
import Learn_bot
import game
import Player
import Board


NUM_TIES_BEFORE_MUTATION = 2#change back to something like 100!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

full_path = os.path.realpath(__file__)
weights_path =  os.path.dirname(full_path) + '\\synaptic_weights'

#not really random
def get_rand_move(board):
    #make list of possable moves
    pMoves = []
    for colNum in range(board.width):
        if len(board.chips[colNum]) < board.height:
            pMoves.append(colNum)
    
    #this will be neural net stuff at some point
    randPic = random.choice(pMoves)
    return randPic


def mutate(old_weights):
    return old_weights
      
        
def train_session(board_size, num_games, show_final_board):
    #get first weights
    synaptic_weights_1 = get_synaptic_weights(board_size)
    synaptic_weights_2 = mutate(synaptic_weights_1)
    
    #make 1st 2 learnbots
    lb1 = Learn_bot.Learn_bot(synaptic_weights_1)
    lb2 = Learn_bot.Learn_bot(synaptic_weights_2)
    
    p1 = Player.Player('ai', game.CHIP1, lb1)
    p2 = Player.Player('ai', game.CHIP2, lb2)
        
    games_played = 0    
    while(games_played < num_games):
        #find "winner" (best 2 out of 3?????)
        p1_wins = 0
        p2_wins = 0
        count = 0
        
        while( ( abs(p1_wins - p2_wins) < 2 ) and (p1_wins - 1) < NUM_TIES_BEFORE_MUTATION):
            new_board = Board.Board (board_size ['width'], board_size ['height'])
            #swap who goes first
            if count % 2 == 0:
                winning_player = game.core_game(new_board, p1, p2, False)
            else:
                winning_player = game.core_game(new_board, p2, p1, False)
                
            if show_final_board == True:
                new_board.display(False)
            
            #in case of tie
            if winning_player == False:
                p1_wins += 1
                p2_wins += 1
            else:
                #find who won/add to their wins
                if winning_player.chip == p1.chip:
                    p1_wins += 1
                elif winning_player.chip == p2.chip:
                    p2_wins += 1
                else:
                    print('should make a propper error here, error in ai_train_game, invalid winner chip')#!!!!!!!!!!!!!!!
            count += 1
            games_played += 1
            
        
        #if tie, default to player 1 as the winner
        if winning_player == False:
            winning_player = p1
                
        better_bot = winning_player.bot
        
        #set winner as player 1
        p1 = Player.Player('ai', game.CHIP1, better_bot)
        
        #mutate better_bot to make player 2
        #HOW TO DO THIS?????????????????????????????????????????????????????????????????????????
        new_learn_bot = Learn_bot.Learn_bot(better_bot.synaptic_weights)#rn just copies weights!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        p2 = Player.Player('ai', game.CHIP2, new_learn_bot)
        
    #say training is done and log the winning weights (player 1 = winner)
    print('Training done!')
    log_weights(p1.bot.synaptic_weights, board_size)
    print('synaptic weights have been logged!')
               

def log_weights(new_weights, board_size):
    print('new weights:', new_weights)
    new_weights_dict = {}
    
    #format newest weights
    for weight in new_weights:
        new_weights_dict[len(new_weights_dict)] = str(weight[0])
        print(type(weight[0]))
        
    print(new_weights_dict)
    
    #log
    logger.logSingle(new_weights_dict, get_synaptic_weights(board_size))
    
#     try:#if csv already exists
#         old_weights_dl = logger.readCSV(weights_path)
#  
#         #if the training session that was just preformed was on a board that yeilded more weights than any previous training session
#         if len(new_weights) > len(old_weights_dl[0]):
#             need_overwrite = True #if number of fieldnames changes, need to wverwrite csv
#             log_dl = []
#             #add Nones to all existing rows
#             for row_dict in old_weights_dl:
#                 while(len(row_dict) < len(new_weights)):
#                     row_dict[len(row_dict)] = None
#                 log_dl.append(row_dict)
#                 
#         #add Nones to newest weights if needed
#         while(len(new_weights_dict) < len(old_weights_dl[0])):
#             new_weights_dict[len(new_weights_dict)] = None
#     except:
#         pass
#  
#     if need_overwrite == True:    
#         print('overwriting old csv!!!!!!!!!!!!!!!!!!!!!!')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
#         print('log_dl:', log_dl)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         for dict in log_dl:#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             print('length of dict to be logged:', len(dict))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         log_dl.append(new_weights_dict)
#         logger.logList(log_dl, weights_path, False)
#     else:
#         print('logging single!!!!!!!!!!!!!!!!!!')
#         logger.logSingle(new_weights_dict, weights_path)


#if weights exist, reads them, if not, randomly generates some
def get_synaptic_weights(board_size):
    num_digits_for_possable_moves = ( len( bin(board_size['width']) ) - 2 )# number of digits needed to express number of possable moves in binary
    num_chip_spaces = ( board_size['width'] * board_size['height'] ) #number of places a chip can be put on the board
    num_weights = ( num_chip_spaces * 2 ) + num_digits_for_possable_moves
    print('num_weights:', num_weights)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    try:#if any old weights exist
        file_path = get_synaptic_weights_path(board_size)
        old_weights_dl = logger.readCSV(file_path)
        synaptic_weights = old_weights_dl[0]
        print('synaptic_weights:', synaptic_weights)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
    except: # very first train session / no weights read
        synaptic_weights = 2 * random.random((num_weights, 1)) - 1
        
    return  synaptic_weights



def get_synaptic_weights_path(board_size):
    filename = str(board_size['width']) + 'x' + str(board_size['height']) + '.csv'
    return weights_path + '\\' + filename
    
    
    
    
    
    
    