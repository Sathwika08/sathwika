#Nested conditional statements
#Nested if
x=25 
if x>0:
    print("x is positive")
    if x%2==0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is not positive")
    
#Nested if-elif-else
score=85
if score >90:
    print("grade: A")
elif score >80:
    print("grade: B")
    if score >=85:
        print("GOOD JOB!")
    elif score >70:
        print("grade: C")
    else:
        print("grade: below c")
        
    x=20
    if x>0:
        print("given number is positive")
        if x%2==0:
            print(" given number is even")
        else:
            print("given number is odd")
            if x==0:
                print("given number is zero")  
                
x=-5
if x<0:
    print("x is negetive")
else:
    print("x is positive")
    
age=80
if age<4:
    print("baby")
elif age<12:
    print("child")
elif age<18:
    print("teenage")
elif age<30:
    print("adult")
else:
    print("senior citizen")      
    
year=2023
if year%400==0:
    print("leap year : feb has 29 days")
else:
    print("not a leap year : feb has 28 days")             
                 
    
    
        