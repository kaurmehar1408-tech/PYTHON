# Q16. Write a program to find the sum of digits of a number using a while loop.
# python
# Sample Input: 1234
# Expected Output: Sum of digits = 10

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print(sum)