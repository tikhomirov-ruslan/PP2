fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":    
    print(x)

# The break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() function
for x in range(6): # 0 to 5
    print(x)

# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: 
        break
    print(x)
else:
    print("Finally finished!")

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# the pass statement
for x in [0, 1, 2]:
    pass