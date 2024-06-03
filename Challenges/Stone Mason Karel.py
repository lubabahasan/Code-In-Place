from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def move_up() :
    while front_is_clear() :
        move()
    turn_right()
    if front_is_clear() :
        move()
        turn_left()

def build_pillar() :
    while(front_is_clear()) :
        if no_beepers_present() :
            put_beeper()
        move()
    if no_beepers_present() :
        put_beeper()

def turn_right() :
    for i in range (3) :
        turn_left()
        
def look_for_arch() :
    while front_is_clear() :
        turn_right()
        move()
        turn_left()
    turn_left()
    turn_left()
    

def main():
    turn_left()
    build_pillar() 
    turn_right()
    move()
    turn_left()

    while front_is_clear() :
        look_for_arch()
        build_pillar()
        turn_left()
        if front_is_clear() :
            turn_left()
            move_up()
    

if __name__ == '__main__':
    main()