# working with dictionaries
student={
 "name": "sathwika",
"age": 25,
"major":"Computer Science",
"gpa": 3.8
}

# Modifying value
student["gpa"] = 4.0

# Adding new key-value pair
student["university"] = "XYZ University"
print(student)

student = {
    "name": "Dodagatta Nihar",
    "age": 25,
    "major": "Computer Science",
    "gpa": 3.8
}

# Get keys and values
keys = student.keys()
values = student.values()

print(keys)   
print(values)

employee = {"name": "Alice", "age": 30}
employee["age"] = 35
print("1. Modified employee dictionary:", employee)

# Question 2
fruits = {"apple": 5, "banana": 7}
fruits["orange"] = 3
print("2. Added key-value pair to fruits dictionary:", fruits)

# Question 3
inventory = {"apple": 10, "banana": 15, "sugar": 2}
del inventory["sugar"]
print("3. Removed key-value pair from inventory dictionary:", inventory)

# Question 4
stock = {"apple": 10, "banana": 15}
item_name = "banana"
if item_name in stock:
    stock[item_name] += 1
print("4. Updated stock dictionary:", stock)

# Question 5
scores = {"Bob": 85, "Charlie": 90, "Alice": 78}
key = "Alice"
if key in scores:
    print("5. Key found in scores dictionary. Value:", scores[key])
else:
    print("5. Key not found.")
