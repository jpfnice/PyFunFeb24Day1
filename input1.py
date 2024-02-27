
nb1 = input("Give me a number: ")
nb1 = int(nb1)

"""
if boolean expression:
    statement 1
    statement 2
    ...
elif boolean expression:
    statement 1
    statement 2
    ...
elif boolean expression:
    statement 1
    statement 2
    ...
else:
    statement 1
    statement 2
    ...
"""
#  bool operator: > < >= <= == != and or not
if nb1 > 10 :
    print("condition satisfied")
    print("End of the if block")
elif nb1 == 8 :
    print("second condition")
elif nb1 == 5 :
    print("third condition")
else:
    print("In the else block")
    
print("The end")

