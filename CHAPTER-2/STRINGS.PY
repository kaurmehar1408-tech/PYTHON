# 1. 🔤 Strings in Python

# Strings = sequence of characters enclosed in " " or ' '.

# Example:

# name = "Harmehar"
# city = 'Delhi'

# 📌 String Operations

# Concatenation (+)
# first = "Hello"
# second = "World"
# print(first + " " + second)  # Hello World

# Repetition (*)
# print("Hi! " * 3)  # Hi! Hi! Hi!

# Indexing & Slicing
# word = "Python"
# print(word[0])     # P (first char, index starts at 0)
# print(word[-1])    # n (last char)
# print(word[0:4])   # Pyth (slice from index 0 to 3)

# Length
# print(len("Harmehar"))  # 8

# 📌 String Methods (common)
# s = "  hello world  "

# print(s.upper())       # "  HELLO WORLD  "
# print(s.lower())       # "  hello world  "
# print(s.strip())       # "hello world" (removes spaces)
# print(s.replace("hello", "hi"))  # "  hi world  "
# print(s.split())       # ['hello', 'world']
# print("-".join(["2025","09","05"]))  # "2025-09-05"
# print(s.find("world")) # 8

# 📌 f-Strings (formatting)
# name = "Harmehar"
# age = 20
# print(f"My name is {name} and I am {age} years old.")

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Example
# Get the character at position 1 (remember that the first character has the position 0):

# a = "Hello, World!"
# print(a[1])