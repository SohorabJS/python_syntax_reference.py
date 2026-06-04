name = "sourov"
print(type(name)) #str
a = [1,2,3]
print(type(a)) #listS
num = 10
print(type(num)) #int
is_valid = True

#here  we are checking the type of int
print(type(is_valid)) #bool
is_int =-20
print(type(is_int)) #float
big=1_000_000
print(type(big)) #1000000
hexa= 0xFF 
print(type(hexa)) #int
binary= 0b1010
print(type(binary)) #int

#here we are checking the type of float
height = 5.9
print(type(height)) #float
temp= 98.6
print(type(temp)) #float
sci = 1.5e4
print(type(sci)) #float
print(sci) #15000.0
tiny = 2.5e-3
print(type(tiny)) #float
print(tiny) #0.0025
#proving the data type
x = 10.0
print(isinstance(x, float)) #True


#Now checking the data type of boolen
#A bool has exactly two values: True or False. It is a subclass of int — True behaves as 1 and False as 0 in math. Used in conditions, comparisons, and logic.

is_valid=True
print(type(is_valid)) #bool
is_false = False
print(type(is_false))
 
is_greater = 5 < 3
print(type(is_greater), is_greater) #boolS


#Now checking the data type of list
#A list is an ordered, changeable collection of items. Items are indexed starting from 0. You can store any mix of types — ints, strings, other lists, anything. It is the most used container in Python
nums = [1, 2, 3, 4, 5]
print(type(nums)) #list



