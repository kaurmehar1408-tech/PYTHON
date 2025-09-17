# 📒 Python Notes — Integers, Floats & Booleans

# 🔢 1. Integers (int)
# Whole numbers (positive, negative, or zero).
# No decimal point.
# Example: 10, -25, 0.
# In Python, there is no limit to the size of integers (unlike C/Java).

# ✅ Common Operations
# a = 10
# b = 3

# print(a + b)   # 13
# print(a - b)   # 7
# print(a * b)   # 30
# print(a / b)   # 3.333... (float division)
# print(a // b)  # 3 (integer division - floor division)
# print(a % b)   # 1 (remainder)
# print(a ** b)  # 1000 (exponent: 10^3)

# 🔢 2. Floats (float)
# Numbers with decimals.
# Example: 10.5, -2.3, 0.0.
# Can also be written in scientific notation: 1.5e3 → 1500.0.

# ✅ Type Conversion
# x = 10
# y = 3.5
# print(float(x))   # 10.0
# print(int(y))     # 3 (decimal part removed, not rounded)

# ✅ Useful Functions
# import math
# print(round(3.14159, 2))  # 3.14
# print(math.sqrt(49))      # 7.0
# print(pow(2, 5))          # 32

# ✅ 3. Type Checking
# print(type(10))      # <class 'int'>
# print(type(10.0))    # <class 'float'>
# print(type("10"))    # <class 'str'>

# 🟢 4. Booleans (bool)

# Only two values: True and False.
# Type of comparison/logical results.
# Example:
# print(5 > 3)   # True
# print(5 == 10) # False

# 🔹 Truthy and Falsy Values
# Python treats some values as False automatically:
# 0
# 0.0
# None
# "" (empty string)
# [] (empty list)
# {} (empty dict)
# set() (empty set)
# Everything else is True.

# print(bool(0))      # False
# print(bool(1))      # True
# print(bool(""))     # False
# print(bool("Hi"))   # True

# 🔹 Logical Operators
# print(True and False)   # False
# print(True or False)    # True
# print(not True)         # False

# 🔹 Relational Operators
# x = 10
# y = 20

# print(x > y)   # False
# print(x < y)   # True
# print(x == y)  # False
# print(x != y)  # True

# ⚡ Quick Interview Notes
# int + float = float
# print(5 + 2.0)  # 7.0

# Boolean is actually a subtype of int:
# print(True + True)  # 2
# print(False + 5)    # 5

# Use // for integer division (always floor).


# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

# Example
# The following will return False:
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})
# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator	Name	Example	Try it
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	
# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# :=	print(x := 3)	x = 3
# print(x)	

# Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator	Name	Description	Example	Try it
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
# Operator Precedence
# Operator precedence describes the order in which operations are performed.

# Example
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

# print((6 + 3) - (6 + 3))
# Example
# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:

# print(100 + 5 * 3)
# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	Description	Try it
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR	
# If two operators have the same precedence, the expression is evaluated from left to right.

# Example
# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

# print(5 + 4 - 7 + 3)
