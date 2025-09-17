# ✅ 1. What are Loops?
# Loops are used to repeat a block of code multiple times until a condition is met.

# ✅ 2. Types of Loops in Python
# ✅ for loop → Repeats for a sequence of elements (like list, string, range).
# ✅ while loop → Repeats while a condition is True.

# ✅ 3. ✅ for Loop
# 🔹 Syntax
# for variable in sequence:
#     # block of code

# 🔹 Example 1: Loop through list
# fruits = ["apple", "banana", "grapes"]
# for fruit in fruits:
#     print(fruit)

# 🔹 Example 2: Loop through range (0 to 4)
# for i in range(5):
#     print(i)   # prints 0, 1, 2, 3, 4

# ✅ 4. ✅ while Loop
# 🔹 Syntax
# while condition:
#     # block of code
# 🔹 Example: Print numbers from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# ✅ 5. ✅ break and continue
# 👉 break → Exit the loop immediately.
# 👉 continue → Skip current iteration, go to next.

# 🔹 Example with break
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)  # Prints 1 to 4

# 🔹 Example with continue
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)  # Prints 1, 2, 4, 5 (skips 3)

# ✅ 6. ✅ else with Loops
# The else block runs when the loop completes normally (without break).
# 🔹 Example
# for i in range(3):
#     print(i)
# else:
#     print("Loop completed ✅")

# ✅ 7. ✅ Nested Loops
# 👉 One loop inside another.
# for i in range(1, 4):         # Outer loop
#     for j in range(1, 3):     # Inner loop
#         print(i, j)

# ✅ 8. ✅ Infinite Loop (with caution)
# while True:
#     print("Infinite loop – press Ctrl+C to stop!")
#     break   # Avoid infinite running in practice


# 🌟 Key Takeaways

# Use for when looping over sequences (lists, strings, ranges).

# Use while when the loop depends on a condition.

# Use break to exit early, continue to skip iteration.

# else executes when the loop didn’t break.

# Avoid infinite loops unless absolutely necessary.

