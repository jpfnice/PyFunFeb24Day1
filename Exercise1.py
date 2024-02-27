'''
Write a Python script that prompts the user for a number and displays a message that does indicate if the number is odd or even.

You can use % 2 to check if the number is even or not

Note: do consider 0 has being neither odd nor even.
This means they are 3 possible situations:
    the number entered is 0
    the number entered is even (number % 2 == 0)
    the number entered is odd (number % 2 == 1)
    
After having tested a first number, the script should prompt the user for other numbers as long as he or she would like to.
You could use a while loop to prompt the user for a new number as long as he or she would like to

'''

while True:
    nb=input("Please enter a number: ")
    
    nb=int(nb)
    
    if nb == 0:
        print(nb,"is neither even nor odd !")
    elif nb % 2 == 0:
        print(nb,"is even")
    else:
        print(nb,"is odd")

    answer=input("Do you want to continue (Y or N) ?")
    if answer != "Y" and answer != "y":
        break
    
print("The end")

