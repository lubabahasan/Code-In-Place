from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.

def main():
    for i in range (2):
        move()
    for i in range (3):
        turn_left()

    move()
    turn_left()
    move()

    pick_beeper()
    for i in range (2):
        turn_left()
    for i in range (3):
        move()
    for i in range (3):
        turn_left()

    move()
    for i in range (3):
        turn_left()
    
# don't edit these next two lines
# they tell python to run your main function

if __name__ == '__main__':
    main()