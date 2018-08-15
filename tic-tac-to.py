#python progrma for tic tac to
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker=input('Player 1 , choose X or O: ')
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return(player1,player2)


player1_marker,player2_marker=player_input()

def place_marker(board,marker,position):
    board[position]=marker
    
def win_check(board,mark):
    return((board[1]==board[2]==board[3]==mark)or(board[4]==board[5]==board[6]==mark)or
           (board[7]==board[8]==board[9]==mark)or(board[1]==board[4]==board[7]==mark)or
           (board[2]==board[5]==board[8]==mark)or(board[3]==board[6]==board[9]==mark)or
           (board[1]==board[5]==board[9]==mark)or(board[3]==board[5]==board[7]==mark))


import random
def choose_function():
    flip=random.randint(0,1)
    if flip==0:
        return'player1'
    else:
        return 'player2'


def space_check(board,position):
    return board[position]==' '


def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    else:
        return True

def player_choice(board):
    position= 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
    	position = int(input('Choose position from (1-9): '))
    
    return position


def replay():
    choice=input("play again? yes or no: ")
    
    return choice=='yes'




print('Welcome to TIC TAC TOE')

while True:

    the_board=[' ']*10
    player1_marker,player2_marker=player_input()


    turn=choose_function()
    print(turn +' will go first')


    play_game=input('Ready to play? y or n?: ')
    if play_game=='y':
        game_on=True
    else:
        game_on=False


    while game_on:
        if turn=='player1':

            display_board(the_board)

            position=player_choice(the_board)

            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 won')
                game_on= False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE')
                    game_on=False
                else:
                    turn='player2'


        else:

            display_board(the_board)

            position=player_choice(the_board)

            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE')
                    game_on = False
                else:
                    turn='player1'

    if not replay():
        break