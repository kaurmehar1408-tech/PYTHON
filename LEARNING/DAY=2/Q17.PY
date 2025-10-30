# Write a program to check if a person is eligible for a loan: 
# ● Age should be >= 21 and <= 60 
# ● Income should be >= 25000 Print appropriate message

age = int(input("Enter your age: "))
income = float(input("Enter your income: "))
if 21 <= age <= 60 and income >= 25000:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")
    