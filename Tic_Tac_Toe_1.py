import numpy as np
from random import randint
import sys
import subprocess as sp


def x_input(g):  # player choose his next move
    l = 0
    while True:
        for i in range(3):
            print()
            for j in range(3):
                sys.stdout.write("|" + g[i, j] + "|\t")
        try:
            l = int(input("\nEnter Your choice (1-9):"))
            sp.call('cls', shell=True)
        except ValueError as err:
            print(err)
        if l in range(1, 10):
            break
    return l


def random_starter(p1, p2, name1, name2):  # make a random to choose who starts first
    choice = randint(1, 100)
    if choice % 2 == 0:
        p1 = True
        p2 = False
        sys.stdout.write(name1 + " Player 1 (O) starts playing :")
    else:
        p1 = False
        p2 = True
        sys.stdout.write(name2 + " Player 2 (X) starts playing:")


def is_winner(switcher, game, pl):  # test if someone won the game
    return (game[switcher[1]] == game[switcher[4]] == game[switcher[7]] == pl or
            game[switcher[2]] == game[switcher[5]] == game[switcher[8]] == pl or
            game[switcher[3]] == game[switcher[6]] == game[switcher[9]] == pl or
            game[switcher[9]] == game[switcher[5]] == game[switcher[1]] == pl or
            game[switcher[7]] == game[switcher[5]] == game[switcher[3]] == pl or
            game[switcher[6]] == game[switcher[5]] == game[switcher[4]] == pl or
            game[switcher[1]] == game[switcher[2]] == game[switcher[3]] == pl or
            game[switcher[7]] == game[switcher[8]] == game[switcher[9]] == pl
            )


sp.call('cls', shell=True)
score1 = score2 = 0
name1 = input("Player 1 name : ").capitalize()
name2 = input("Player 2 name : ").capitalize()
while True:  # repeat the game while the players wanna play again
    sp.call('cls', shell=True)
    game = np.zeros((3, 3), dtype=str)  # decalre an array of empty strings
    x = y = 0
    game[game == ""] = '-'  # replace empty strings with '-'
    sp.call('cls', shell=True)
    player1 = player2 = False
    random_starter(player1, player2, name1, name2)
    winner = ""
    while winner == "":
        if '-' not in list(game[0]) and '-' not in list(game[1]) and '-' not in list(game[2]):  # check if the tic tac table is not full
            sp.call('cls', shell=True)
            print("\nTied !!")
            for i in range(3):
                print()
                for j in range(3):
                    sys.stdout.write("|" + game[i, j] + "|")
            break
        x = x_input(game)  # next move of player
        switcher = {  # switch the number chosen by the player to a tuple to use it as an index
            7: (0, 0),
            8: (0, 1),
            9: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            1: (2, 0),
            2: (2, 1),
            3: (2, 2),
        }
        if game[switcher[x]] == '-':
            if player1:
                game[switcher[x]] = "O"
                player1 = False
                if is_winner(switcher, game, 'O'):
                    sp.call('cls', shell=True)
                    winner = name1 + " (O)"
                    for i in range(3):
                        print()
                        for j in range(3):
                            sys.stdout.write("|" + game[i, j] + "|\t")
                    break
                elif is_winner(switcher, game, 'X'):
                    sp.call('cls', shell=True)
                    winner = name2 + " (X)"
                    for i in range(3):  # print the tic tac toe table
                        print("\n")
                        for j in range(3):
                            sys.stdout.write("|" + game[i, j] + "|\t")
                    break
                print(name2 + " (X) turn :")

            else:
                game[switcher[x]] = "X"
                player1 = True
                if is_winner(switcher, game, 'O'):
                    sp.call('cls', shell=True)
                    winner = name1 + " (O) "
                    for i in range(3):
                        print()
                        for j in range(3):
                            sys.stdout.write("|" + game[i, j] + "|\t")
                    break
                elif is_winner(switcher, game, 'X'):
                    sp.call('cls', shell=True)
                    winner = name2 + " (X)"
                    for i in range(3):
                        print()
                        for j in range(3):
                            sys.stdout.write("|" + game[i, j] + "|\t")
                    break
                print(name1 + " (O) turn :")
        else:
            pass
    if winner != "":
        print("\n\nGG " + winner + " is the winner")
        if winner.split()[0] == name1:
            score1 += 1
        elif winner.split()[0] == name2:
            score2 += 1
    print("\nScores: \n\n" + name1 + "\t-->\t" + str(score1) + "\n" + name2 + "\t-->\t" + str(score2) + "\n")  # print score of players
    again = input("Wanna Play Again ? (y/n):").lower()
    if again == ('n' or 'no' or 'non'):  # quit the game if the players don't want to play again
        break
    else:  # clear the screen and start again
        sp.call('cls', shell=True)

# print final score of players
print("\nGG Final Scores : \n\n" + name1 + "\t-->\t" + str(score1) + "\n" + name2 + "\t-->\t" + str(score2) + "\n")
