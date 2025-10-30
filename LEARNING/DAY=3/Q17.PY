# Q17. Write a program to check if a number is prime using a for loop.
# python
# Sample Input: 17
# Expected Output: 17 is a prime number

num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print("not a prime number")
        break
    else:
        print("is a prime number")
        break
    