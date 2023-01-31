# can also create lists using constructor "list()"
myList = []
anotherList = list()

for i in range(0, 100):
    myList.append(i)
    
print("myList: " + str(myList))
print("Length of list: " + str(len(myList)))
print("Type of list: " + str(type(myList)))

# There are 4 collection data types in Python
# lists
# tuples
# sets
# dictionaries

print("myList[25] = " + str(myList[25]))
print("myList[-1] = " + str(myList[-1]))
print("myList[43:70] = " + str(myList[43:70]))

if 89 in myList:
    print("89 is in myList")
else:
    print("89 is not in myList")
    
if 101 in myList:
    print("101 is in myList")
else:
    print("101 is not in myList")
    
for i in range(100, 200):
    # Add an item to the end of the list.
    anotherList.append(i)
    
print("anotherList: ")
print(anotherList)

# Extend the list by appending all the items from the iterable.
myList.extend(anotherList)
print("myList extended with anotherList: " + str(myList))

# Insert an item at a given position. 
myList.insert(0, 'x')

# Remove the first item from the list whose value is equal to x.
myList.remove('x')