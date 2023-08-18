#tuples
#tuple packing and unpacking
person = ("John", 30, "New York")
name, age, city = person

print(name)  # Output: "John"
print(age)   # Output: 30
print(city)  # Output: "New York"
#tuple functions len(),min(),max()
numbers = (5, 2, 8, 1, 7)

# Length of the tuple
length = len(numbers)
print(length)  

# Maximum and minimum elements in the tuple
maximum = max(numbers)
minimum = min(numbers)
print(maximum, minimum) 

#tuple concatination and repetation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
result = tuple1 + tuple2
print(result)  

# Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple) 

 

