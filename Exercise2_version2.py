"""
Step 1:
Write a Python script that construct a list of number with the help of
a text file that containes one number per line.

Step 2:
After having retrieved all the numbers, print the list.

Step 3:
The script will then compute and print the minimum, the maximum and the mean 
of the different numbers present in the list.

Step 4:
Compute the "truncated mean" of the elements: 
the mean of all elements except the smallest and largest ones.

Example:
    if the list is:
    [3,4,3,6,77,3,77,55,45,45]
    
    the truncated mean will only take into account the elements:
    [4,6,55,45,45] (3 and 77 are ignored)
"""

numbers=[]   # Creation of an empty list <=> numbers=list()

# Step 1:
myfile=open("values.txt")

for line in myfile:
    numbers.append(int(line))
     
print("Here is the constructed list:",numbers, "it's size is", len(numbers))

# Step 3:
   
if len(numbers) > 0:
    print(f"Minimum: {min(numbers)} Maximum: {max(numbers)}")    
    print(f"Mean: {sum(numbers)/len(numbers)}")
    # or
    import statistics
    print(f"Mean: {statistics.mean(numbers)}")
    
else:
    print("The list is empty")

# Step 4:

if len(numbers) > 0:
    mini=min(numbers)
    maxi=max(numbers)
    while mini in numbers:
        numbers.remove(mini) 
    while maxi in numbers:
        numbers.remove(maxi)
    print(f"Truncated mean is {sum(numbers)/len(numbers)}")  
else:
    print("The list is empty")