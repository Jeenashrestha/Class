str1=str()
str1=str1.__add__("ADD THIS")
print(type(str1))
print(str1)

str2='''I am at home'''
print(str2.__add__("EXECUTIVE SUMMARY"))

str3= "apple is a fruit"
tmpstr= str3.capitalize()
print(tmpstr)

a="admin"
b="AdMin"
result= (a==b)
print(result) #False because different in ascii value

c=a.casefold() #converts to small case
d=b.casefold()
r1= (c==d)
print(r1)

s1= "broadway"
str2=(s1.center(20,'*'))
print(str2)

s1= "broadway"
str2=(s1.ljust(20,'*'))
print(str2)

s1= "broadway"
s2=(s1.rjust(20,'*'))
print(s2)

print(s1.count("a"))

print(s1.endswith("y"))

str1 = "SN\tNAME\tADDRESS"
str2 = "1\tJeena\tKathmand"
print(str1)
print(str2)

print(str1.expandtabs(20))
print(str2.expandtabs(20))

print ()
st1="THIS IS THE STRING"
result = st1.find("STRING", 0, -1)
print(result)

str1 ="""Structural pattern matching has been added in the form of a match statement and case statements of patterns with associated actions. Patterns consist of sequences, mappings, primitive data types as well as class instances. Pattern matching enables programs to extract information from complex data types, branch on the structure of data, and apply specific actions based on different forms of data."""
str2 ="the"
count =str1.count(str2)
print(count)  # times - 2
# position ?
result1 = str1.find(str2, 0, len(str1)-1)
print(result1)
result2 = str1.find(str2, result1+len(str2), len(str1)-1)
print(result2)

str1 ="""Structural pattern matching has been added in the form of a match statement and case statements of patterns with associated actions. Patterns consist of sequences, mappings, primitive data types as well as class instances. Pattern matching enables programs to extract information from complex data types, branch on the structure of data, and apply specific actions based on different forms of data."""
str2 ="of"
count =str1.count(str2)
print(count)

result1 = str1.find(str2, 0, len(str1)-1)
print(result1)
result2 = str1.find(str2, result1+len(str2), len(str1)-1)
print(result2)
result3 = str1.find(str2, result2+len(str2), len(str1)-1)
print(result3)
result4 = str1.find(str2, result3+len(str2), len(str1)-1)
print(result4)
result5 = str1.find(str2, result4+len(str2), len(str1)-1)
print(result5)


