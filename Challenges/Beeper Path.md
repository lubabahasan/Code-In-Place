<img align="left" src="Images/Beeper_Path.png" height="520">

```python
from karel.stanfordkarel import *

def main():
    #Karel moves until beeper found
    while beepers_present() :
        move()


if __name__ == '__main__':
    main()
```
