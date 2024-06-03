import random

def main():
    #taking input of no. of sides
    sides = input("How many sides does your dice have? ")

    #converting to integer
    sides = int(sides)

    #generating a random number based on no. of sides
    roll = random.randint(1, sides)

    #printing a random number based on no. of sides
    print("Your roll is " + str(roll))

if __name__ == '__main__':
    main()