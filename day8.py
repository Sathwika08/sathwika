#logical operators
# and 
# or
# not
# true and true => true 
# true and false => false 
# false and true => false 
# false and false => false

#true or true => true
#true or false => true
#false or true => true
#false or false =>false

a="true"
b="false"
result= a and b
print(result)


a= "true"
b="true"
result=a and b
print(result)

X=10
Y=20
result=(X>0) or (Y<30)
print(result)

a ="true"
result=not a
print(result)

x=10
y=20
z=30 
result=(x>y) or (x<y) and (x>=z)
print(result)

