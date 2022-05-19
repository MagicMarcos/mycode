#!/usr/bin/env python3
"""Guessing program utilizing conditionals"""

def main():
    """Code containint conditional logic for our game"""
    
    # count for each iteration of our loop
    round = 0
    
    #answer as a blank string - initialize here to make while loop work
    answer = ""

    #infinite loop 
    while round < 3 and (answer != "brian" and answer != "shrubbery") :
        
        #increment round
        round += 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        # prompt user for their guess
        answer = input("Your guess \n> ")
        
        # normalize casing 
        answer = answer.lower()
        
        #Conditional logic to check if user answered correctly 
        if answer == "brian": # normalize case and check against "Brian
            print("Correct!")

        elif answer == "shrubbery": # logic for super secret answer
            print("You gave the super secret answer!")
            
        elif round == 3 :             # ensure round is not yet 3 (game over)
            print("Sorry, the answer was Brian.")

        else:                         # logic for if wrong answer was given
            print("Sorry, try again!")


main()
