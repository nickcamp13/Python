# Dictionaries are used to store date values in
# key:value pairs
# It is a collection that is ordered, changeable, and do NOT allow duplicates
# Values in a dictionary can be any data type


# Initialize a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# Can also initialize a dictionary using constructor
anotherdict = dict(thisdict)

# You can print the entire dictionary
print(thisdict)

# Print the value of a specific key
print(thisdict["brand"])

# Using .get() to access values of keys
x = thisdict.get("model")
print(x)

# Print number of pairs in the dictionary
print(len(thisdict))

# dictionaries are their own type
print(type(thisdict))

# .keys() returns a list of the keys in the dictionary
print(thisdict.keys())

# .values() returns a list of the values in the dictionary
print(thisdict.values())

# .items() returns a list of tuples that contain each pair in the dictionary
print(thisdict.items())

# How to check if a key exists in the dictionary
if "year" in thisdict:
    print("'year' is found in the dictionary")
else:
    print("'year' not found in the dictionary")
    
# .update() will update the dictionary with items from the given argument
# the argument must be a dictionary, or an iterable object w/ key:value pairs
thisdict.update({"year": 2020, "newkey": "value"})
print(thisdict)

# .pop() will remove items with the specified key name
thisdict.pop("newkey")
print(thisdict)

# .popitem() removes the last item added into the dictionary
thisdict.popitem()
print(thisdict)

# del removes the item with the specified key from the dictionary
del thisdict["model"]
print(thisdict)

# .clear() empties the dictionary
anotherdict.clear()
print(anotherdict)

# Looping through a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)            # will return the keys
    print(thisdict[x])  # will return the values
for x, y in thisdict.items():
    print(x, y)         # will return the key followed by the value


# Nested dictionaries
myfamily = {
    "child1": {
        "name": "Nick",
        "year": 2000
    },
    "child2": {
        "name": "Kelly",
        "year": 2001
    },
    "child3": {
        "name": "Buster",
        "year": 2006
    }
}