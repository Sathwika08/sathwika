#nested loops
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  
    
n=5  
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
    
    
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()  
    
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
print()
        
for i in range (1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
    
for i in range(5):
     if i == 0 or i == 4:
         print("*" * 5)
     else:
         print("*" + " " * 3 +"*")
print() 

sum = 0
for i in range(1, 6):
    for j in range(1, i + 1):
        sum += j
print(sum)
print()

for i in range(5, 0, -1):
    for j in range(1,5):
        print(i * j, end=" ")
    print()
print()

for i in range(1,6):
    print("*" * i)
print()




        
                
