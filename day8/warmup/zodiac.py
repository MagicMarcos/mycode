#!/usr/bin/env python3
'''Morning challenge: fix the wordy code to be more efficient and modular.'''

def main(): 
    '''take user input for name and birth year, match it to values in a list of dictionaries containing signs and print. '''
    
    # collect user name -> capitalize first letter of each word
    usr_name = input('Enter your name:\n> ').title()
    # collect birth year -> use into to convert to integer then use modulus to divide by 12
    # the remainder of the modulus function will return the index of the sign in the zodiac list
    year_mod = int(input('Enter your birth year in YYYY format, e.g. 2010\n> ')) % 12
    
    # list of dictionaries containing all zodiac signs
    zodiac_signs = [
        {'sign' : 'Monkey', 'description' : 'you are sharp, smart, curious, and mischievious.' },
        {'sign' : 'Rooster', 'description' : 'you are hardworking, resourceful, courageous, and talented.'},
        {'sign' : 'Dog', 'description': 'you are loyal, honest, cautious, kind, and a very good boy! Who\'s a good boy?! YES! It\'s you!'},
        {'sign' : 'Pig', 'description' : 'you are a symbol of wealth, honesty, and practicality.'},
        {'sign' : 'Rat', 'description' : 'you are artistic, sociable, industrious, charming, and intelligent.'},
        {'sign' : 'Ox', 'description' : 'you are strong, thorough, determined, loyal, and reliable.'},
        {'sign' : 'Tiger', 'description' : 'you are courageous, enthusiastic, confident, charismatic, and a leader.'},
        {'sign' : 'Rabbit', 'description' : 'you are vigilant, witty, quick-minded, and ingenious.'},
        {'sign' : 'Dragon', 'description' : 'you are talented, powerful, lucky, and successfull.'},
        {'sign' : 'Snake', 'description' : 'you are wise, like to work alone, and determined.'},
        {'sign' : 'Horse', 'description' : 'you are animated, active, and energetic.'},
        {'sign' : 'Sheep', 'description' : 'you are creative, resilient, gentle, mild-mannered, and shy.'},
    ]
    # store index of zodiac sign - mostly for readibility 
    zodiac = zodiac_signs[year_mod]

    # print results using fstring
    print(f"{usr_name} your zodiac sign is {zodiac['sign']}, you are {zodiac['description']}")

if __name__ == '__main__':
    main()

# ORIGINAL CODE 
#!/usr/bin/env python3

# def main():    
#     usr_name = input("Please enter your name:\n>") 
              
#     usr_name = usr_name.title()    
#     usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
            
#     if usr_date in [2011, 1999, 1987, 1975, 1963]:
#         print(f"{usr_name} your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.")
#     elif usr_date in [2020, 2008, 1996, 1984, 1972, 1960]:
#         print(f"{usr_name} your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.")
#     elif usr_date in [2010, 1998, 1986, 1974, 1962]:
#         print(f"{usr_name} your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.")
#     elif usr_date in [2021, 2009, 1997, 1985, 1973, 1961]:
#         print(f"{user_name} your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.")
#     elif usr_data in [2012, 2000, 1988, 1976, 1964]:    
#         print(f"{usr_name} your zodiac sign is Dragon, you are talented, powerful, lucky, and successfull.")
#     elif usr_date in [2013, 2001, 1989, 1977, 1965]:
#         print(f"{usr_name} your zodiac sign is Snake, you are wise, like to work alone, and determined.")
#     elif usr_date in [2014, 2002, 1990, 1978, 1966]:
#         print(f"{usr_name} your zodiac sign is Horse, you are animated, active, and energetic.")
#     elif usr_date in [2015, 2003, 1991, 1979, 1967]:
#         print(f"{usr_name} your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy.")
#     elif usr_date in [2016, 2004, 1992, 1980, 1968]:
#         print(f"{usr_name} your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.")
#     elif usr_date in [2017, 2005, 1993, 1981, 1969]:
#         print(f"{usr_name} your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.")
#     elif usr_date in [2018, 2006, 1994, 1982, 1970]:
#         print(f"{usr_name} your zodiac sign is Dog, you are loyal, honest, cautious, and kind.")
#     elif usr_date in [2019, 2007, 1995, 1983, 1971]:
#         print(f"{usr_name} your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.")


# main()