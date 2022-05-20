#!/usr/bin/env python3
"""A simple quiz game to determine which HarryPotter house you belong to"""

from questions import question1, question2, question3, question4, finalquestion

def main():
    #short description telling the user about the game
    print("You've arrived at your sorting ceremony in Hogwarts. The sorting hat asks you a series of questions. Answer truthfully by typing in the number corresponding to your answer and it will decide which house you belong to.\n")
    
    #dictionary containing possible houses and the current count from each answer
    houses = {
            "Ravenclaw"  : 0,
            "Slytherin"  : 0,
            "Gryffindor" : 0,
            "Hufflepuff" : 0
            }
    
    #loop that serves as the core of our game, prompting user with questions
    while True:
        # question 1
        question1(houses)

        #question2
        question2(houses)

        #question3
        question3(houses)

        #question4
        question4(houses)
        
        break #break out of loop when last question is asked
    
    #loop through dictionary of houses to determin the winner
    highest = max(houses.values())

    housechoices = []

    for house in houses:
        
        if houses[house] == highest:
            housechoices.append(house)
    
    house = ""

    if len(housechoices) == 1:
        house = housechoices[0]
    else:
        housestring = " or  ".join(housechoices)

        print(f"\nA rare opportunity appears before you! It seems the sorting hat can't quite place you... He give you a choice! These are the houses he lays before you: {housestring}. Type in the name of the house you'd like to join: ")
       
        house = finalquestion(housechoices)
        print("DEBUG_HOUSE: ", house)
      
    print(f"\n The sorting hat has decided... You belong to {house}!!!!")

    print(houses)

main()
