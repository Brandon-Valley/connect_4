#Learn_bot
from numpy import exp, array, random, dot
import random

import ai_funcs #Only for testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Learn_bot:
    def __init__(self, prev_weights):
        self.synaptic_weights = prev_weights
        pass
        
    def get_move(self, board, self_chip):
        return ai_funcs.get_rand_move(board)

def translate_board(board):
    pass
        
        
        
        
        
        
        
#     
# training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
# training_set_outputs = array([[0, 1, 1, 0]]).T
# random.seed(1)
# synaptic_weights = 2 * random.random((3, 1)) - 1
# for iteration in range(10000):
#     output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
#     synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
# print(synaptic_weights)
# print( 1 / (1 + exp(-(dot(array([0, 1, 0]), synaptic_weights)))))
