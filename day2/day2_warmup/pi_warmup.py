#!/usr/bin/env python3

"""
This program fixes errors present in the code snipped below 

#!/usr/env python3 <-- incorrect path

def main():
    pi= 3.14

    #no quotes in our strings below
    c= circumference 
    r= radius

    #multiple formatting errors in our string, replace concatenation with f-string
    print("To calculate the " + c + "of a circle, the formula is 2 x " + pi + " x " + " r " )

#no function call 
"""

def main():
    pi= 3.14
    c= "circumference"
    r= "radius"

    print(f"To calculate the {c} of a circle, the formula is 2 x {pi} x {r}" )
    # OUTPUT SHOULD READ AS:
    # To calculate the circumference of a circle, the formula is 2 x 3.14 x radius

main()
