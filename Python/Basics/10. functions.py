#Python functions - Functions are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and reducing redundancy. Functions can take inputs (parameters) and can return outputs (return values).
#Defining a function
def greet(name):
    """This function greets the person passed as a parameter."""
    return f"Hello, {name}!"

#Calling a function
print(greet("Alice"))  # Output: Hello, Alice!

#Function with multiple parameters
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b
print(add(5, 3))  # Output: 8

#Function with default parameters
def power(base, exponent=2):    
    """This function returns the base raised to the power of exponent."""
    return base ** exponent
print(power(4))       # Output: 16 (4^2)
print(power(2, 3))    # Output: 8  (2^3)

#Function with variable-length arguments
def multiply(*args):
    """This function returns the product of all numbers passed as arguments."""
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(2, 3, 4))  # Output: 24 (2*3*4)

#Parameters vs Arguments - Parameters are the variables defined in the function definition, while arguments are the actual values passed to the function when it is called.
#Example to illustrate Parameters vs Arguments
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Email") # "Email" is an argument

#Function with keyword arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Function with arbitrary keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 

#Combining *args and **kwargs
def my_function(*args, **kwargs):
    print("I would like to have", args[0], "and", args[1], "for breakfast.")
    print("My name is", kwargs["name"])
my_function("eggs", "bacon", name="Alice")

#Lambda function (anonymous function) - A lambda function is a small anonymous function. It can take any number of arguments but can only have one expression.
# synatx - "lambda arguments: expression"
square = lambda x: x ** 2
print(square(5))  # Output: 25

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Why Use Lambda Functions? - They are used for short, throwaway functions that are not going to be reused elsewhere. They are often used in higher-order functions like map(), filter(), and reduce().
#Example of using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
#Example of using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
#Example of using lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1*2*3*4*5)

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) # Output: 22

#Python Decorators - Decorators are a way to modify or enhance the behavior of functions or methods without changing their actual code. They are often used for logging, access control, instrumentation, and caching.
#Defining a simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
#Using the decorator
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
#Output:
#Something is happening before the function is called.
#Hello!
#Something is happening after the function is called.

#Decorator with parameters
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")    
greet("Alice")
#Output:
#Hello, Alice!
#Hello, Alice!  
#Hello, Alice!

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())
#Output: HELLO SALLY

#Python Recursion - Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used for problems that can be broken down into smaller, similar subproblems.
#Example of a recursive function to calculate factorial
def factorial(n):
    """This function returns the factorial of a given number n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120 (5*4*3*2*1)

#Example of a recursive function to calculate Fibonacci numbers
def fibonacci(n):
    """This function returns the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))  # Output: 8 (0, 1, 1, 2, 3, 5, 8)

#Example of a recursive function to sum a list of numbers
def sum_list(numbers):
    """This function returns the sum of a list of numbers."""
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15 (1+2+3+4+5)

#Python Generators - Generators are a type of iterable, like lists or tuples, but they do not store their contents in memory. Instead, they generate values on the fly and yield them one at a time, which makes them more memory efficient for large datasets.
#Defining a simple generator
def simple_generator():
    yield 1
    yield 2
    yield 3
for value in simple_generator():
    print(value)
#Output:
#1
#2
#3

