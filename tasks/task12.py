'''
Enter id: 1
Enter name: Raj
Enter class: 7
Enter section : A
Enter exam: First terminal
Enter Marks obtained
SUB-1 : 45
SUB-2 : 65
SUB-3 : 89
___________________________________________________________________________
TOTAL:
AVERAGE:
RESULT:
GRADE:
Thank you!
_____________________________________________________________________________
'''

def studentInfo(id, name, grade, section, sub1, sub2, sub3 ):
    print("ID: ", id)
    print("NAME: ", name)
    print("grade: ", grade, section)
    print("Sub1: ", sub1)
    print("Sub2: ", sub2)
    print("Sub3: ", sub3)
    total = sub1+sub2+sub3
    print("Total: ", total)
    average = total/3
    print("Average: ", average)
    if (sub1>=40 and sub2>=40 and sub3>=40):
        result = "pass"
    else:
        result = "fail"
    print("Result: ", result)

    percentage = (total/300)*100
    print("Percentage: ", percentage,"%")
    return

id = input("Enter id: ")
name = input("Enter name: ")
grade = input("Enter grade: ")
section = input("Enter section: ")
print("Enter Marks")
sub1 = int(input("Sub1: "))
sub2 = int(input("Sub2: "))
sub3 = int(input("Sub3: "))

studentInfo(id, name, grade, section, sub1, sub2, sub3)