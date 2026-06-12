# Indexing is the way to access individual elements from a sequence (like strings, lists, tuples) using their position. Think of it like an address system—each element has a position number that lets you retrieve it
# simple example of indexing in a string
str1 = "hello world"
print(str1[0]) #h
print(str1[6]) #w


# 1. Zero-Based Indexing
# Python uses zero-based indexing — the first element is at index 0, not 1.
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# 2. Negative Indexing
# Access elements from the end using negative numbers:
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[-1]) # Cherry
print(fruits[-2]) # Banana


# 3. Out of Range
# Accessing an index that doesn't exist raises an IndexError:
num = [1, 2, 3]
print(num[3]) # IndexError: list index out of range


# Essential Topics Related to Indexing
# 1. SLICING (Very Important! 🌟)
# Extract a portion of a sequence using [start:stop:step]
# Basic slicing [start:stop]
str = "Python programming is fun"
print(str[0:6]) # Python
print(str[:6]) # programming
print(str[7:]) # programming is fun

# Step parameter
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(str[::2]) #every 2nd element
print(list1[::3]) #every 3rd element

# 2. Multi-Dimensional Indexing (For Lists/Arrays)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][0])

# 3. Dictionary/Mapping Access
# Dictionaries use keys instead of numeric indices:
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "course": ["android", "ios", "flutter"]
}
print(person["course"][2]) # Alice


'''enumerate() is a game-changer for loops.
 What is enumerate()?
 enumerate() gives you both the index AND the value when looping through a sequence. It's much cleaner than manually tracking indices.'''
#old way
fruits = ["Apple", "Banana", "Cherry"]
for i in range(len(fruits)):
    print(f"index: {i}, value:{fruits[i]}")

#new way with enumerate()
fruits = ["Banana", "Licy", "fruits", "Apple"]
for index, value in enumerate(fruits):
    print(index[2]);