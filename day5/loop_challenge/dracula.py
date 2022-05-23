#!/usr/bin/env python3
    #""" The challenge: loop thorough dracula.txt, write out every line with 'vampire    ' (case-insensitive) to a new file called vampytime.txt and count out how many o    f those lines exist."""

vampirecount = 0 # counts how many lines contains vampire

# use with along with open so we don't need to close our file at the end 
with open("dracula.txt", "r") as draculafile: 
    vampirelower = "vampire" # lowercase vamp
    
   # loop through file
    for line in draculafile:

        # check if line contains either version of vampire
        if vampirelower in line.lower():
            
            vampirecount +=1 #increment count  
            
            #open a file passing in "a", so that if it doesn't exist we create one
            with open("vampytime.txt", "a") as vampfile:
                vampfile.write(line + "\n") #write out the line with "vampire"
    
    #write out how many times the word vampire appears
    print(f"The word 'vampire' appears {vampirecount} times")
                
