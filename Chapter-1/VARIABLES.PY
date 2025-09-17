# BASICALLY HERE WE ARE BEGINNING WITH OUR FIRST EVER PROGRAMMING LANGUAGE (PYTHON)

# TOPIC-1 {VARIABLES}
# Variables are REFERENCE to a MEMORY LOCATION in the system and can be MANIPULATED during program execution.
# They act as a PLACEHOLDERS OF DATA.
# IN PYTHON , They do not require EXPLICIT declaration of type.

          # RULES FOR NAMING VARIABLES
# 1) Variable names can only contain letters , digits , underscores.
# 2) Variable name cannot be started with a digit.
# 3) They are CASE-SENSITIVE.
# 4) They are DYNAMICALLY-TYPED (same variable can hold different type of values during execution).
# 5) They hold references to the objects , not the actual object themselves.
# 6) Reassigning a value doesn't affect the other variables  referencing the same object unless explicitly updated.

# Scope of Variable:
#The scope of the variable is the area within which the variable has been created. Based on this, a variable can either have a local scope or a global scope.

# Local Variable: local variable is created within a function and can only be used inside that function. Such a variable has a local scope.
#    def func():
#       x = 10  # Local variable
#       print("Inside:", x)
#func() print(x)  # ❌ Error: x is not defined

#Global Scope:- Variables declared outside any function/class are global.Accessible from anywhere in the same module (file).
#x = 100  # Global variable

#    def func():
#       print("Inside:", x)
#func()
#print("Outside:", x)   No Error this time.

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"

