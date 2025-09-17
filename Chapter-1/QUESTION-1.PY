#Part A: Basics

# Q-1 Create 5 variables of different data types (int, float, str, bool, complex) and print their values and types.
# SOLUTION =
# var1=34
# var2=27.14
# var3="good vibes"
# var4= True
# var5= 4 + 3j

# print(var1,type(var1))
# print(var2,type(var2))
# print(var3,type(var3))
# print(var4,type(var4))
# print(var5,type(var5))

# Q-2 Assign the same value to three different variables in one line.
# SOLUTION= 
# a = b = c = 24
# print("value of a :" ,a)
# print("value of b :" ,b )
# print("value of c :" ,c)

# Q-3 Swap two variables using a temporary variable.
# SOLUTION = 
# a = 28
# b = 37
# print("before swapping")
# print(a) , print(b)
# temp=a
# a = b
# b = temp
# print("after swapping")
# print(a) , print(b)

#Q-4 Swap two variables using a temporary variable.
# SOLUTION= 
# a = 45
# b = 78
# by traditional method 
# a , b = b , a
# print(a , b)

#Q-5 Take two numbers as input, store them in variables, and print their sum.
# num1 = int(input("enter your first number:" ))
# num2 = int(input("enter your second number:" ))
# sum = num1 + num2
# print(sum)

# Q-6 Create two integer variables a and b, and print:
# a + b
# a - b
# a * b
# a / b
# a % b
# a ** b
# SOLUTION=
# a = 68
# b = 4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)

# Q-7 Create a variable with your full name and print only your first name.
# SOLUTION = 
# name ="Harmehar KAUR"
# print(name.split()[0])   # first name
# print(name.split()[-1])  # last name

#Q-8 Take input for a number and print its square using a variable
# a = int(input("enter your number :" ))
# b = a*a
# print(b)

#Q-9 Store 5 subject marks in separate variables, then calculate total and average.
# SOLUTION=
# sub1 = 86
# sub2 = 82
# sub3 = 80
# sub4 = 89
# sub5 = 90
# total = sub1+sub2+sub3+sub4+sub5
# print(total)
# average = total/5
# print(average)

#Q-10 Assign a float number to a variable, convert it to int, and print both.
# SOLUTION=
# var_float = 85.4
# var_int =int(var_float)
# print(var_float) 
# print(var_int)

#Q-11 Show that Python allows reassignment → assign x = 5, then x = "Hello", print x.
# SOLUTION=
# x = 5
# x = "Hello"
# print(x)
# from here concluded that python allows reassignment

#Q-12 Multiple assignment: x, y, z = 10, 20, 30. Print each variable.
#SOLUTION= 
#  x , y , z = 10 , 20 , 30
# print("value of x :" ,x)
# print("value of y :" ,y)
# print("value of z :" ,z)

#Q-13 Assign the same string "Python" to three different variables in one line.
# SOLUTION=
# a = b = c = "HELLO"
# print(a , b, c)

# Q-14 Use variables to calculate the area of a rectangle (length × width).
# SOLUTION =
# LENGTH=int(input("enter the length:" ))
# BREADTH=int(input("enter the breadth:" ))
# AREA = LENGTH*BREADTH
# print("AREA OF THE RECTANGLE:" ,AREA)

# Q-15 Use variables to calculate the area of a circle (πr²).
# SOLUTION =
# RADIUS= int(input("enter the radius of circle:" ))
# AREA=3.14*RADIUS*RADIUS
# print("AREA OF THE CIRCLE:" ,AREA)

# Q-16 Take user input for two numbers and print which is greater using variables.
# a = input("enter the first number:" )
# b = input("enter the second number:" )
# if a>b:
#     print("a is greatest")
# elif b>a:
#     print(" b is greatest")
# else:
#     print("both numbers are equal")

# Q-17 Write a program that swaps values of x and y without using + or - (hint: use multiplication/division or XOR).
# SOLUTION=
# x = 10
# y = 20
# print("Before swapping: x =", x, "y =", y)

# Step 1: Multiply
# x = x * y   # x = 10 * 20 = 200

# Step 2: Divide to find new y
# y = x // y  # y = 200 // 20 = 10

# Step 3: Divide again to find new x
# x = x // y  # x = 200 // 10 = 20

# print("After swapping: x =", x, "y =", y)

#Q-18 Store your birth year in a variable and calculate your current age.
# SOLUTION=
# Birthyear= int(input("enter your birth year:" ))
# Currentyear=int(input("enter current year:" ))
# Age = int(Currentyear-Birthyear)
# print("YOUR AGE IS :" , Age) 

#Q-19 Assign a value to a variable and check if it’s even or odd using %.
# SOLUTION=
# number = int(input("enter a number:" ))
# if number%2==0:
#     print("number is even")
# else:
#     print("number is odd")

#Q-20 Store two strings in variables and concatenate them with a space.
#SOLUTION =
# str1="good"
# str2="vibes"
# finalstr= str1+" " +str2
# print(finalstr) 

#Q-21 Assign marks for 3 subjects in variables, then use conditionals to print grade (A/B/C/Fail).
# SOLUTION =
# sub1 = int(input("enter sub1 marks:" ))
# sub2 = int(input("enter sub2 marks:" ))
# sub3 = int(input("enter sub3 marks:" ))
# total= (sub1 + sub2 + sub3)/3
# if total>=90:
#     print("grade:A")
# elif total>=70 and total<90:
#     print("grade:B")
# elif total>=40 and total<70:
#     print("grade:C")
# else:
#     print("grade:D")

# Q-22 Take input for name and age variables, and print: "Hello, <name>. You will turn 100 in year <year>."
# SOLUTION=
# name=input("enter your name :" )
# age=int(input("enter your age:" ))

# current_year = 2025
# year_turn_100 = current_year + (100 - age)

# print("Hello", name ,"You will turn 100 in year", year_turn_100)

#Q-23 CONVERT TEMPERATURE INTO FAHRENHEIT

#SOLUTION=
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} °C = {fahrenheit} °F")

#Q-24 Write a program to calculate Simple Interest (SI = P*R*T/100) using variables.
# SOLUTION=
# p=int(input("enter prinicipal value:" ))
# r=int(input("enter rate:" ))
# t=int(input("enter time period:" ))
# simple_interest= p*r*t/100
# print("simple interest=" ,simple_interest)

#Q-25 Write a program that stores your height in cm and weight in kg in variables, then calculates BMI.
# SOLUTION=
# height=float(input('enter your height:' ))
# weight=float(input('enter your weight:' ))
# BMI= int(weight/height*height)
# print("BMI=" ,BMI)