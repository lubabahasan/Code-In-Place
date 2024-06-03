"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""

def main():

    #variable to keep count
    count = 10

    #using a for loop to count
    for i in range (10):
        print(count)
        count = count-1

    #once out of the loop :
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()