
nb1 = input("Give me a number: ")
nb1 = int(nb1)

"""
while boolean expression:
    statement 1
    statement 2
    ...

"""

while True :
    print("in the loop")
    print("nb1 is", nb1)
    nb1 = nb1 - 1
    if nb1 == 3:
        break
 
print("The end")
