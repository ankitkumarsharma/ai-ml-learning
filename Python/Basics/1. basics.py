import random
print('Hello World')
print("I am", 35, "years old.")
# this is a comment

"""
This is a comment
written in
more than just one line
"""
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
----------------------------------------------
x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True/False	                                bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	
x = None	                                    NoneType
----------------------------------------------
x = str("Hello World")	                        str	
x = int(20)	                                    int	
x = float(20.5)	                                float	
x = complex(1j)	                                complex	
x = list(("apple", "banana", "cherry"))	        list	
x = tuple(("apple", "banana", "cherry"))	    tuple	
x = range(6)	                                range	
x = dict(name="John", age=36)	                dict	
x = set(("apple", "banana", "cherry"))	        set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	                                    bool	
x = bytes(5)	                                bytes	
x = bytearray(5)	                            bytearray
x = memoryview(bytes(5))	                    memoryview

"""
print(random.randint(10, 99))
#Python Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x, y, z)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x, y, z, w)
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)
#boolean Values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#Python Operators
#Arithmetic Operators
x = 15
y = 4
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division
#Comparison Operators
x = 5
y = 3
print(x == y) # Equal
print(x != y) # Not Equal
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to
#Logical Operators
x = 5
print(x > 0 and x < 10)
print(x > 0 or x < 4)
print(not(x > 0 and x < 10))
#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # Returns True because z is the same object as x
print(x is y) # Returns False because x is not the same object as y
print(x is not y) # Returns True because x is not the same object as y
print(x == y)   # Returns True because x is equal to y
"""
Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""
#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # Returns True because a sequence with the value "banana" is in the list
print("pineapple" not in fruits) # Returns True because a sequence with the value "pineapple" is not in the list    
#Operator Precedence - () , * / % // , + - , < <= > >= , == != , not , and , or

#list vs tuple vs set vs dictionary
"""
Parameter 	        list	            tuple	            set	                                dictionary
Syntax	            [1, 2, 3]	        (1, 2, 3)	        {1, 2, 3}	                        {"a": 1, "b": 2}
Ordered	            Yes	                Yes	                No	                                Yes (insertion order, Python 3.7+)
Mutable	            Yes (changeable)	No (unchangeable)	Yes (can add/remove elements)	    Yes (changeable)
Duplicates	        Allowed	            Allowed	            Not Allowed (unique elements only)	Keys must be unique; values can be duplicated
Indexing	        Integer-based	    Integer-based	    No index-based access	            Key-based access
"""
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""