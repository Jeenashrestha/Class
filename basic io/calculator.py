#input 2 numbers and find sum
'''
num1= input("enter first number: ")
num2= input("enter second number: ")
sum = num1+num2
print(sum)

this gives result 1010 because input is in string and is not converted
'''


#correct solution
num1= input("enter first number: ")
num2= input("enter second number: ")
sum = int(num1)+int(num2)
print(sum)

'''
#alternately
n1= int(input("enter first number: "))
n2= int(input("enter second number: "))
total = n1+n2
print(total)
'''