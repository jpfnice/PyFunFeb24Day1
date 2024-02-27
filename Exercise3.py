"""
Write a Python scripts that implements the “Guess the Number” game.

The script will generate of a random integral number (use the module random) from 1 to 100, and ask you to guess it.

The script will tell you if each guess is too high or too low.

You win if you can guess the number within six tries.
"""

import random

secret=random.randint(1,100)
 
# secret is the name of the variable
# that holds the number to guess

print(secret) # Just for testing purpose ...

currentNumberOfAttempts=0

while currentNumberOfAttempts < 6:

    currentValue=input("Enter an int in the range [1,100]: ")
    currentValue=int(currentValue)
    
    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
        break
    elif currentValue > secret:
        print("Too large !")
    elif currentValue < secret:
        print("Too small !") 
        
    #currentNumberOfAttempts = currentNumberOfAttempts + 1
    currentNumberOfAttempts += 1 # -= *= /=
    
if secret != currentValue:
    print("The secret number was:", secret)
