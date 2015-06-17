#Import necessary modules.
import simplegui
import random
import math

#Declare global variables. 
secret_number = 0
number_range = 100
number_of_guesses = 0

"""New game function to start and also initialize
the number of guesses."""
def new_game():
    #Set number range.
    global secret_number
    secret_number = random.randrange(0,number_range)
    #Set number of guesses.
    global number_of_guesses
    number_of_guesses = int(math.ceil(math.log(number_range,2)))
    print "New Game. The selected range is from 0 to",number_range
    print "The number of guesses remaining is", number_of_guesses
    print ""
    pass

#Define 100 range for control.
def range100():
    global number_range
    number_range = 100
    new_game()
    pass

#Define 1000 range for control.
def range1000():
    global number_range
    number_range = 1000
    new_game()
    pass

#The main function.
def input_guess(guess):
    #Subtract one guess.
    global number_of_guesses
    number_of_guesses -= 1
    #Input number.
    number = int(guess)
    print "Guess was" , number
    #Compare input against secret number.
    if number == secret_number:
        print "Number of guesses remaining:",number_of_guesses
        print "Correct!"
        print ""
        new_game()
    elif number > secret_number:
        #Lose if less than 1 guess.
        if number_of_guesses < 1:
            print "Game Over. You ran out of guesses. The number was", secret_number
            print ""
            new_game()
        #Continue.
        else:
            print "Number of guesses remaining:",number_of_guesses
            print "Lower"
            print
            print ""
    else:
        #Lose if less than 1 guess.
        if number_of_guesses < 1:
            print "Game Over. You ran out of guesses. The number was", secret_number
            print ""
            new_game()
        #Continue.
        else:
            print "Number of guesses remaining:",number_of_guesses
            print "Higher"
            print ""
    pass

    
# create frame
frame = simplegui.create_frame("Guess",300,200)
frame.add_input("Enter Guess:",input_guess,50) 
frame.add_button("New Game",new_game,100)
frame.add_button("Range: 0 - 100",range100,200)
frame.add_button("Range: 0 - 1000",range1000,200)

# call new_game 
new_game()
frame.start()
