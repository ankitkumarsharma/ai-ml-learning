#Python Lists - Lists are used to store multiple items in a single variable.
myList = ["apple", "banana", "cherry"]
print(myList)  # Output: ['apple', 'banana', 'cherry']
print(len(myList)) # Output: 3
#The list() Constructor
thisList = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thisList)  # Output: ['apple', 'banana', 'cherry']
print(thisList[1])
print(thisList[1:2])
thisList[1] = "blackcurrant"
print(thisList)
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Add List Items
## Append Items - To add an item to the end of the list, use the append() method:
thisList = ["apple", "banana", "cherry"]
thisList.append("orange")
print(thisList)  # Output: ['apple', 'banana', 'cherry', 'orange']

## Insert Items - To insert a list item at a specified index, use the insert() method:
thisList = ["apple", "banana", "cherry"]
thisList.insert(1, "orange")
print(thisList)  # Output: ['apple', 'orange', 'banana', 'cherry']

## Extend List - To append elements from another list to the current list, use the extend() method:
thisList = ["apple", "banana", "cherry"]  
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)  # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Remove List Items
## Remove Specified Item - The remove() method removes the specified item.
thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)  # Output: ['apple', 'cherry']

## Remove Specified Index - The pop() method removes the specified index.
thisList = ["apple", "banana", "cherry"]  
thisList.pop(1)
print(thisList)  # Output: ['apple', 'cherry']

## Remove Last Item - If you do not specify the index, the pop() method removes the last item.
thisList = ["apple", "banana", "cherry"]
thisList.pop()
print(thisList)  # Output: ['apple', 'banana']  

## Delete Item - The del keyword removes the specified index.
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)  # Output: ['banana', 'cherry']

## Clear the List - The clear() method empties the list.
thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)  # Output: []

## Loop Through a List
thisList = ["apple", "banana", "cherry"]  
for x in thisList:
  print(x)

## Sort List Alphanumerically - List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)  # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

## Sort Descending - To sort descending, use the keyword argument reverse = True:
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(reverse = True)
print(thisList)  # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

## Sort Numerically - You can also sort a list of numbers:
thisList = [100, 50, 65, 82, 23]
thisList.sort()
print(thisList)  # Output: [23, 50, 65, 82, 100]

## Sort Numerically Descending - To sort descending, use the keyword argument reverse = True:
thisList = [100, 50, 65, 82, 23]
thisList.sort(reverse = True)
print(thisList)  # Output: [100, 82, 65, 50, 23]

## Customize Sort Function - You can also customize your own function by using the keyword argument key = function.
def myFunc(n):
  return abs(n - 50)  
thisList = [100, 50, 65, 82, 23]
thisList.sort(key = myFunc) 
print(thisList)  # Output: [50, 65, 23, 82, 100]

## Case Insensitive Sort - By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters. You can perform a case-insensitive sort by using str.lower as a key function:
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort(key = str.lower)
print(thisList)  # Output: ['banana', 'cherry', 'Kiwi', 'Orange']

## Reverse Order of List - The reverse() method reverses the current sorting order of the elements.
thisList = ["banana", "Orange", "Kiwi", "cherry"] 
thisList.reverse()
print(thisList)  # Output: ['cherry', 'Kiwi', 'Orange', 'banana']

## Copy a List - You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)  # Output: ['apple', 'banana', 'cherry']

## Another way to make a copy is to use the built-in method list().
thisList = ["apple", "banana", "cherry"]
myList = list(thisList)
print(myList)  # Output: ['apple', 'banana', 'cherry']

## Join Two Lists - There are several ways to join, or concatenate, two or more lists in Python.
#Using the + Operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3] 
list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]

#Using the extend() Method
list1 = ["a", "b", "c"] 
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]

#Using the unpacking operator *
list1 = ["a", "b", "c"] 
list2 = [1, 2, 3]
list3 = [*list1, *list2]
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]  

## List Methods
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
#List Comprehension - offers a shorter syntax when you want to create a new list based on the values of an existing list.



