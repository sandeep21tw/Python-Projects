# This program is a simple rock, paper and scissor game
# by Sandeep

# NOTE: there is some error mentioned below and more about that is written in test.py program
# i have changed this work without error using global keyword but look for it why this error
# unboundlocalerror: local variable referenced before assignment (written more in test func)
# Refactor code


import random

# Variables are currently initialized here only. will later improve.

comp = 0
player = 0

option = ["rock", "paper", "scissors"]
option_logic = {"rock":"paper", "paper":"scissors", "scissors":"rock"}

def win(cm, pm):
    # cm stands for computer move and pm stands for player move
    global player, comp
    
    if pm == cm:
        print("Tie")

    # passing player move in dict will give us what we need to win against the player and if
    # the computer move is that what we needed then computer wins!
    
    elif option_logic[pm] == cm:
        print("Computer win this time :(")
        comp = comp + 1
        
    elif option_logic[pm] != cm:
        print("You won this time :)")
        player = player + 1
    else:
        print("Something went wrong.")


def moves_parse(pm):
    simple_logic_dict = {
        "r":"rock",
        "s":"scissors",
        "p":"paper",
        "q":"quit",
        "reset":"reset",
        "h":"how"
        }
    if pm in simple_logic_dict:
        move = simple_logic_dict[pm]
    elif pm in option:
        move = pm
    else:
        move = "Invalid move"

    return move

def play():
    while True:
        pm = input("Choose your move: 'r', 'p', 's': ")
        pm = pm.lower()
        pm = moves_parse(pm)

        cm = random.choice(option)

        if pm == "quit":
            print("Ok bye!")
            winner()
            break
        elif pm == "how":
            how()
        elif pm == "reset":
            reset()
        elif pm != "Invalid move":
            print("You choose {0}!".format(pm))
            print("Computer chooses {0}!".format(cm))
            win(cm, pm)
        else:
            print("That's an invalid move! Try again")
        print("")


def reset():
    # implemented in play!
    winner()
    r = input("Do you wanna reset the game? ")
    if r == "y" or r == "yes":
        print("Game is resetted!")
        global player, comp
        player = 0
        comp = 0
    else:
        print("Continuing the game!")

def how():
    # implemented in play
    print("")
    print("Rock will win against scissors")
    print("Scissor will win against paper")
    print("paper will win against rock")
    print("Rock > Scissors")
    print("Scissors > Paper")
    print("Paper > Rock")



def winner():

    print("Computer score is {0}".format(comp))
    print("Your score is {0}".format(player))
    print("")

    
    if player > comp:
        print("Yay! You won :)")
    elif player < comp:
        print("Computer won this time :(")
    else:
        print("It's a Tie!")


def intro():
    print("Hello! Welcome to the game of rock, paper and Scissors!")
    print("You opponent is computer")
    print("")
    print("Let me tell you a little guide!")
    print("")
    print("You could either type rock, paper, scissors in full or just type 'r' for rock, 'p' for paper and 's' for scissors")
    print("You could type 'q' to quit the game")
    print("After the quit the game, score card will be revealed!")
    print("")
    

def main():
    intro()
    play()


main()
