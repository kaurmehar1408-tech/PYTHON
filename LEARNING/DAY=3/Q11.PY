# Q11. Write a program to find the factorial of a number using a while loop.
# python
# Sample Input: 5
# Expected Output: Factorial = 120
# (5! = 5 × 4 × 3 × 2 × 1 = 120)

n = int(input("Enter a number: "))
factorial = 1
i = 1
while i<=n:
    factorial *=i
    i = i+1
print(factorial)
