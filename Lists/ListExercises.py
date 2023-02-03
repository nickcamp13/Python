fruits = ['apple', 'banana', 'cherry']

# print second element of fruits list
print(fruits[1])

# change value of 'apple' to 'kiwi'
fruits[0] = 'kiwi'

# use .append() to add 'orange' to fruits
fruits.append('orange')

# use .insert() to add 'lemon' as the second element of fruits list
fruits.insert(1, 'lemon')

# use .remove() to remove 'banana' from fruits
fruits.remove('banana')

# use negative indexing to print the last item of fruit list
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# use a range of indexes to print the third, fourth and fifth items of fruits
print(fruits[2:5])
print(fruits[-5:-2])

# use correct syntax to print the number of items in fruits
print(len(fruits))