# 1
class String:
    def __init__(self, string):
       self.string = string
    def getString(self):
        self.string = str(input())
    def printString(self):
        print(self.string.upper())

# 2
class Square:
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0):
        self.length = length
    def area(self):
        print(self.length * self.length)

# 3
class Rectangle(Shape):
    def __init__(self, width):
        self.width = width
    def area(self):
        print(self.length * self.width)

  