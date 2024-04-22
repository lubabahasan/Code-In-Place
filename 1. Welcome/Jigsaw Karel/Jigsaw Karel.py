from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def main():
    #Karel moves 2 steps forward
    for i in range (2) :
        move()
    #Karel picks up the beeper
    pick_beeper()
    #Karel moves forward and turns
    move()
    turn_left()
    #Karel moves forward and places beeper
    for i in range (2) :
        move()
    put_beeper()
    #Karel moves back to the initial position
    for i in range (2) :
        turn_left()
    for i in range (2) :
        move()
    for i in range (3) :
        turn_left()
    for i in range (3) :
        move()
    for i in range (2) :
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()