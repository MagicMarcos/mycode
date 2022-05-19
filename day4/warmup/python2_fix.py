#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.


def add(num1,num2):
    print("\n" + str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    
def sub(num1,num2):
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))

def main():
    #calc1 = ""
    # calc2 = ""
    while True:
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input("Your answer: ")
        calc1.lower()
        if calc1 == "q":
            break
        try:
            calc1 = float(calc1)
        except:
            print("Invalid entry. Restarting")

        # Second operation
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input("Your answer -> ")
        calc2.lower()

        if calc2 == "q":
            break
        calc2 = float(calc2)
        
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input("Your answer -> ")

        if operation == "+":
            add(calc1,calc2)
            break
        elif operation == '-':
            sub(calc1,calc2)
            break
        else:
            print("\n Not a valid entry. Restarting...")
main()

