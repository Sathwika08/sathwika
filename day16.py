#strings comparision
string1="sathwika"
string2="SATHWIKA"
if string1==string2:
    print("both strings are equal.")
else:
    print("strings are not equal")
    if string1 != string2:
        print("strings are not equal")
    else:
        print("both strings are equal")
        
string1="sathwika"
string2="sathu" 
if string1 < string2:
    print("string1 comes before string2.")
else:
    print("string1 comes after or is equal to string2.")

if string1 <= string2:
    print("string1 comes before or is equal to string2.")
else:
    print("string1 comes after string2.")

if string1 > string2:
    print("string1 comes after string2.")
else:
    print("string1 comes before or is equal to string2.")

if string1 >= string2:
    print("string1 comes after or is equal to string2.")
else:
    print("string1 comes before string2.")
    
string1="Python"
string2="python" 
if string1==string2:
    print("true") 
else:
    print("false")  
    
string=""
if string=="":
    print("true")
else:
    print("false")    