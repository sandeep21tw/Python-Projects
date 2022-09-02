# This program is just a simple word guessing game
# by Sandeep

# To do: It sort of works now!
# Important step: NEED IT! DO IT LATER refactor code (mayebe on sunday)
# Now, move everything below and write the code again (next task)
# sort of need to refactor the code a little more, otherwise works fine!

# Give the user +2 chances the length of word (for ex: if game word is selected,
# then chances given should be 6)
# You may to change the code to show how many letter are there in a word first
# (otherwise user may say that we have cheated)
# test the code for any bugs:
#    - bug present, if a  user type a word: then it should check if that
#       guess word is equal to actual word or not. currently, it iterates
#       over a word and update the guessed_word list, which is causing this
#       behaviour.



"""
#  DONE:
-prints how many chances a user has taken ...
-add the functionality so that if the user types the full word then it prints success
-add a message if user can't guess the word right
-Also , You can further enhance program by adding timer after every Guess
-ohhh, definately gonna implement above point to make it more intersting.
-will refactor it later...(maybe on sunday + also add above chance feature)
"""


import random
import time

def introduction():
    name = input("Hey! What's your name? ")
    print("")
    print("Hey, {0}! This is a simple word guessing game.".format(name))
    print("You will be given 12 chances to guess the word.")


def word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks', 'elon', 'rockets',
             'commerce', 'amazon', 'twitter', 'facebook', 'reddit',
             'covid19', 'license', 'language', 'game', 'youtube',
             'google', 'alphabet', 'microsoft']

    word = random.choice(words)
    return word


word = word()
#chances = 12
guessed = ["_" for i in range(len(word))]      # for tracking how many letter the user have guessed


def update_guessed(word, guess):
    # This function updates the guessed list according to PROPER LETTER POSITION(PROPER INDEX) in a word.
    index = 0
    for letter in word:
        if letter == guess:
            guessed[index] = guess
        index += 1
        


    
    
#print(word)

def taking_guess():
    # This program takes the user guess.
    # This program return the user guess and time taken by user to enter guess.

    t1 = time.time()

    guess = input("Enter the word or the letter(you think present in word): ")
    guess = guess.lower()

    t2 = time.time()

    time_taken = t2 - t1        # in seconds
     
    return guess, time_taken


def game_logic(word, guess):
    if len(guess) >= 1:
        """
        iterating over each letter and then updating
        Note: need to update game logic, based on above bugs(see in the top section)
        i think it is easy to do: FIXED IN BELOW game_logic1 function.
        """   
        for guess_letter in guess:
                if guess_letter in word:
                    update_guessed(word, guess_letter)
    else:
        print("Invalid response")
        


def game_logic1(word, guess):
    if len(guess) > 1:
        if guess == word:
            for guess_letter in guess:
                update_guessed(word, guess_letter)
        else:
            print("\nYou have guessed the wrong word.")
    else:
        if guess in word:
            update_guessed(word, guess)


def game(word):
    chances = 12
    print(" ".join(guessed))
    while chances > 0:
        """
        # time in starting of game(necessary to calculate time taken by user)
        t1 = time.time()

        

        guess = input("Enter the word or the letter(you think present in word): ")
        guess = guess.lower()

        # time taken after a user enters a word! (necessary to calculate the  time taken by user)
        # we need to calculate how much time does a user take in thinking and typing the word in prompt

        t2 = time.time()

        """

        guess, time_taken = taking_guess()
        
        # This if else checks whether the time taken by user is less 10 sec or not
        # if yes then continue the game else, stop the game.
        if time_taken < 10:
            """
            if len(guess) >= 1:
                # iterating over each letter and then updating
                for guess_letter in guess:
                    if guess_letter in word:
                        update_guessed(word, guess_letter)
            else:
                print("Invalid response")
            """
            game_logic1(word, guess)
                
        else:
            print("You took too much time!")
            break
        
        # You could enclose this in a function below lines.

        print(" ".join(guessed))
        print("\n")
        
        if word == "".join(guessed):
            print("You succesfully guessed the word :)")
            break
        else:
            print("You have {0} chances left.".format(chances))
        
        chances -= 1
        
        
    else:
        print("You failed to guess the correct word :(")


def main():
    introduction()
    game(word)

main()














"""                

while chances > 0:

    if word == "".join(guessed):
        print("You succesfully guessed the word")
        break

    
    guess = input("Enter your guess letter(only single letter): ")
    guess = guess.lower()

    if len(guess) > 1:
        for guess_letter in guess:
            if guess_letter in word:
                # this code is for updating the guessed list so that result can be showin on screen
                
                index = 0
                for i in word:
                    if i == letter:# and guessed[index] == "_":
                        guessed[index] = letter
                    index += 1
                
                update_guessed(word, guess_letter)
    

    if guess in word:
        print("")
        print("Your guess letter is in the word")

        # enclose below till index increment into a function
        # this code actually track the index and see if guess = word on
        # that and changed the guessed variable accordingly
        
        index = 0
        for i in word:
            if guess == i:# and guessed[index] == "_":
                guessed[index] = guess
            
            index += 1
        
        update_guessed(word, guess)
            
        
        #guessed_index = word.index(guess)
        #guessed[guessed_index] = guess
    else:
        print("Not present in word")
 

    print(" ".join(guessed))
    print("\n")

    chances -= 1





alright! what we want is
__t__

but this loop is not okay i guess for that


"""
