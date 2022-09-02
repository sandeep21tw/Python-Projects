# In this file we are going to create a simple number guessing game
# by Sandeep

# will add the functionality to give the hint based on prime in special_hints method. (going to do it tomorrow)
# (cleaning the code)
import random

#number = random.randint(1, 10)

def introduction():
    print("Welcome to the game :)")
    print("In this game, your task is to guess a correct number")
    print("")
    selection = mode()
    if selection == "easy":
        print("You have to guess a number between 1 to 10")
        print("You have only three guesses to guess the number.")
    elif selection == "hard":
        print("You have to guess a number between 1 to 100")
        print("You have five guesses to guess a number")
        
    print("")
    # print("The one who guessed the right number will gets a reward")
    # print("What is the reward? You will get the link to my github profile(something like that) or maybe a cookie")

    #print("you will get two hints, one larger or smaller, other multiple or prime")

    return selection


def mode():
    print("Hey player which mode you wanna play this game on?")
    print("Type 'e' or 'easy' for 'Easy mode'")
    print("Type 'h' or 'hard' for 'Hard mode'")
    print("")

    selection = input("Enter wether you wanna easy mode or hard mode: ")
    print("")
    selection = selection.lower()

    if selection in ['e', 'easy']:
        print("Welcome to the easy mode")
        selection = "easy"               # for later use
    elif selection in ['h', 'hard']:
        print("Welcome to the hard mode! BWAHAHAHAH!")
        selection = "hard"
    else:
        print("================================")
        print("Invalid input. Please try again.")
        print("================================")
        print("")
        mode()           # i think this is a bad code coz it's kind of recursion.
        
    return selection



def hints(number, guess):
    if number < guess:
        print("Number is smaller than you guessed")
    elif number > guess:
        print("Number is larger than you guessed")
    else:
        print("something is wrong, (for debug purposes only), you shouldn't even be here coz of condition")


def special_hint(number, guess):
    # first special hint: (for now only 1, you could add more if you want.
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

    #print("you will get two hints, one odd or even, other multiple or prime")



def score(guesses):
    print("Your score is {0} percent".format(100/guesses))

def easy():
    number = random.randint(1, 10)
    guesses = 1
    while guesses < 4:
        guess = int(input("Enter a number: "))

        if number == guess:
            print("You guessed the right number :)")
            score(guesses)
            break
        else:
            hints(number, guess)
        guesses += 1
    else:
        print("You lose, Try again :(")

def hard():
    number = random.randint(1, 100)
    guesses = 1                     # starting from 1 to implement score func
    while guesses < 6:              # total 5 guesses
        guess = int(input("Enter a number: "))
        if number == guess:
            print("You guessed the right number :]")
            score(guesses)
            break
        else:
            print("Are you an idiot")
            print("Take a hint, dumb man")
            print("")
            hints(number, guess)
            if guesses == 4:
                print("Here's a special hint for you!")
                special_hint(number, guess)
        guesses += 1
    else:
        print("You lose, Try again :[")


def main():

    #number = random.randint(1, 10)
    
    selection = introduction()              # need to change this

    if selection == "easy":
        easy()
    else:
        hard()
    

    # i have used the while else. Read it about somewhere i dont'
    # whether it's a good to use it not :)






main()
