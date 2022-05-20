#!/usr/bin/env python3

def question1(houses):
    print("Question1:  \nYou would be most hurt if a person called you... \n" +
                "1. boring \n" +   #gryffindor
                "2. unkind \n" +   #hufflepuff
                "3. ignorant \n" + #ravenclaw
                "4. weak")         #slytherin

    answer1 = input("\nYour answer: ")

    if answer1 == "1":
            houses["Gryffindor"] += 1
    elif answer1 == "2":
            houses["Hufflepuff"] += 1
    elif answer1 == "3": 
            houses["Ravenclaw"] += 1
    elif answer1 == "4":
            houses["Slytherin"] += 1
    else:
        print("\nThe sorting hat is angry that you have not chosen an appropriate answer! Please pick 1-4")
        question1(houses)

if __name__ == "__question1__":
    question1(houses)

#Second question
def question2(houses):
    #Print question
    print("\nQuestion2: You're locked in a duel with a skilled opponent. They fire an unknown spell at you, and you shout… \n" +
                "1. Expelliarmus! \n" + #hufflepuff
                "2. Protego! \n" +      #ravenclaw
                "3. Stupefy! \n" +      #gryffindor
                "4. Crucio!")           #slytherin
    
    #collect user answer
    answer2 = input("\nYour answer: ")
    
    #assign value to house matching user answer
    if answer2 == "1":
        houses["Hufflepuff"] += 1
    elif answer2 == "2":
        houses["Ravenclaw"] += 1
    elif answer2 == "3":
        houses["Gryffindor"] += 1
    elif answer2 == "4":
        houses["Slytherin"] += 1
    else:
        print("\nYou're upsetting the sorting hat dude! Pick a number 1-4")
        question2(houses)

if __name__ == "__question2__":
    question2(houses)

#Third Question        
def question3(houses):
    #Print question for user
    print("\nQuestion3:  \nIt's your fifth year at Hogwarts, and you've just received a Howler from your parents. What for? \n" +
                "1. Sneaking into the Forbidden Forest at night on a dare. \n" +                  #gryffindor
                "2. Getting caught cheating in my Divination O.W.L. \n" +                         #slytherin
                "3. Being put in detention after I was caught in the library after hours. \n" +   #ravenclaw
                "4. Nothing! I'd never do anything to warrant a Howler.")                         #hufflepuff
    
    #Collect user response
    answer3 = input("Your answer: ")

    #Conditional logic assigns points to the house corresponding to user answer
    if answer3 == "1":
        houses["Gryffindor"] += 1
    elif answer3 == "2":
        houses["Slytherin"] += 1
    elif answer3 == "3":
        houses["Ravenclaw"] += 1
    elif answer3 == "4":
        houses["Hufflepuff"] += 1
    else: 
        print("\nI don't even know what to tell you dude... It's 1,2,3 or 4. The hats losing his cool!")
        question3(houses)

if __name__ == "__question3__":
    question3(houses)

#Fourth question
def question4(houses):

    #print question for user
    print("\nQuestion4:  \nWhich of your skills are you most proud of? \n" +
                "1. My ability to absorb new information. \n" + #ravenclaw
                "2. My ability to make new friends. \n" +       #gryffindor
                "3. My ability to get what I want. \n" +        #slytherin
                "4. My ability to keep secrets.")               #hufflepuff
    
    #Collect user response
    answer4 = input("Your answer: ")
    
    #Conditional logic assings points to the corresponding house 
    if answer4 == "1":
        houses["Ravenclaw"] += 1
    elif answer4 == "2":
        houses["Gryffindor"] += 1
    elif answer4 == "3":
        houses["Slytherin"] += 1
    elif answer4 == "4":
        houses["Hufflepuff"] += 1
    else: 
        print("\nBruh... 1...2...3...4... IT'S NOT HARD!")
        question4(houses)

if __name__ == "__question4__":
    question4(houses)

#question to be asked if there are ties in the scoring system 
def finalquestion(housechoices):
    
    housestring = " or ".join(housechoices)
    
    #print(f"A rare opportunity appears before you! I seems the sorting hat can't quite place you... Out of the kindness of his heart and because he wants to get this ceremony over with, he will give you a choice. These are the houses he lays before you: {housestring}. Type in the name of the house you'd like to join: ")

    answer = input("\nYour answer: ")
    answer = answer.lower().capitalize()
    

    if answer in housechoices:
        print("DEBUG_FINALQUESTION_ANSWER:" ,answer)
        return answer
    else:
        print(f"\nThis is a rare opportunity! Don't play games! Your choices are {housestring}. Pick fast!!!")
        finalquestion(housechoices)

if __name__ == "__finalquestion__":
    finalquestion(housechoices)
