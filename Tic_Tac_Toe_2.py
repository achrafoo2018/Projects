from sys import stdout
from random import randint
import os


def display_board(board):
    k = -3
    for i in range(3):
        k += 3
        for j in range(3):
            if j !=1:
                print("   |   |   ")
            else:
                stdout.write(f" {board[k]} | {board[k+1]} | {board[k+2]}\n") # print the board
        if i<2:
            print('-------------')


def place_marker(board, marker, position):
    switcher = {
        9: 2,
        8: 1,
        7: 0,
        3: 8,
        2: 7,
        1: 6
    }
    if 4<=position<=6:
        board[position-1] = marker
    else:
        board[switcher[position]] = marker
def win_check(board, mark):
    return (board[0] == board[1] == board[2] == mark or
            board[0] == board[3] == board[6] == mark or
            board[0] == board[4] == board[8] == mark or
            board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or
            board[3] == board[4] == board[5] == mark or
            board[6] == board[7] == board[8] == mark or
            board[6] == board[4] == board[2] == mark
            )


def choose_first():
    if randint(0,1000) % 2 == 0: # randomize who starts first
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position): # check if the position is not taken
    switch = { # switch numbers given by players to it's index on the list
        7: 0,
        8: 1,
        9: 2,
        4: 3,
        5: 4,
        6: 5,
        1: 6,
        2: 7,
        3: 8
    }
    return board[switch[position]] == " "


def full_board_check(board): # check if the board is full
    return " " not in board


def player_choice(board):
    while True:
        try:
            choice = int(input("Choose You next move (1-9) : ")) # ask player for his next move
        except ValueError:
            continue
        if 1<=choice<=9:
            break
    if space_check(board, choice):
        return choice


def replay(): # ask players whether they want to play again
    while 1:
        again = input("\t\t\tYou want to play again (y/n)?")
        if again in ['y', 'Y','Yes','YES','n','N','No']:
            break
    return again not in ['n','N','No']


def board_clean(board):
    for i in board:
        if i != " ":
            return False
    return True


# Intialize players score
player1_score = 0
player2_score = 0
# main
os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal
name1 = input("Player 1 name ? :").capitalize()
name2 = input("Player 2 name ? :").capitalize()
while True:
    board = [" "] * 9
    os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal
    print('---  Welcome To TiC TaC ToE ---')

    if randint(0, 100) % 2 == 0:
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'
    turn = choose_first()
    start = ' play first :'
    turn_text = " turn : "
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(board)
        if turn == 'Player 1':
            # print start first if it's the first move in the game else print turn
            print(f'{name2} ({p2}){start if board_clean(board) else turn_text}')
            while True: # repeat until player give valid move
                move = player_choice(board) # ask for player's next move
                try:
                    if not full_board_check(board) & space_check(board, move): # check if the board is not full and next move is not already taken
                        place_marker(board, p2, move)
                        break
                except:
                    continue
            turn = 'Player 2'
        else:
            print(f'{name1} ({p1}){start if board_clean(board) else turn_text}')
            while True:
                move = player_choice(board)
                try:
                    if not full_board_check(board) & space_check(board, move):
                        place_marker(board, p1, move)
                        break
                except:
                    continue
            turn = 'Player 1'
        if win_check(board, p1):
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(board)
            print(f'\n\t{name1} ({p1}) won the round\n')
            player1_score += 1
            break
        elif win_check(board, p2):
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(board)
            print(f'\n\t{name2} ({p2}) won the round\n')
            player2_score += 1
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        if full_board_check(board):
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(board)
            print('Tied GG WP')
            break
    if not replay(): # check if players wants to play again
        if player1_score != player2_score:
            print(f'\n\tGG WP {name1 if player1_score > player2_score else name2} won the game') # print the winner
        else :
            print(f'\tTied ! GG WP Both Of You') # print tied message
        # print players score
        print(f'{name1} ({p1}) score : {player1_score}')
        print(f'{name2} ({p2}) score : {player2_score}')
        break

        
        
