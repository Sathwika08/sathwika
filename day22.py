#working with sets 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of two sets
union_set = set1.union(set2)
print(union_set)  

# Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)  

# Difference between two sets
difference_set = set1.difference(set2)
print(difference_set)  

# Symmetric Difference (elements in either set, but not in both)
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) 

my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  
print(6 not in my_set) 

# Question 1: Symmetric Difference between two sets
set_A = {1, 2, 3}
set_B = {3, 4, 5}
symmetric_difference = set_A.symmetric_difference(set_B)
print(symmetric_difference)

# Question 2: Checking membership in a set
my_set = {1, 2, 3}
element_to_check = 2
is_member = element_to_check in my_set
print(is_member)

# Question 3: Union of two sets
set_A = {1, 2, 3}
set_B = {3, 4, 5}
union_set = set_A.union(set_B)
print(union_set)

# Question 4: Intersection of two sets
set_A = {1, 2, 3}
set_B = {3, 4, 5}
intersection_set = set_A.intersection(set_B)
print(intersection_set)

# Question 5: Difference between two sets
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5}
difference_set = set_A.difference(set_B)
print(difference_set)

# Question 6: Removing duplicate elements from a list using a set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)

# Question 7: Finding the length of a set
my_set = {1, 2, 3, 4, 5}
set_length = len(my_set)
print(set_length)

# Question 8: Checking if one set is a subset of another
set_A = {1, 2, 3}
set_B = {1, 2, 3, 4, 5}
is_subset = set_A.issubset(set_B)
print(is_subset)

# Question 9: Checking if two sets are disjoint
set_A = {1, 2, 3}
set_B = {4, 5, 6}
are_disjoint = set_A.isdisjoint(set_B)
print(are_disjoint)

# Question 10: Removing all elements from a set
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)
