#Arithmetic operators 
# Perform basic mathematical calculations on numbers.

# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Modulus (returns the remainder of a division)

# ** Exponentiation (raises a number to the power of another)
# The core idea — base ** exponent means "multiply the base by itself, exponent times." So 3 ** 4 = 3 × 3 × 3 × 3 = 81. That's it.
x = 3**4


# // Floor Division (returns the quotient of a division, rounded down to the nearest whole number)



#comparison operators
# == Equal to
a=10
b=20
# print(a==b) # False
# != Not equal to
# print(a!=b) # True
# # > Greater than
# print(a>b) # False
# # < Less than
# print(a<b) # True
# # >= Greater than or equal to
# print(a<=b) # True
# <= Less than or equal to
# print(a>=b) # False


# #Logical operators Combine or negate boolean expressions.
# # and Returns True if both statements are true
# print(True and False) # True
# # or Returns True if one of the statements is true
# print(True or False) # True
# # not Returns True if the statement is false
# print(not 0) # False


# Assignment operators
# Assign (or update) values to variables.
# = Assigns a value to a variable
x = 5
# += Adds a value to the variable and assigns the result back to the variable
x += 3  # Equivalent to x = x + 3
# -= Subtracts a value from the variable and assigns the result back to the variable
x -= 2  # Equivalent to x = x - 2
# *= Multiplies the variable by a value and assigns the result back to the variable
x *= 4  # Equivalent to x = x * 4
# /= Divides the variable by a value and assigns the result back to the variable
x /= 2  # Equivalent to x = x / 2
# %= Takes the modulus of the variable by a value and assigns the result back to the variable
x %= 3  # Equivalent to x = x % 3
# **= Raises the variable to the power of a value and assigns the result back to the variable
x **= 2  # Equivalent to x = x ** 2


# comparison_operators
x=5
# print(x==5)
# print(x!=5)
# print(x>10)
# print(x<10)
# print(x>=5)
# print(True == 1 )
# print("ab"=="ab")
# print([1,2,3]==[1,2,3])
print([1,2,3] == [1,3]) # False because they are different objects in memory
# print([1,2,3] <= [1,2,3]) # False because they are different objects in memory
# print(None == None)