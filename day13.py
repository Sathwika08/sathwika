#string methods
#length of string : len()

string=("hello world")
length=len(string)
print(length)

#converting string to lower case :lower()
string=("SaThWiKa")
lower_case=string.lower()
print(lower_case)

#converting string to upper case : upper()
string=("sathwika")
upper_case=string.upper()
print(upper_case)

#removes leading and trailing whitespaces in the string : strip()
string=("Hello World")
stripped_string=string.strip()
print(stripped_string)

#replacement of substring replace()
string="hello sathwika"
new_string=string.replace("hello","abhi")
print(new_string)

#spliting string into list of substrings : split()
string="apple,banana,orange"
splitted_string=string.split(",")
print(splitted_string)

#startswith
string="hii iam sathwika"
result=string.startswith("hii")
print(result)

#endswith
string="hii iam sathwika"
result=string.endswith("hii")
print(result)

#count()
string="sathwika"
count=string.count("a")
print(count)

#find()
string="sathwika"
find=string.find("w")
print(find)

#isdigit()
string="123456"
isdigit=string.isdigit()
print(isdigit)

#isalpha()
string="sathwika"
isalpha=string.isalpha()
print(isalpha)

string="I LOVE PYTHON PROGRAMMING"
words=string.split()
for word in words:
    print(words)
    
    
    