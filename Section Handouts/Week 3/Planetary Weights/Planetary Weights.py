"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

def main():
     
    #taking weight input
    earth_weight = int(input("Enter a weight on Earth : "))
    
    #taking planet input
    planet = input("Enter a planet : ")

    if( planet == "Mercury"):
        gravity = 0.376
    elif( planet == "Venus"):
        gravity = 0.889
    elif( planet == "Mars"):
        gravity = 0.378
    elif( planet == "Jupiter"):
        gravity = 2.36
    elif( planet == "Saturn"):
        gravity = 1.081
    elif( planet == "Uranus"):
        gravity = 0.815
    else:
        gravity = 1.14
    
    #equivalent weight on other planet
    eq_weight = float(gravity)*earth_weight

    #rounding up the value
    eq_weight = round(eq_weight, 2)

    #printing equivalent weight
    print("The equivalent weight on " + planet + " : "+ str(eq_weight))

    pass

if __name__ == "__main__":
    main()