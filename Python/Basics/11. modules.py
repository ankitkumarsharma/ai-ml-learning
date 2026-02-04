#Python Modules - Modules are files containing Python code that can define functions, classes, and variables. They help organize code into manageable sections and promote code reuse. Modules can be imported into other Python scripts using the import statement.
#Creating a module
# Save the following code in a file named mymodule.py
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Importing a module
# In another Python file, you can import and use the mymodule
import mymodule # Assuming mymodule.py is in the same directory
print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(mymodule.add(5, 3))       # Output: 8
print(mymodule.person1["name"])  # Output: John

#Importing specific attributes from a module
from mymodule import greet, add
print(greet("Bob"))  # Output: Hello, Bob!
print(add(10, 20))   # Output: 30

#Using alias while importing a module - renames the module for easier access
import mymodule as mm
print(mm.greet("Charlie"))  # Output: Hello, Charlie!
print(mm.add(7, 2))         # Output: 9

from platform import system as sys 
print(sys())  # Output: The name of the operating system

#Importing all names from a module - not recommended for large modules due to potential name conflicts
from mymodule import *
print(greet("David"))  # Output: Hello, David!
print(add(4, 6))       # Output: 10

#Using the dir() Function - lists all the attributes and methods of a module
import mymodule
print(dir(mymodule))
#Output: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'greet', 'person1']
#The dir() function can also be used without arguments to list the names in the current local scope
print(dir())
#Output: List of names in the current local scope

#The Python Standard Library - A collection of modules and packages included with Python that provide various functionalities like file I/O, system calls, data serialization, and more.
#Example: Using the math module from the standard library
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

#Example: Using the datetime module from the standard library
import datetime
now = datetime.datetime.now()
print(now)  # Output: Current date and time

#Example: Using the os module from the standard library
import os
print(os.getcwd())  # Output: Current working directory
#Example: Using the random module from the standard library
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10

#Python JSON Module - The json module provides functions to work with JSON data, allowing you to parse JSON strings and convert Python objects to JSON format.
import json
#Converting Python object to JSON string
person = {"name": "Alice", "age": 30, "city": "New York"}
person_json = json.dumps(person)    
print(person_json)  # Output: {"name": "Alice", "age": 30, "city": "New York"}

#Converting JSON string to Python object
person_dict = json.loads(person_json)
print(person_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person_dict["name"])  # Output: Alice

#Reading JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
#Writing JSON data to a file
with open('output.json', 'w') as file:
    json.dump(person, file)
#Output: A file named output.json will be created with the JSON representation of the person dictionary 

"""
Python	        JSON
dict	        Object
list	        Array
tuple	        Array
str	            String
int	            Number
float	        Number
True	        true
False	        false
None	        null
"""
#Example of using json with complex data types
data = {
    "name": "Bob",
    "age": 25,
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}
data_json = json.dumps(data, indent=4)
print(data_json)
#Output: JSON string with indentation for better readability
data_dict = json.loads(data_json)
print(data_dict)

#Python RegEx Module - The re module provides support for regular expressions in Python, allowing you to search, match, and manipulate strings based on specific patterns.
import re
#Example: Searching for a pattern in a string
text = "The rain in Spain"
x = re.search("ai", text)
if x:
    print("Match found:", x.group())  # Output: Match found: ai
else:
    print("No match found")

#Example: Finding all occurrences of a pattern
text = "The rain in Spain"
x = re.findall("ai", text)
print("All matches:", x)  # Output: All matches: ['ai', 'ai']

#Example: Replacing a pattern in a string
text = "The rain in Spain"
x = re.sub("Spain", "Italy", text)
print("Replaced text:", x)  # Output: Replaced text: The rain in Italy
#Example: Splitting a string based on a pattern
text = "apple, banana, cherry"
x = re.split(", ", text)
print("Split text:", x)  # Output: Split text: ['apple', 'banana', 'cherry']

#Python PIP - PIP is the package installer for Python. It allows you to install and manage additional libraries and dependencies that are not included in the standard library. like in javaScript's npm.
#Installing a package using pip
# Open your command prompt or terminal and run the following command:
# pip install package_name
#Example: Installing the requests library
# pip install requests
#Using the requests library to make an HTTP GET request
import requests
response = requests.get('https://api.github.com')
print("Status Code:", response.status_code)  # Output: Status Code: 200
print("Response Body:", response.json())     # Output: JSON response from the GitHub API

# pip list - Lists all installed packages
# pip show package_name - Shows details about a specific package
# pip uninstall package_name - Uninstalls a specific package
