print("It's alright")
#Strings are Arrays
a = "Hello, World!"
print(a[1])
print(a[-1])
#Looping Through a String
for x in "ankit":
    print(x)
#String Length
print(len(a))
#Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)
#Slicing - You can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])
# Slice From the Start
print(b[:5])
# Slice To the End
print(b[2:])
#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#F-Strings
name = "Ankit"
txt = f"My name is John, I am {name}"
print(txt)
# String methods
txt = "hello world"
print(txt.capitalize()) # Capitalize the first letter
print(txt.upper()) # Convert to uppercase
print(txt.lower()) # Convert to lowercase
print(txt.title()) # Convert to title case  
print(txt.count('o')) # Count occurrences of a substring
print(txt.replace("h", "j")) # Replace a substring
print(txt.split(" ")) # Split the string into a list
print(a.strip()) # Remove whitespace from both ends
print(a.find("World")) # Find the position of a substring
"""
Method	            Description
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning
"""


