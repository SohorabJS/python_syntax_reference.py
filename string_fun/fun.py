# 2. BASIC STRING METHODS
# text = "Hello World"

# print(text.upper())        # HELLO WORLD
# print(text.lower())        # hello world
# print(text.capitalize())   # Hello world (first char uppercase)
# print(text.title())        # Hello World (each word capitalized)
# print(text.swapcase())     # hELLO wORLD
 









# Searching and Checking
# text2 = "Python is great programing language"

# print(text2.find("is", 5))
# print(text2.rfind("on"))
# print(text2.count("o"))
# print(text2.index("great"))
# Checking
# print(text2.startswith("Python"))
# print(text2.endswith("e"))
# print(text2.isalpha())
# print("23344".isdigit())
# print(text2.islower())
# print(text2.isupper())
# print(text2.isspace())

# Trimming and Padding
# text = "Python";
# print(text.strip())              # "Python" (remove from both ends)
# print(text.lstrip())             # "Python  " (left trim)
# print(text.rstrip())             # "  Python" (right trim)

# url = "***Python***"
# print(url.strip("*"))

# # Padding
# text = "HI"
# print(text.rjust(10))
# print(text.ljust(10))
# print(text.center(10))
# print(text.zfill(10))

# Replace and Split

text = "Banana, Apple, cherry"
# print(text.replace("B", "b"))    
# print(text.replace("a", "A",1))   # Apple,banana,cherry (limit to 1)

# # Split 
# fruits = text.split(",")
# print(fruits);

# split with limit
# fruits = text.split(",", 1) #it will appear as resuld ['Banana', 'Apple, cherry'];

# Split by any whitespace
# text2 = "hello     world\npython";
# print(text2.split());   # ['Hello', 'World', 'Python']

#splitline
text3 = "line1\nline2\nline3"
print(text3.splitlines()) # ['line1', 'line2', 'line3'];



