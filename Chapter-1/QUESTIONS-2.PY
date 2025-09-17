# Q-1 Check and print the type of values: 10, 10.0, "10".
# SOLUTION =
# a = 10
# b = 10.0
# c = "10"
# print(type(a))
# print(type(b))
# print(type(c))

# Q-2 Convert a float (12.56) into an int and observe the result.
# SOLUTION =
# a = 12.56
# b = int(a)
# print(type(b))

# Q-3 Convert an int (25) into a float.
# SOLUTION =
# a = 25
# b = float(a)
# print(type(b))

# Q-4 Store a number as a string "123" and convert it into an int.
# SOLUTION=
# str1="123"
# str2=int(str1)
# print(type(str2))

# Q-5 Add an integer and a float together. What will the result type be?
# SOLUTION=
# a = int(input("enter a number :" ))
# b = float(input("enter a number :" ))
# c = a + b
# print(c)
# print(type(c))

# Q-6 Take user input (string) and check its type. Convert it into int.
# SOLUTION=
# a = input("enter something: ")

# if a.isdigit():   # check if input contains only digits
#     b = int(a)
#     print("Converted to int:", b)
# else:
#     print("Not a valid integer input")

# Q-7 Write a program to calculate floor division (29 // 5).
# SOLUTION=
# floordiv=29//5
# print(floordiv)

# Q-8 Print the square root of a number using ** 0.5.
# SOLUTION=
# num=int(input("enter a number:" ))
# sq_root=num**0.5
# print(sq_root)

# Q-9 Use math module to calculate sqrt(49) and pow(2, 5).
# SOLUTION=
# import math

# # square root of 49
# sqrt_val = math.sqrt(49)

# # 2 raised to power 5
# pow_val = math.pow(2, 5)

# print("Square root of 49:", sqrt_val)
# print("2 to the power 5:", pow_val)

# Q-10 Find the remainder when 29 is divided by 5.
# SOLUTION=
# REM=29%5
# print(REM)

# Q-11 Store the result of a comparison (like 5 > 3) in a variable and print its type
# result = 5 > 3
# print(result)        # True
# print(type(result))  # <class 'bool'>

# Q-12 Write a program that checks if a number is positive
# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# else:
#     print("Not Positive")

# Q-13 Check if a given year is a leap year
# 👉 Rule:
# Year divisible by 400 → Leap Year
# Else if divisible by 100 → Not Leap Year
# Else if divisible by 4 → Leap Year
# Else → Not Leap Year
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# Q-14 Write a program that checks if someone is eligible to vote (age ≥ 18)
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible to vote ✅")
# else:
#     print("Not eligible to vote ❌")

# Q-15 Evaluate expressions like (True and False), (True or False), not True
# print(True and False)   # False
# print(True or False)    # True
# print(not True)         # False

