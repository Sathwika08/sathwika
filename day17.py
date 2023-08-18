#Lists
#accessing elements
fruits=["apple","banana","mango"]
print(fruits[0])
print(fruits[2])

#modifying elements
fruits=["apple","mango"]
fruits[1]="grape"
print(fruits)

#list operations
#1.concatination
#2.repetation

list1=[1,2,3]
list2=[6,5,4]
result=list1+list2
print(result)

list1=[1,2,3]
repetation=list1*3
print(repetation)

#list methods
#1.adding
list=["1","2","3"]
list.append("5")
print(list)
#2.removing
list=["1","2","3"]
list.remove("3")
print(list)
#sorting
list=["1","2","3"]
list.sort()
print(list)


numbers=[1,2,3,4,5]
for num in numbers:
    print(num)
    
def sum_of_numbers(num_list):
    return sum(num_list)

input_list = [1, 2, 3, 4, 5]
result = sum_of_numbers(input_list)
print(result) 

list=[10,20,30,40]
result=max(list)
print(result)

