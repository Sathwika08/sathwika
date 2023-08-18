#loop control statements
#break
#continue
#pass

for num in range(1, 6):
    if num == 3:
        break
    print(num)
    
for num in range(1,6):
    if num%2==0:
        continue
    print(num)  
    
for num in range (1,6):
    pass

for i in range (1,10):
    if i==5:
        break
    print(i)      

my_list=[1,2,3,4,5]
for num in my_list:
    if num==3:
        continue
    print(num)
    
my_list = [1, 2, 3, 4, 5]
for num in my_list:
    if num == 4:
        continue
    print(num * 2) 
    
num=1
while num<=20:
    if num==16:
        break
    print(num)
    num+=1    
    
