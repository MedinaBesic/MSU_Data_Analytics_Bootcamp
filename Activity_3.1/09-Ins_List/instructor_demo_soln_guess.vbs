# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80]
print(myList)
#['Jacob', 25, 'Ahmed', 80]

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)
#['Jacob', 25, 'Ahmed', 80, 'Matt']

# Returns the index of the first object with a matching value
print(myList.index("Matt"))
##############################What does this mean? 
#4

# Changes a specified element within an List at the given index
myList[3] = 85
print(myList)
#['Jacob', 25, 'Ahmed', 85, 'Matt']

# Returns the length of the List
print(len(myList))
#5

# Removes a specified object from an List
myList.remove("Matt")
print(myList)
#['Jacob', 25, 'Ahmed', 85]

# Removes the object at the index specified
myList.pop(0)
myList.pop(0)
print(myList)
#['Ahmed', 85]

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)
#('Python', 100, 'VBA', False)