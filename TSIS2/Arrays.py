cars = ["Ford", "Volvo", "BMW"]

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

x = cars[0]
cars[0] = "Toyota"
print(x)

# The Length of an Array
x = len(cars)
print(x)

# Looping Array Elements
for x in cars:
    print(x)

# Adding Array Elements
cars.append("Honda")

# Removing Array Elements
cars.pop(1)
cars.append("Volvo")
cars.remove("Volvo")