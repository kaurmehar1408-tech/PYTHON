# Q13. Write a program to reverse a number using a while loop.
# python
# Sample Input: 12345
# Expected Output: Reversed number = 54321

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0 :
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print(reversed_num)
