#!/usr/bin/env python3
# ^^^ originally python not python3

import sys
import time # time module  was not imported

def print1by1(text, delay=0.1):
    # there's nothing wrong with this function, it's just some cool code!
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def name_grabber(): #multiple indentation issues
    while True:
        try:
            name= input("What is your name?\n> ")
            num= input("Pick a number between 1 and 3:\n> ")
            if name and num in ["1","2","3"]:
                return name, num
        except:
            print("Bad input.")

def main():
    num_dict= {"1":"great","2":"awesome","3":"superb"} #missing }
    name, num= name_grabber()
    
    #missing "a"||"w" argument in open()
    with open("horoscope.txt", "w" ) as fileobj:
        fileobj.write(f"{name}, I predict today will be {num_dict[num].upper()}!\n")

    # not an error per se, but it's undesirable that
    # this gets written out with no spaces
    # fix the for loop to give a nicer output!
    for x in ["YOUR", "FUTURE", "HAS", "BEEN", "WRITTEN", "TO", "HOROSCOPE.TXT...\n"]:
        print1by1(x + " ") # add white space in between each word

#added main() function call
if __name__ == "__main__"
    main()
