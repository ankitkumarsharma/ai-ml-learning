# Tuples in Python are immutable sequences, similar to lists but with fixed elements. A tuple is a collection which is ordered and unchangeable and Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(len(thistuple))  # Output: 5

# The tuple() Constructor
thisTuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisTuple)  # Output: ('apple', 'banana', 'cherry')
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1) # Output: ('abc', 34, True, 40, 'male')
print(tuple1[1])  # Output: 34

#What is the data type of a tuple?
print(type(thistuple))  # Output: <class 'tuple'>

# Access Tuple Items
print(thistuple[1])  # Output: banana 
print(thistuple[1:3])  # Output: ('banana', 'cherry')
print(thistuple[-1])  # Output: cherry
print(thistuple[-3:-1])  # Output: ('cherry', 'apple')

#Change Tuple Values
# Tuples are unchangeable, so you cannot change, add, or remove items once the tuple is created.
# But you can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  # Output: ('apple', 'kiwi', 'cherry') 
# same for add or remove an element from tuple, as explain above.

#Unpacking a Tuple -  When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry") # packing a tuple
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")  
(green, yellow, red) = fruits # unpacking a tuple
print(green)  # Output: apple 
#Using Asterisk* - If the number of variables is less than the number of values, you can add an asterisk* to the variable name that will hold the remaining values as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(red)  # Output: ['cherry', 'strawberry', 'raspberry']

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)  
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)

#Multiply Tuples - If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Tuple Methods
# count() - Returns the number of times a specified value occurs in a tuple
thistuple = (1, 2, 3, 2, 2, 4, 5)
x = thistuple.count(2)  
print(x)  # Output: 3
# index() - Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 2, 3, 4, 5)
x = thistuple.index(4)  
print(x)  # Output: 3