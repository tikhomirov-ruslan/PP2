# 1
import re
txt = str(input())
a = re.findall("ab", txt)
b = re.findall("a0", txt)
c = re.findall("abb", txt)
print(a, b, c)
# 2
x = re.findall ("ab{2,3}", txt)
print(x)

# 3
x = re.findall("[a-z][_][a-z]", txt)
print(x)

# 4
x = re.findall("[A-Z][a-z]+", txt)
print(x)

# 5
x = re.findall("a.+b$", txt)
print(x)

# 6 
x = re.sub("[ ,.]","|", txt)
print(x)
