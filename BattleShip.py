"""Battle Ship Game"""
import random
#Generate a board for battleship
#generate the 'sea' & make it look like a board
board = []
for i in range(6):
    board.append(['~']*6)

#generate a function to print the board
def print_board(board):
    for i in range(6):
        print ' '.join(board[i])

#generate ship orientation, 1 = vertical, 2 horizontal
ship_orientation = random.choice([1,2])

#assign the random ship position to the board
ship_col = random.randint(0,len(board)-1)
ship_row = random.randint(0,len(board)-1)
print ship_col, ship_row

#user will get 5 turns 
for turn in range(5):
    print "Turn", turn + 1
    print_board(board)
    
    #need raw input from the player & Check if its a valid input
    i = True
    while i:
        guess_col = raw_input("Attack Column: ")
        #test to see if what the user inputted is a number
        test = ord(guess_col[0])
        if test >= 65:
            print "Please enter a valid column number!"
        else:
            guess_col = int(guess_col)
            i = False
    i = True
    while i:
        guess_row = raw_input("Attack Row: ")
        #test to see if what the user inputted is a number
        test = ord(guess_row[0])
        if test >= 65:
            print "Please enter a valid row number!"
        else:
            guess_row = int(guess_row)
            i = False

    #compare the user's guess to the actual value
    if guess_col == ship_col and guess_row == ship_row:
        board[ship_row][ship_col] = "O"
        print
        print "You sank my battleship Son!"
        print_board(board)
        break
    
    #code if guess is out of range
    elif (guess_col > (len(board)-1)) or guess_row > (len(board)-1):
        print "Dude that's not even on the Board!"
        print
    else:
        board[guess_row][guess_col] = "X"
        print "Na uh Girl!You missed!"
        print
print "Game Over"  

