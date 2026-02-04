#Python Try Except - The try-except block is used for handling exceptions in Python. It allows you to write code that can gracefully handle errors without crashing the program. The code inside the try block is executed, and if an exception occurs, the code inside the except block is executed.
#Basic Syntax of try-except block
"""
try:
    # code that may raise an exception
except SomeException:
    # code to handle the exception
"""
#Example of try-except block
try:
    x = 10 / 0  
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
#Output: Error: Division by zero is not allowed.

try:
  print(x)
except:
  print("An exception occurred")
#Output: An exception occurred
"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks
"""
#Example with else and finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", x)
finally:
    print("Execution completed.")
#Output:
#Result: 5.0