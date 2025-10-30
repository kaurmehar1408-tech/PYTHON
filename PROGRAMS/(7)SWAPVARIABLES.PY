# Method-1 : Using a temporary variable
a = 12
b = 13
print("Before Swapping (Using Temporary Variable)" , a ,b)

temp = a
a = b
b = temp

print("After Swapping (Using Temporary Variable)" , a ,b)

# Method-2 : Without using a temporary variable
a , b = 5 , 7
print("Before Swapping (Without Using Temporary Variable)" , a ,b)
a , b = b , a
print("After Swapping (Without Using Temporary Variable)" , a ,b)