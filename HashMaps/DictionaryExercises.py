car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Use .get() to return the value of the "model" key
print(car.get("model"))

# change the "year" value to 2020
car["year"] = 2020
print(car)

# add "color": "red"
car["color"] = "red"
print(car)

# use .pop() to remove the "model" pair
car.pop("model")
print(car)

# use .clear() to empty the car dictionary
car.clear()
print(car)