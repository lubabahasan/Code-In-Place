<img align="left" src="Images/Karel's_Home.png" height="700">

```python
from karel.stanfordkarel import *

# The function should make Karel 
# move to the beeper, pick it up, and
# return home.

def main():
    for i in range (2):    #moves 2 steps
        move()
    for i in range (3):    #turn right
        turn_left()

    move()                
    turn_left()            #cut corner
    move()

    pick_beeper()          #pick beeper and
    for i in range (2):    #move back in position
        turn_left()
    for i in range (3):
        move()
    for i in range (3):
        turn_left()

    move()
    for i in range (3):
        turn_left()

if __name__ == '__main__':
    main()
```
