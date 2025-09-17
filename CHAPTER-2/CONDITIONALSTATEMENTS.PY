# ✅ 1. What are Conditional Statements?
# Conditional statements help us execute code based on certain conditions (decision making).
# 👉 Example:
# If it’s raining → Take umbrella
# Else → No umbrella needed

# ✅ 2. Types of Conditional Statements
# 🔹 ✅ Simple if
# age = 20
# if age >= 18:
#     print("Adult")
# 👉 The code block under if runs only if condition is True.

# 🔹 ✅ if - else
# num = 5
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# 👉 Executes if block if condition is True, else executes else.

# 🔹 ✅ if - elif - else
# num = 0
# if num > 0:
#     print("Positive")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative")
# 👉 Multiple conditions checked in order.
# First True condition’s block runs → Rest are skipped.

# ✅ 3. ✅ Nested if
# x = 15
# if x > 10:
#     if x < 20:
#         print("x is between 10 and 20")
# 👉 One if inside another → Used when multiple related conditions.

# ✅ 4. ✅ Shorthand if (One-liner)
# x = 5
# if x == 5: print("x is 5")
# 👉 Good for simple checks.

# ✅ 5. ✅ Ternary Operator (Shorthand if-else)
# age = 18
# status = "Adult" if age >= 18 else "Minor"
# print(status)   # Adult
# 👉 Very useful for assigning values conditionally in a single line.

# ✅ 6. ✅ Common Examples
# Even/Odd check
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Largest of 3 Numbers
# a = 10
# b = 20
# c = 15
# if a > b and a > c:
#     print("a is largest")
# elif b > c:
#     print("b is largest")
# else:
#     print("c is largest")

# Eligibility to vote
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible to vote ✅")
# else:
#     print("Not eligible to vote ❌")

# ✅ 7. Truthy and Falsy Values in Conditionals
# ✅ Truthy → Non-zero numbers, non-empty strings, non-empty lists, etc.
# ❌ Falsy → 0, "", [], {}, None
# if "Python":
#     print("This runs")  # Runs because string is not empty
# if "":
#     print("Won't run")  # Won’t run

# ✅ 8. Best Practices

# Always use proper indentation (4 spaces).
# Avoid complex conditions in one line — use parentheses for clarity.
# Use ternary for simple assignments only.
# Prefer explicit comparisons (e.g., x == 0 instead of if not x for clarity).