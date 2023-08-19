#sets
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)
print(my_set)  

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set) 

# Question 1: Creating a set
empty_set = set()
print(empty_set)

# Question 2: Adding elements to a set
my_set = {1, 2, 3}
element_to_add = 4
my_set.add(element_to_add)
print(my_set)

# Question 3: Removing an element from a set
my_set = {1, 2, 3, 4}
element_to_remove = 3
my_set.remove(element_to_remove)
print(my_set)

# Question 4: Removing a non-existent element from a set
my_set = {1, 2, 3, 4}
element_to_remove = 5
my_set.discard(element_to_remove)
print(my_set)

# Question 5: Creating a set from a list
my_list = [5, 10, 15, 20]
my_set = set(my_list)
print(my_set)

# Question 6: Adding multiple elements to a set
my_set = {1, 2, 3}
elements_to_add = {4, 5}
my_set.update(elements_to_add)
print(my_set)

# Question 7: Removing elements using discard()
my_set = {10, 20, 30, 40}
elements_to_remove = {20, 50}
my_set.difference_update(elements_to_remove)
print(my_set)