#1. Assignment operators

#1.1. Simple assignment operator
var1 = 5
var2 = var1
print(var1)
print(var2)

a, b = True, False
print(a, b)

#1.2 Multiple assignment operator
var1 = var2 = 100
print(var1, var2)

#1.3 Short-hand assignment operator

c=6
d=6+5
print(d)
c+=5
print(c)

print("-----------------------------------------------------------")

#2 Airthmetic operators (+, -, *, %, /, **, //, pow, sqrt)
#2.1. Add
print(True+True)
print(True+False)
print(True+False)
print("Kathmandu"+ ", "+ "Nepal")
print(34+32)
print(1.23+10)
print(1.23+10.23)
#print(True+"Kathmandu") (Type Error: cannot be added as it is of different type)
print(True+123)
#print(1+"one") (Type Error: cannot be added as it is of different type)
#print(1.1+ "one") (Type Error: cannot be added as it is of different type)

print("-----------------------------------------------------------")
#1.2 Subtract
print(True-True)
print(True-False)
print(True-False)
#print("Kathmandu"- ", "- "Nepal") (Strings cannot be subtracted)
print(34-32)
print(1.23-10)
print(1.23-10.23)
#print(True-"Kathmandu") (Type Error: cannot be added as it is of different type)
print(True-123)
#print(1-"one") (Type Error: cannot be added as it is of different type)
#print(1.1-"one") (Type Error: cannot be added as it is of different type)
print("-----------------------------------------------------------")
#1.3 Multiply
print(True*False)
print(1.2*1.2)
print(1*1.2)
print(1*5)
print("String "*2)
print("-----------------------------------------------------------")

#1.4 Division
print(12/3)
print(12/3.1)
print(12.3/3)
print(10//3)
print(10%3)
#print ("Jeena"/1) (TypeError)

print("-----------------------------------------------------------")

#1.5Power
import math
print(pow(2,3))
print(2**3)

#1.6 Sqrt
print(math.sqrt(16))

print("-----------------------------------------------------------")
#3. Relational Operator [==, !=, >, < , >=, <=]
#3.1 == {returns True if both values are equal else returns false}
print (10==45)
print (10.1==10.1)
print ("jeena"=="jeena")
print(12==12.5)

print("-----------------------------------------------------------")

#3.2 != {returns True if both values are not equal else returns false}
print (10!=45)
print (10.1!=10.1)
print ("jeena"!="jeena")
print(12!=12.5)

print("-----------------------------------------------------------")

#3.3. > {if left side value is greater than right, it returns true else returns false}

print(10>45)
print(13>10.1)
print("jeena">"jeena")
print("c">"b")
print(12>12.5)

print("-----------------------------------------------------------")

#3.4. < {if right side value is greater than left, it returns true else returns false}
print(10<45)
print(13<10.1)
print("jeena"<"apple")
print(12<12.5)

print("-----------------------------------------------------------")

#3.5. <= {if left side value is greater than or equals to right value, it returns true else returns false}

print(10<=45)
print(13<=10.1)
print("jeena"<="jeena")
print("c"<="b")
print(12<=12.5)

print("-----------------------------------------------------------")
#4. Logical Operators (Compares multiple conditions to give a single result)
#AND , OR

print((1==1) and (2==2))
print((1<2) and (2>3))
print((1>=2) and (2>=3))

print((1==1) or (2==2))
print((1<2) or (2>3))
print((1>=2) or (2>=3))

#NOT
print (not True)
print (not False)
print (not(1>2))

print("-----------------------------------------------------------")

#5. Bitwise operators (Only applicable in low level , python is high level language)

#6. Other operators
#{}, (), .

#OPERATORS PRECEDENCE AND ASSOCIATIVITY
print(1+2/3*6/2+3-5)

