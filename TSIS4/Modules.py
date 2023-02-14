# Use a Module
import mymodule
mymodule.greeting("Jonathan")

# Variables in Module
a = mymodule.person1["age"]
print(a)

# Re-naming a Module    
import mymodule as mx
b = mx.person1["age"]
print(b)

# Built-in Modules
import platform
x = platform.system()
print(x)

# Using the dir() Function
y = dir(platform)
print(y)

# Import From Module
from mymodule import person1
print (person1["age"])