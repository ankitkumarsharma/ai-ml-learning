#while loop
i = 1
while i < 6:
    print(i)
    i += 1

#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#looping through a string
for letter in "banana":
    print(letter)

#using break statement
for i in range(10):
    if i == 5:
        break
    print(i)

#using continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#using else statement with loops
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

#nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

#using pass statement
for i in range(5):
    pass  # Placeholder for future code
print("Loop with pass statement completed")