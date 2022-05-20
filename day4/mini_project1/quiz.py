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
    
    
    #find highest value in houses dictionary
    highest = max(houses.values())
    
    #list eventually contains users potential houses based on their values from houses dictionary
    housechoices = []
    
    #loop through houses dict and populate housechoices list with highest values from dict
    for house in houses:
        
        if houses[house] == highest:
            housechoices.append(house)
    
    #ultimately, the house a user ends up joining
    house = ""
    
    #if theres only one house in housechoices, then there are no ties and user is placed
    if len(housechoices) == 1:
        house = housechoices[0]
    else: #if there are multiple potential houses (ties) 
        
        #string from potential houses
        housestring = " or  ".join(housechoices)
        
        #prompt user with a tie breaker question
        print(f"\nA rare opportunity appears before you! It seems the sorting hat can't quite place you... He give you a choice! These are the houses he lays before you: {housestring}. Type in the name of the house you'd like to join: ")
       
        #invoke final question, giving user the choice of which house they want to be in and assign to house
        house = finalquestion(housechoices)
        print("DEBUG_HOUSE: ", house)
    
    #print the users result
    print(f"\n The sorting hat has decided... You belong to {house}!!!!")

    print("\nDEBUG_HOUSES_TOTAL: ", houses)

if __name__ == "__main__":
    main()
