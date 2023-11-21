# win conditions 
# all orthogonal
# all diagonal

# 1|2|3 
# - - - 
# 4|5|6
# - - -
# 7|8|9

# 1,2,3
# 4,5,6
# 7,8,9 

# 1,4,7
# 2,3,5
# 3,6,9

# 1,5,9
# 3,5,7 

#lets start with just linear 3 in a row 
import random
import logging 


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


options = [1,2,3,4,5,6,7,8,9]
board = 9*[-10]
counter = 0 

while True: 
    play = int(input("select sq:"))
    options.remove(play)
    
    board[play-1] = (counter % 2)
    counter +=1
    
    #graphic 
    print(board)

    if sum(board) > 0: 
        break


