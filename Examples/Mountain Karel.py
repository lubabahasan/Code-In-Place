from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size
and plants a beeper at the top
"""

def main():
    #Karel climbs mountain until she reaches the top
    #where the front is clear
    while(front_is_blocked()):
        climb_mountain()

    #puts beeper at the top
    put_beeper()

    #climbs down until a wall is reached
    while(front_is_clear()):
        descend_mountain()
    

def climb_mountain() :
    #pre : Karel at the base
    #pre : Karel facing East

    #Karel faces North
    turn_left()

    #moves up/North
    move()

    #faces East
    turn_right()

    #moves forward
    move()
        
def descend_mountain():
    #pre : Karel at the top
    #pre : Karel facing East

    #Karel moves forward
    move()

    #Karel faces South
    turn_right()

    #Karel moves down/South
    move()

    #Karel faces East
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()