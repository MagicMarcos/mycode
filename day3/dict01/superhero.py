#!/usr/bin/env python3
"""Returns information on Professor X based on user input. """


def main():

    #dictionary containing information on ProfessorX
    ProfessorX={
            'name':'Professor Charles Xavier',
            'aliases':[
                'Professor X',
                'Onslaught',
                'Consort-Royal',
                'Founder',
                'X',
                'Warlord',
                'Entity'
                ],
            'base of operations':'Salem Center, New York',
            'creator':[
                'Stan Lee',
                'Jack Kirby'
                ],
            'bio':'Professor X (Professor Charles Xavier) is the founder of the superhero team The X-Men in the Marvel Universe and an incredibly powerful mutant hero.',
            }

    #add new item to superhero dictionary
    ProfessorX["favorite food"] = "burritos"
    
    #print out keys
    print(f"Here's our current knowledge on Professor X: \n{ProfessorX.keys()}")

    #get user input 
    choice = input("what would you like to know about Professor X? \n>")
    
    #print result
    print( ProfessorX.get(choice, "Sorry but we don't have that information"))

main()
