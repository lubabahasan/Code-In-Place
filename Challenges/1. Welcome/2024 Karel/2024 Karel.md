<img align="left" src="2024_Karel.png" height="550">

```python
from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 24 beepers, and end facing East to 
the right of the 24 beepers.
"""

def main():
    #Karel puts beeper down 20 times and moves forward
    for i in range (20) :
        put_beeper()
    move()
    #Karel puts beeper down 24 times and moves forward
    for i in range (24) :
        put_beeper()
    move()

if __name__ == '__main__':
    main()
```
