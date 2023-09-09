import simplegui
import random
import math

# helper function to start and restart the game
highest = 101
attempts = 0
max_guesses = 7
guesses_remaining = max_guesses - attempts

def new_game():
    global secret_number
    global highest
    global attempts 
    global guesses_remaining
    attempts = 0
    secret_number = random.randrange(0, highest)
    print()
    print ("New game. Range is [0, " + str(highest - 1) + "]")
    print (str(max_guesses) + " guesses remaining")

    
def range100():
    global secret_number
    global highest
    global max_guesses
    max_guesses = 7
    highest = 101
    new_game()


def range1000():
    global secret_number
    global highest
    global max_guesses
    max_guesses = 10
    highest = 1001
    new_game()  

def input_guess(guess):
    guess_int = int(guess)
    global attempts
    global guesses_remaining
    global max_guesses
    attempts += 1
    guesses_remaining = max_guesses - attempts
 
    print ("Guess was " + guess)
    print (str(guesses_remaining) + " guesses remaining")
    
    if guess_int == secret_number:
        print ("Correct. You Win!")
        new_game()
    elif attempts >= max_guesses:
        print ("No more guesses. You lose")
        print ("The answer was " + str(secret_number))
        new_game()
               
    elif guess_int > secret_number:
        print ("Guess lower")
    elif guess_int < secret_number:
        print ("Guess higher")
    else:
        print ("Input error")

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 400)
frame.add_input("Guess", input_guess, 200)

# register event handlers for control elements and start frame
frame.add_button("Range 100", range100, 200)
frame.add_button("Range 1000", range1000, 200)
frame.add_button("New game", new_game, 200)


# call new_game 
new_game()
frame.start()

