# Error Handling (Exceptions)
# 1. Syntax Error
# 2. Runtime Error
# 3. Logical Error
# 1. Syntax Error
#print ("hello) #Error
print("hello") #solution
# 2. Runtime Error
"""
num1 = int(input("enter first no : "))
num2 = int(input("enter second no : "))
num3 =  num1 + num2
print("result : ", num3)
"""

# 3. Logical Error
"""
#Division by zero error
import  sys
num1=10
num2=10
div=0
try:
    div=num1/num2
    print(div)
except:
    print("Error: ", sys.exc_info()[1])
finally:
    del num1
    del num2
    del div
"""
####USER-DEFINED EXCEPTIONS
"""
class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
"""
num1 = None
num2 = None
num3 = None
try:
    # input, process, output
    num1 = int(input("Enter first no : "))
    num2 = int(input("Enter second no : "))
    num3 = num1 + num2
    print("Sum : ", num3)
except:
    # Error Message
    print("Error : ", sys.exc_info()[1])
finally:
    # Exit
    del num1
    del num2
    del num3