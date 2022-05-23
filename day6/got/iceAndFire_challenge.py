#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

# finds character in API
def findchar(): 
    # api url for characters
    AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/" 
    
    #prompt user for char number
    got_char_to_lookup = input("Pick a number between 1 and 1000 to get info on a GoT character!\n>")
    
    # get json result from API
    gotresp = requests.get(AOIF_CHAR + got_char_to_lookup)

    #parse the response from get request
    got_dj = gotresp.json()

    #prin out response to console
    pprint.pprint(got_dj)

    #return chacter information dictionary
    return got_dj

# finds house character belongs to 
def findhouse(got_dj):
    # url to character allegiance (house) based on dictionary returned from findchar()
    char_house_url = got_dj["allegiances"][0]

    # get json result from API
    char_house_res = requests.get(char_house_url)

    #pare response from get request
    char_house = char_house_res.json()

    #print requested information
    print(f"House:  {char_house['name']}")

# find books character is featured in 
def findbooks(got_dj):
    # list containing books all books 
    books = []
    
    # loop through books found in dictionary returned by findchar()
    for book_url in got_dj["books"]:
        # get json from API
        book_res = requests.get(book_url)

        # parse response from get request
        book = book_res.json()

        # append each response to list
        books.append(book["name"])
    
    # print list containing all books 
    print(f"Books: {books}")

def main():
        # call function for character find
        got_dj = findchar()
        
        # find house character belongs to 
        findhouse(got_dj)

        #find books character is featured in
        findbooks(got_dj)
        
if __name__ == "__main__":
        main()
