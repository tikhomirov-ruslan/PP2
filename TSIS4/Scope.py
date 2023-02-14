# Local Scope
def myfunc():
    x = 300
    print(x)
myfunc()

# Function Inside Function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

# Global Scope
x = 300
def myfunc():
    print(x)
myfunc()
print(x)

# Naming Variables
x = 300

def myfunc():
    x = 200
    print(x)
myfunc()
print(x)

# Global Keyword
def myfunc():
    global x
    x = 300
myfunc()
print(x)

# 

x = 300

def myfunc():
    global x
    x = 200
myfunc()
print(x)