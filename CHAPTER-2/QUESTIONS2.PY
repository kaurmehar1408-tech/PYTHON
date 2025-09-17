# Q-1 Take input of a number and print whether it is positive, negative, or zero.
# SOLUTION =
# num = int(input("enter a number:" ))
# if num > 0:
#     print("positive number")
# elif num == 0:
#     print("zero")
# else:
#     print("negative number")

# Q-2 Take a number as input and print whether it is even or odd.
# SOLUTION=
# num = int(input("enter a number:" ))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# Q-3 Take age as input and print if a person is eligible to vote (age ≥ 18).
# SOLUTION=
# age = int(input("enter your age :" ))
# if age >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# Q-4 Find the largest of two numbers.
# SOLUTION=
# a = int(input("enter ist number:" ))
# b = int(input("enter second number:" ))
# if a > b:
#     print("greatest number is :" ,a)
# elif a == b:
#     print("both are equal numbers")
# else:
#     print("greatest number  :" ,b)

# Q-5 Find the largest of three numbers.
# SOLUTION=
# a = int(input("enter first number :" ))
# b = int(input("enter second number :" ))
# c = int(input("enter third number :" ))
# if a>b and a>c:
#     print("greatest number is :" ,a)
# elif b>c:
#     print("greatest number is :" ,b)
# else:
#     print("greatest number is :" ,c)

# Q-6 Take a year as input and print if it is a leap year or not.
# SOLUTION=
year = int(input("Enter a year: "))
if (year % 400 == 0):
    print(year, "is a Leap Year ✅")
elif (year % 100 == 0):
    print(year, "is NOT a Leap Year ❌")
elif (year % 4 == 0):
    print(year, "is a Leap Year ✅")
else:
    print(year, "is NOT a Leap Year ❌")

# Q-7 Check if a character is a vowel or consonant.
# SOLUTION=
# Take a single character input
# char = input("Enter a single alphabet character: ")
# # Define the string containing all vowels
# vowels = "aeiouAEIOU"
# # Check if the input character is a vowel or consonant
# if char in vowels:
#     print(char, "is a Vowel ✅")
# else:
#     print(char, "is a Consonant ❌")

# Q-8 Check if a number is divisible by 3 and 5 both.
# SOLUTION=
# ✅ Code
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print(num, "is divisible by both 3 and 5 ✅")
# else:
#     print(num, "is NOT divisible by both 3 and 5 ❌"

# ✅ Q9. Check if a person is a teenager (age between 13–19)
# age = int(input("Enter age: "))
# if 13 <= age <= 19:
#     print("Teenager ✅")
# else:
#     print("Not a teenager ❌"

# ✅ Q10. Print greetings based on time (24-hour format)
# time = int(input("Enter time (0-23): "))
# if 5 <= time < 12:
#     print("Good Morning ☀️")
# elif 12 <= time < 17:
#     print("Good Afternoon 🌤️")
# elif 17 <= time < 21:
#     print("Good Evening 🌇")
# else:
#     print("Good Night 🌙")

# ✅ Q11. Check if a number is prime
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is NOT a prime number ❌")
#             break
#     else:
#         print(num, "is a prime number ✅")
# else:
#     print(num, "is NOT a prime number ❌")

# ✅ Q12. Check if three sides form a valid triangle
# a = int(input("Enter side 1: "))
# b = int(input("Enter side 2: "))
# c = int(input("Enter side 3: "))
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("Valid Triangle ✅")
# else:
#     print("Not a valid Triangle ❌")

# ✅ Q13. Grade based on marks
# marks = int(input("Enter marks (0-100): "))
# if marks >= 90:
#     grade = "A"
# elif marks >= 75:
#     grade = "B"
# elif marks >= 50:
#     grade = "C"
# else:
#     grade = "Fail"
# print("Grade:", grade)

# ✅ Q14. FizzBuzz (Divisible by 3 and/or 5)
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# ✅ Q15. Check if a number is a perfect square
# import math
# num = int(input("Enter a number: "))
# sqrt_num = math.isqrt(num)   # Integer square root
# if sqrt_num * sqrt_num == num:
#     print(num, "is a Perfect Square ✅")
# else:
#     print(num, "is NOT a Perfect Square ❌")

