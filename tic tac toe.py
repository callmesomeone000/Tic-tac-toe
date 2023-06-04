import random


board = ['-','-','-',
         '-','-','-',
         '-','-','-']
currentplayer = 'X'
winner = None
gamerunning = True

#Printing the game board
def print_board(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

#Take palyer input
def player_input(board):
    inp=int(input('Enter a number between 1-9: '))
    if inp>=1 and inp<=9 and board[inp-1]=='-':
        board[inp-1] = currentplayer
    else:
        print('Oops player is already in this spot ')

        
#Check win or tie

def check_horizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1]!='-':
        winner=board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3]!='-':
        winner=board[2]
        return True
    elif board[6] == board[7] == board[8] and board[6]!='-':
        winner=board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!='-':
        winner=board[0]
        return True
    elif board[1] == board[4] == board[7] and board[7]!='-':
        winner=board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!='-':
        winner=board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!='-':
        winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!='-':
        winner=board[2]
        return True

    
def check_tie(board):
    global gamerunning
    if '-' not in board:
        print_board(board)
        print('Its a tie!!!')
        gamerunning = False

def check_win():
    if check_diagonal(board) or check_horizontle(board) or check_row(board):
        print(f'The winner is {winner}')


#Switch the palyer

def switch_player():
    global currentplayer
    if currentplayer == 'X':
        currentplayer='O'
    else:
        currentplayer = 'X'

'''#Computer
def computer(board):
    while currentplayer == 'O':
        position = random.randint(0,8)
        if board[position]=='-':
            board[position]='O'
            switch_player()'''

#check for win or tie again

while gamerunning:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    '''computer(board)
    check_win()
    check_tie(board)'''






    
