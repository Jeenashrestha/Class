class Student():
    def __init__(self, id, name, grade, section, sub1,sub2,sub3):
        self.id=id
        self.name=name
        self.grade= grade
        self.section=section
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def result(self):
        if (self.sub1 >= 40 and self.sub2 >= 40 and self.sub3 >= 40):
            result = "pass"
        else:
            result ="fail"
        print("Result: ", result)

    def grades(self):
        total= str(self.sub1+self.sub2+self.sub3)
        print("Total: ",total)
        average= self.sub1+self.sub2+self.sub3/3
        print("Average: ",average)
    def __str__(self):
        return "ID: "+str(self.id) +"\nName: "+self.name+"\nGrade: " +str(self.grade)+self.section+"\nSub1: "+str(self.sub1)+"\nSub2: "+str(self.sub2)+"\nSub3: "+str(self.sub3)


id = input("Enter id: ")
name = input("Enter name: ")
grade = input("Enter grade: ")
section = input("Enter section: ")
print("Enter Marks")
sub1 = int(input("Sub1: "))
sub2 = int(input("Sub2: "))
sub3 = int(input("Sub3: "))
student1=Student(id,name,grade,section, sub1,sub2, sub3)
print(student1)
student1.result()
student1.grades()