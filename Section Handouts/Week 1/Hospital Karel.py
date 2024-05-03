from karel.stanfordkarel import *

# Here is a place to program your Section problem

def turn_right():
    for i in range (3):
        turn_left()

def build_tower():
    #pre : beeper present
    #pre : Karel facing East

    #Karel has to face North
    turn_left()

    #Karel builds half of a tower
    for i in range (2) :
        move()
        put_beeper()

    #Karel has to face East
    turn_right()

    #Karel moves forward
    move()

    #places a beeper for the second half of the tower
    put_beeper()

    #Karel has to face South now
    turn_right()

    #Karel builds the second half of the tower
    for i in range (2) :
        move()
        put_beeper()

    #Karel should be facing East
    turn_left()

def main():
    #Karel will carry out this task
    #until a wall is reached
    while front_is_clear():

        #upon finding a beeper
        if beepers_present() :

            #Karel builds a tower
            #pre : facing East
            #post: facing East
            build_tower()

        #After building tower, if wall not reached,
        #Karel continues ahead
        if front_is_clear() :
            move()
        


if __name__ == '__main__':
    main()