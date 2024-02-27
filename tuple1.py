
# Creation:

data=(2,3,4,6,7)
print(data)

data=2,True,None,7.8,"abc", [3,4,6]
print(data)

data=tuple([5,6,7])
print(data)

# len() for in not in [] [:] [::] + *

for e in data:
    print(e)

print(len(data), sum(data), min(data), max(data))

data=list(data)
data[0]=12
print(data)