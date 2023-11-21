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


#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')


options = [1,2,3,4,5,6,7,8,9]
board = 9*[-10]
counter = 0 

while options: 
    print(board)

    player = counter % 2
    print(f'player{player}') 

    play = int(input("select sq:"))
    
    while True:
        try: 
            options.remove(play)
            break
        except: 
            print(board)
            print(f'Invalid. Stll player{player}')           
            play = int(input("select sq:"))
        
    
    board[play-1] = (player)
    counter +=1
    
print(board)


def check_win(board):
    check = []
    winner = 'DRAW'
    for i,v in enumerate(board):
        check = board[i:i+3]
        print(check)
        if len(set(check)) == 1 and len(check) == 3:
            winner = f'winner is {set(check)}'
            break 
    return print(winner)

#preset testing 
#board = [1,0,1,0,1,1,0,0,0]
#board = [1,1,0,1,0,0,1,0,0]

print(board)

check_win(board)
