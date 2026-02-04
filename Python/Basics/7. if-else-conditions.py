#Python If Statement - 
a = 33
b = 200
if b > a:
  print("b is greater than a")  # Output: b is greater than a

#Python Elif Statement -
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")  # Output: a and b are equal

#Python Else Statement -  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  # Output: b is not greater than a

#Python Shorthand If 
a = 200
b = 33
if a > b: print("a is greater than b")  # Output: a is greater than b

#Python Shorthand If...Else
a = 200
b = 33  
print("A") if a > b else print("B")  # Output: A

#Python And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")  # Output: Both conditions are True

#Python Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")  # Output: At least one of the conditions is True

#Nested If
x = 41
if x > 10:
  print("Above ten,")  
  if x > 20:
    print("and also above 20!")  # Output: Above ten, and also above 20!
  else:
    print("but not above 20.")

#The pass Statement
a = 33
b = 200
if b > a:
  pass  # Output: (no output, pass is just a placeholder) 

#Python Conditional Expressions
a = 200
b = 33
print("A") if a > b else print("B")  # Output: A
print("A" if a > b else "B")  # Output: A
#Multiple Conditions in a Single Line
a = 200
b = 33
print("A" if a > b else "B" if a == b else "C")  # Output: A