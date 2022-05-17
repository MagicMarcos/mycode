#!/usr/bin/env python3
"""print message wishing a happy day of the week to a user """

def main():
  # collect users name
  user_name = input("What is your name? ")

  #collect user input for weekday
  date_of_week = input("What day of the week is today? ")
  
  #print() message 
  print("Hello " + user_name + "! Happy " + date_of_week + "!")

main()

