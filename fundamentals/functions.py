'''def helloFunc(a):
    print ("hello ", a)
    return
helloFunc('Jeena')

def sumFunc(a,b):
    print(a+b)
    return
sumFunc(2,3)

def subFunc(a,b):
    if (a<b):
        print(b-a)
    else:
        print(a-b)
    return
subFunc(5,3)
'''
def f2_1(message):
    print(message)

str1 = "Broadway InfoSys"
f2_1(str1) # str1 Argument (value to send to function)
f2_1("John Bista")
f2_1("Unanyan Thapa")


def f3_1():
    return 1

var1 = f3_1()
print(var1)

def f1_6(num1):
    if num1 == 1:
        return 1
    else:
        return num1 +  f1_6(num1 - 1)

print(f1_6(5))

#anonymous/ lambda function
obj1= lambda str1:str1
print(obj1("Jeena"))

calc= lambda x,y :x+y
print(calc(5,12))
