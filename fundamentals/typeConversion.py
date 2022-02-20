#bool = true/false
#int= whole numbers
#str= anything inside quotations
#float = decimal numbers

var= (123)
print(type(var)) #<class 'int'>

var1= (123.456)
print(type(var1)) #<class 'float'>

var2= ("123.456")
print(type(var2)) # <class 'str'>

var3= ('broadway')
print(type(var3)) # <class 'str'>

var4= ("""broadway""")
print(type(var4)) # <class 'str'>

var5= ('''broadway''')
print(type(var5)) # <class 'str'>

var6=True
print(type(var6)) #<class 'bool'>

var7=()
print(type(var7)) #<class 'tuple'>

#type conversion

#str to int
var9= '123'
print ("var9 type is: " , type(var9))
var10= int(var9)
print("var10 type is: " ,type(var10))

#str to float
var11= '123'
print ("var11 type is: " , type(var11))
var12= float(var11)
print("var12 type is: ",type(var12))


#others to string
var15= True
var16= str(var15)
print("var 16 :" ,type(var16))

#str to bool
var13= '-1'
print ("var13 type is: ", type(var13))
var14= bool(var13)
print("var14 type is: ",type(var14))
print ("var 14:", var14)

a = 1
print(isinstance(a, bool)) #False
print(isinstance(a, str)) #False
print(isinstance(a, float)) #False
print(isinstance(a, int)) #True
