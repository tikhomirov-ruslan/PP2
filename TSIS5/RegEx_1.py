# 1
import re
txt = input()
ans = re.findall("ab*", txt)
print(ans)
# 2
x = re.findall ("ab{2,3}", txt)
print(x)

# 3
x = re.findall("[a-z]+_", txt)
print(x)

# 4
x = re.findall("[A-Z][a-z]+", txt)
print(x)

# 5
x = re.findall("a.*b$", txt)
print(x)

# 6 
x = re.sub("[ ,.]", ":", txt)
print(x)

# 7
myTxt = "helloWorld"
my_txt = "hello_world"
x = re.findall(r"_[a-z]", my_txt)[0][1]
print(x)
y = re.sub(r"_[a-z]", x.upper(), my_txt)
print(y)

# 8


# 9
x = re.findall(r"[A-Z]", myTxt)
print(x)
y = re.sub(r" ")
# 10
