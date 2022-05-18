#!/usr/bin/env python3
"""User inputs a number that corresponds to a value in a superhero dictionary """

def main():

    #superhero dictionary
    ProfessorX={'name':'Professor Charles Xavier',
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
            'creator':['Stan Lee','Jack Kirby'],
            'bio':'Professor X (Professor Charles Xavier) is the founder of the superhero team The X-Men in the Marvel Universe and an incredibly powerful mutant hero.'}

    #get keys related to professor x
    pxkeys = ProfessorX.keys()
    
    #keep count to enumerate keys in keydict
    count = 0
    
    #dictionary of ProfessorX keys
    keydict = {}
    
    #loop through dictionary, incrementing count, populating keydict, printing ProfessorX key value pairs
    for key in pxkeys:
        count = count + 1
        keydict[str(count)] = key
        print(f"{count}: {key}")
   
    #add a space for looks
    print("\n")
    
    #prompt user
    userinput = input("Using the legend above, select what you'd like to learn about Professor X \n>")
    
    #get value from keydict based on user input
    xkey = keydict.get(userinput, "Not found...")

    #use value in xkey to get the actual value we need in ProfessorX
    result = ProfessorX.get(xkey, "We do not currently have that information")

    #print answer to user input
    print(f"{xkey}, {result}")

main()
