# conditional statements
# if
# elif(short form of else if)
# else

age=18
if age>=18:
 print("you are an adult.")
 
age=14
if age>=18:
    print("you are an adult.")
else:
    print("you are minor.")
    
age=25
if age<18:
    print("you are minor.")
elif age>18 and age<65:
    print("you are adult.")
else:
    print("you are senior citizen.")
    
    
num=7
if num%2==0:
    print("even")
else:
    print("odd")
    
    
a=10 
b=20 
if a>b:
    print(a)
else:
    print(b)
    
    char = str(input("Enter a character :"))
char = char.lower()
if len(char) == 1:
    if char in ['a','e','i','o','u']:
        print (f"{char} : this character is a Vowel")
    else:
        print("Consonant")
else:
    print("Please enter a single character.")
    
year = int(input("Enter a year :"))
if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0):
    print (f"{year} is a leap year")
else:
    print (f"{year} is not a leap year")
    
    grade=str(input("enter grade:"))
    grade=grade.upper()
    if grade in["A","B","C","D","F"]:
        if grade!="F":
            print("you are pass!")
        else:
           print("you are fail!")
    else:
        print("enter your correct grade!")      
    


    


    
    
