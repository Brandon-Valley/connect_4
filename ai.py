from random import randint

def get_move(board):
    #make list of possable moves
    pMoves = []
    for colNum in range(board.width):
        if len(board.chips[colNum]) < board.height:
            pMoves.append(colNum)
    
    #this will be neural net stuff at some point
    randPic = randint(0, len(pMoves))
    return pMoves[randPic]
        