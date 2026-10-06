# Defining a function
def func1():
    print('Hello World')
# func1()

# Function in Arguments
def greet(name):
    gr = "hello " + name
    return gr
a = greet("abc")
# print(a)

# Default value in functions
def greet(name = "abc"):
    gr = "hello" + name
    return gr
b = greet()
c = greet("def")
# print(b)
# print(c)

# Recursion 
def factorial(n):
    for i in range(n):
        if i == 0 or i == 1:
            return 1
        else:
            return n*factorial(n-1)
ans = factorial(5)
print(ans)