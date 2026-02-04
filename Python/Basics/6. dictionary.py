#Python Dictionaries - Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
##*Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(len(thisDict))  # Output: 3

#The dict() Constructor
thisDict = dict(brand="Ford", model="Mustang", year=1964)
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#What is the data type of a dictionary?
print(type(thisDict))  # Output: <class 'dict'>

#Access Dictionary Items
x = thisDict["model"]
print(x)  # Output: Mustang
x = thisDict.get("model")
print(x)  # Output: Mustang

# keys() method - Returns a list containing the dictionary's keys
x = thisDict.keys()
print(x)  # Output: dict_keys(['brand', 'model', 'year'])
# values() method - Returns a list of all the values in the dictionary
x = thisDict.values()
print(x)  # Output: dict_values(['Ford', 'Mustang', 1964])
# items() method - Returns a list containing a tuple for each key value pair
x = thisDict.items()
print(x)  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#Change Dictionary Items
thisDict["year"] = 2020
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
thisDict.update({"year": 2021}) # using update() method  
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2021}
#Add Dictionary Items
thisDict["color"] = "red"
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2021, 'color': 'red'}
#Remove Dictionary Items
thisDict.pop("model") # removes item with the specified key name
print(thisDict)  # Output: {'brand': 'Ford', 'year': 2021, 'color': 'red'}
thisDict.popitem() # removes the last inserted item
print(thisDict)  # Output: {'brand': 'Ford', 'year': 2021}
del thisDict["year"] # removes item with the specified key name 
print(thisDict)  # Output: {'brand': 'Ford'}
thisDict.clear() # empties the dictionary
print(thisDict)  # Output: {}
#The del keyword will delete the dictionary completely.
del thisDict
# print(thisDict)  # This will raise an error because the dictionary no longer exists
#Loop Through a Dictionary
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisDict:
  print(x)  # Output: brand model year  
for x in thisDict.keys():
  print(x)  # Output: brand model year
for x in thisDict.values():
  print(x)  # Output: Ford Mustang 1964
for x, y in thisDict.items():
  print(x, y)  # Output: brand Ford model Mustang year 1964

#Copy a Dictionary
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
myDict = thisDict.copy()  
print(myDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

myDict = dict(thisDict)
print(myDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Nested Dictionaries
myDict = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myDict)  # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
child1 = myDict["child1"]
print(child1)  # Output: {'name': 'Emil', 'year': 2004}
child1_name = myDict["child1"]["name"]  
print(child1_name)  # Output: Emil  
child2_year = myDict["child2"]["year"]  
print(child2_year)  # Output: 2007
#The dict() Constructor can also be used to make a nested dictionary.
myDict = dict(child1 = dict(name="Emil", year=2004),
              child2 = dict(name="Tobias", year=2007),  
              child3 = dict(name="Linus", year=2011))
print(myDict)  # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}  
child3_name = myDict["child3"]["name"]  
print(child3_name)  # Output: Linus
#Loop Through Nested Dictionaries
for child, info in myDict.items():
  print(child)  # Output: child1 child2 child3
  for key in info:
    print(key, info[key])

#Dictionary Methods
# copy() - Returns a shallow copy of the dictionary
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
myDict = thisDict.copy()
print(myDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# fromkeys() - Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0
thisDict = dict.fromkeys(x, y)
print(thisDict)  # Output: {'key1': 0, 'key2': 0, 'key3': 0}
# get() - Returns the value of the specified key
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisDict.get("model")
print(x)  # Output: Mustang
# items() - Returns a view object that displays a list of a dictionary's key-value tuple
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisDict.items()
print(x)  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# keys() - Returns a view object that displays a list of all the keys in the dictionary
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisDict.keys()
print(x)  # Output: dict_keys(['brand', 'model', 'year'])
# pop() - Removes the item with the specified key name
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisDict.pop("model")
print(thisDict)  # Output: {'brand': 'Ford', 'year': 1964}
# popitem() - Removes the last inserted key-value pair
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisDict.popitem()
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang'}
# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisDict.setdefault("model", "Bronco")  
print(x)  # Output: Mustang
y = thisDict.setdefault("color", "red")
print(y)  # Output: red
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
# update() - Updates the dictionary with the specified key-value pairs
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisDict.update({"year": 2020}) 
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
thisDict.update({"color": "red"})
print(thisDict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}
# values() - Returns a view object that displays a list of all the values in the dictionary
thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisDict.values()
print(x)  # Output: dict_values(['Ford', 'Mustang', 1964])  
#Example of dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  
