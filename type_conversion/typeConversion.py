# What is Type Conversion?
# Type conversion is the process of converting data from one data type to another. Python is a dynamically-typed language, but sometimes you need to explicitly change the type of a variable to perform specific operations or ensure data compatibility.

# Basic Example:

#x ="10" # This is a string.If i print x it will print 10 but if i try to add 5 to x it will give an error because x is a string and 5.5 is a float.
# print(type(x)) # <class 'str'>

# x = float(x) # This will convert the string "10" to the float 10.0
# print(type(x)) # <class 'float'>

# sum = x + 5.5  # This will work because Python automatically converts x to a float
# print(sum)  # Output: 15.5


# Types of Type Conversion
# Two Main Categories:
# 1)Implicit Conversion (Automatic by Python)
# 2)Explicit Conversion (Manual by Programmer)

# Implicit Type Conversion
# Implicit type conversion happens automatically when Python converts one data type to another without explicit instructions.
# When Does Python Convert Implicitly?

# 1. During Arithmetic Operations
# x=3
# y=4.5
# result = x + y  # Python converts x to a float before performing the addition
# print(result)  # Output: 7.5
# print(type(result))  # Output: <class 'float'>
 
# Explicit (Manual) Type Conversion
# This is where you manually convert data types using built-in functions. Yes, Python has many manual type conversion functions!

x = "5"
y = 10.0
sum = float(x) + float(y);
print(sum)  # Output: 15.0