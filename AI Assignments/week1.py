# Python Fundamentals Cheat Sheet

# Data Types
# Integers and floating-point numbers
num_int = 10
num_float = 3.14

# Strings
text = "Hello, world!"
multiline_text = """This is a
multiline string"""

# Boolean
is_true = True
is_false = False

# Variables
name = "Alice"
age = 30

# Expressions
result = 10 + 5  # Addition
result = 10 - 5  # Subtraction
result = 10 * 5  # Multiplication
result = 10 / 5  # Division
result = 10 // 3  # Floor Division
remainder = 10 % 3  # Modulus (Remainder)

# Conditionals
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Loops
# For loop
for i in range(5):
    print(i)

# While loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])  # Accessing elements
print(len(fruits))  # Length of list

# Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Accessing values
person["age"] = 31  # Modifying value
person["gender"] = "female"  # Adding new key-value pair

# Input/Output
name = input("Enter your name: ")
print("Hello,", name)

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("This is written to the file.")
