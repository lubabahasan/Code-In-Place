"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")

    #taking numbers as inputs
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(num1*num2)



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()