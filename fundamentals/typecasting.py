#typecasting (numeric to numeric conversion i.e float->int OR int->float)
print ("integer to float conversion")
i1= 123
f1=float(i1)
print(type(f1))
print("________________________________________")
print("float to integer conversion")
f = 123.123
i=int(f)
print(type(i)) #type of

f = 123.356 #r-edeclare and assign
print(f) #accessing the  variable
print (id(f)) # Memory address of the variable

import sys
g = True
print(sys.getsizeof(g)) #size of the variable

a=True
b=True
print(sys.getsizeof(a), sys.getsizeof(b))
print(id(a), id(b))


