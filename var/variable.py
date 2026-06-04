#a variable does not hold value , its a pointer to a value in memory
x = 10
y = x


y=20
#print(x, y)



#lets see with list
a = [1,2,3] #a is a pointer to the list [1,2,3] in memory
b=a #b is also a pointer to the same list [1,2,3] in memory

#print(id(a), id(b)) #both a and b have the same id because they point to the same list in memory

b.append(4)
print(id(a), id(b))
print(f"a:{a}, b:{b}") #both a and b are changed because they point to the same list in memory


