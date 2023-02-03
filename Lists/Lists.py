# can also create lists using constructor "list()"
myList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
anotherList = list(("N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"))


# List Attributes
print("myList: " + str(myList))
print("Length of list: " + str(len(myList)))
print("Type of list: " + str(type(myList)))


# Accessors
print(f"myList[2] = {myList[2]}")
print(f"myList[-1] = {myList[-1]}")
print(f"myList[4:7] = {myList[4:7]}")



letter = "G"
if letter in myList:
    print(f"{letter} is in myList")
else:
    print(f"{letter} is not in myList")



print(f"anotherList: {str(anotherList)}")
# Extend the list by appending all the items from the iterable.
myList.extend(anotherList)
print(f"myList extended with anotherList: {str(myList)}")


# Insert an item at a given position. 
myList.insert(0, 'x')
print(f"myList inserted 'x' at index 0: {str(myList)}")



# Remove the first item from the list whose value is equal to x.
myList.remove('x')
print("myList removed 'x': " + str(myList))


# Pop (remove) element from list, no parameter means remove ending
myList.pop(1)
myList.pop()
print("myList popped item at index 1 and at the end: " + str(myList))



del myList[13]      # equivalent to myList.pop(13)
del anotherList     # anotherList no longer defined
print(f"myList removed item at index 13: {str(myList)}")


# returns the number of specified parameter in the list
print(f"Number of Cs in myList: {str(myList.count('C'))}")