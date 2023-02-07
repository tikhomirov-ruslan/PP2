i = 1
while i < 6:
  print(i)
  i += 1

#break statement
  j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1

# continue statement
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")