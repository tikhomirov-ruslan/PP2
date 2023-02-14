# 1
import math
from cmath import pi
degree = float(input())
print(math.radians(degree))

# 2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
S = ((a + b) / 2) * h
print(float(S))

# 3 
from cmath import tan
a = int(input())
b = int(input())
tg = math.tan((math.pi) / b)
S = 0.25 * a * a * b / tg
print(S)

# 4
a = float(input())
b = float(input())
S = a * b
print(float(S))