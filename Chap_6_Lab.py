# Program simulates a dice game.
# It asks the user to enter player names,
# then will roll a die for each player.
# The player with the higher roll wins.

import random

def get_player1_name():
    player1 = input("Enter Player 1's name: ")
    return player1

def get_player2_name():
    player2 = input("Enter Player 2's name: ")
    return player2

def dice_game(player1, player2):
    player1_roll = random.randint(1, 6)
    print(player1, " rolled a ", player1_roll)
    player2_roll = random.randint(1, 6)
    print(player2, " rolled a ", player2_roll)
    if player1_roll > player2_roll:
        print(player1, " wins!")
    elif player1_roll < player2_roll:
        print(player2, " wins!")
    else:
        print("It's a tie.")

player1 = get_player1_name()
player2 = get_player2_name()
dice_game(player1, player2)

