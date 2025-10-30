# Q14. Write a program to count the number of digits in a number using a while loop.
# python
# Sample Input: 45678
# Expected Output: Number of digits = 5

num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count +=1
print(count)
