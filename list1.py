
# Creation:

alist=[2,3,4,6,7]
print(alist)

alist=[2,True,None,7.8,"abc", [3,4,6]]
print(alist)

alist=list()
print(alist)

alist=[]
print(alist)

alist=list("abdef")
print(alist)

# len() for in not in [] [:] [::] + *

# to update a list:
print(alist)
alist.append(10)
print(alist)
alist.insert(0,20)
print(alist)
alist.pop(1)
print(alist)
alist.remove('b')
print(alist)
alist.pop()
print(alist)
alist[2]=45
print(alist)
alist[2:4]=[0]
print(alist)

data=[2,3,[4,5,2]]
data.remove(2)
print(data)

data=[6,3,[4,5,2]]
if 2 in data:
    data.remove(2)
print(data)

data=[2,3,4,5,2]
print(data, len(data))
data.append([10,11,12])
print(data, len(data))

data=[2,3,4,5,2]
print(data, len(data))
data.extend([10,11,12])
print(data, len(data))

#data.sort()
#print(data)
data=[2,3,4,5,2]
print(data)
result=sorted(data)
print(data)
print(result)