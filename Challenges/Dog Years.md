<img align="left" src="Images/Dog_Years.png" height="500">

```python
# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    #taking input
    years = input("Enter an age in calendar years: ")
    
    #converting to integer
    years = int(years)

    #calculating dog years
    years = years*DOG_YRS_MULTIPLIER

    #printing dog years
    print("That's "+ str(years) +" in dog years!")

if __name__ == '__main__':
    main()
```
