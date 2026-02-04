#Python Sets - Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets. Duplicate members are not allowed.
thisSet = {"apple", "banana", "cherry"}
print(thisSet)  # Output: {'banana', 'cherry', 'apple'}

#The set() Constructor
thisSet = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisSet)  # Output: {'banana', 'cherry', 'apple'}

#What is the data type of a set?
print(type(thisSet))  # Output: <class 'set'>

#Access Set Items - You cannot access items in a set by referring to an index or a key. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thisSet:
  print(x)  
# Check if "banana" is present in the set
print("banana" in thisSet)  # Output: True  

#Add Set Items
# To add one item to a set use the add() method.
thisSet.add("orange")
print(thisSet)  # Output: {'banana', 'cherry', 'orange', 'apple'}

# To add more than one item to a set use the update() method.
thisSet.update(["mango", "grape", "pineapple"]) 
print(thisSet)  # Output: {'banana', 'cherry', 'orange', 'apple', 'mango', 'grape', 'pineapple'}

#Remove Set Items
# To remove an item in a set, use the remove(), or the discard() method.
thisSet.remove("banana")
print(thisSet)  # Output: {'cherry', 'orange', 'apple', 'mango', 'grape', 'pineapple'}
thisSet.discard("cherry")
print(thisSet)  # Output: {'orange', 'apple', 'mango', 'grape', 'pineapple'}
# The difference between remove() and discard() is that remove() will raise an error if the specified item does not exist, and discard() will not.
# You can also use the pop() method to remove an item, but this method will remove a random item, since sets are unordered.
x = thisSet.pop()   
print(x)  # Output: random item
print(thisSet)  # Output: remaining items in the set

# The clear() method empties the set.
thisSet.clear()
print(thisSet)  # Output: set()

# The del keyword will delete the set completely.
del thisSet
# print(thisSet)  # This will raise an error because the set no longer exists

#Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  # Output: {'a', 1, 2, 3, 'c', 'b'}
set1.update(set2)
print(set1)  # Output: {'a', 1, 2, 3, 'c', 'b'}
#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)  # Output: {'apple'} 

#The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)  # Output: {'apple'} 
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"} 
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)  # Output: {'banana', 'cherry', 'google', 'microsoft'}
#The symmetric_difference() method will return a new set, that contains only the elements that are
# NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)  # Output: {'banana', 'cherry', 'google', 'microsoft'}
#Difference Between update(), union(), intersection_update(), intersection(), symmetric_difference_update(), and symmetric_difference()
"""
update() - Inserts the items in set2 into set1
union() - Returns a new set with all items from both sets 
intersection_update() - Removes the items from set1 that are not present in set2
intersection() - Returns a new set with items that are present in both sets
symmetric_difference_update() - Inserts the items that are not present in both sets into set1
symmetric_difference() - Returns a new set with items that are not present in both sets
"""
#Python frozenset - A frozenset is an immutable version of a set, which means that once it is created, its items cannot be changed, added, or removed. Frozensets are hashable and can be used as keys in dictionaries or as elements of other sets.
thisFrozenset = frozenset(("apple", "banana", "cherry"))
print(thisFrozenset)  # Output: frozenset({'banana', 'cherry', 'apple'})
#What is the data type of a frozenset?
print(type(thisFrozenset))  # Output: <class 'frozenset'>
#Access Frozenset Items - You cannot access items in a frozenset by referring to an index or a key. But you can loop through the frozenset items using a for loop, or ask if a specified value is present in a frozenset, by using the in keyword.
for x in thisFrozenset:
  print(x)
#Frozenset Methods
# copy() - Returns a shallow copy of the frozenset
thisFrozenset = frozenset(("apple", "banana", "cherry"))
myFrozenset = thisFrozenset.copy()
print(myFrozenset)  # Output: frozenset({'banana', 'cherry', 'apple'})
# difference() - Returns a new frozenset with elements in the frozenset that are not in the specified set
x = frozenset({"apple", "banana", "cherry"})
y = frozenset({"google", "microsoft", "apple"})
z = x.difference(y)
print(z)  # Output: frozenset({'banana', 'cherry'})
# intersection() - Returns a new frozenset with elements common to the frozenset and the specified set
x = frozenset({"apple", "banana", "cherry"})
y = frozenset({"google", "microsoft", "apple"})
z = x.intersection(y)
print(z)  # Output: frozenset({'apple'})
# isdisjoint() - Returns True if the frozenset has no elements in common with the specified set
x = frozenset({"apple", "banana", "cherry"})
y = frozenset({"google", "microsoft", "facebook"})
z = x.isdisjoint(y)
print(z)  # Output: True
# issubset() - Returns True if all elements of the frozenset are in the specified set
x = frozenset({"apple", "banana"})
y = frozenset({"google", "microsoft", "apple", "banana", "cherry"})
z = x.issubset(y)
print(z)  # Output: True
# issuperset() - Returns True if all elements of the specified set are in the frozenset
x = frozenset({"google", "microsoft", "apple", "banana", "cherry"})
y = frozenset({"apple", "banana"})
z = x.issuperset(y)
print(z)  # Output: True
# symmetric_difference() - Returns a new frozenset with elements in either the frozenset or the specified set but not in both
x = frozenset({"apple", "banana", "cherry"})    
y = frozenset({"google", "microsoft", "apple"})
z = x.symmetric_difference(y)
print(z)  # Output: frozenset({'banana', 'cherry', 'google', 'microsoft'})
# union() - Returns a new frozenset with elements from the frozenset and all specified sets
x = frozenset({"apple", "banana", "cherry"})  
y = frozenset({"google", "microsoft", "apple"})
z = x.union(y)
print(z)  # Output: frozenset({'banana', 'cherry', 'google', 'microsoft', 'apple'}) 
