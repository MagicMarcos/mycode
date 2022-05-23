#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

def api_lookup(url):
  res = requests.get(url)
  return res.json()

# finds character in API
def findchar():
    # api url for characters
    AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

    #prompt user for char number
    got_char_to_lookup = input("Pick a number between 1 and 1000 to get info on a GoT character!\n>")

    return api_lookup(AOIF_CHAR + got_char_to_lookup)

# finds house character belongs to 
def findhouse(got_char_dictionary):
    char_house = ""
    char_house_url = got_char_dictionary.get("allegiances")
    if len(char_house_url) != 0:
        # url to character allegiance (house) based on dictionary returned from findchar()
        char_house_info = api_lookup(char_house_url)
        char_house = char_house_info["name"]
    else: 
        print(0)
        char_house = "no house"

    return char_house

# find books character is featured in 
def findbooks(got_char_dictionary):
    books = ""
    # loop through books found in dictionary returned by findchar()
    for book_url in got_char_dictionary["books"]:
        
        book = api_lookup(book_url)

        # append each response to list
        books += book["name"] + ", "
    
    if got_char_dictionary.get("povbooks") != None:
        for book_url in got_char_dictionary.get("povbooks"):
            book = api_lookup(book_url)

            books += book["name"] + ", "
      
    return books
    

def main():
        # call function for character find
        got_char_dictionary = findchar()

        char_name = got_char_dictionary["name"]

        # find house character belongs to 
        char_house = findhouse(got_char_dictionary)

        #find books character is featured in
        char_books = findbooks(got_char_dictionary)

        print(f"{char_name} appears in {char_books}and is a member of {char_house}")

if __name__ == "__main__":
        main()
