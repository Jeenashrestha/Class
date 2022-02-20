"""class Person():
    pid = "1"
    name = "Jeena"
    address = "Nepal"

person1= Person()
print(person1.pid, person1.name,person1.address)

person1.pid= 10 #appending an attribute
print(person1.pid, person1.name,person1.address)"""

"""class Person():
    def __init__(self): #initializer function| constructor|| self calling when object of this class is created
        self.pid ="1"
        self.name ="Jeena"
        self.address = "Nepal"
p1= Person()

person1= Person()
print(person1.pid, person1.name,person1.address)

person1.id= "3"
person1.name = "Selena"
print(person1.pid, person1.name,person1.address)
"""
"""
class Person():
    def __init__(self, pid, name, address):
        self.pid = pid
        self.name = name
        self.address = address
    def __str__(self):
        return str(self.pid) +" "+self.name+" " +self.address
person1=Person(1, "Jeena", "Nepal")
print(person1.pid, person1.name,person1.address)
print(person1)
"""
class Person():
    def __init__(self, pid, name, address):
        self.pid = pid
        self.name = name
        self.address = address

        # getters
        def getPid(self):
            return self.pid

        def getName(self):
            return self.name

        def getAddress(self):
            return self.address

        # def setters
        def setPid(self, pid):
            self.pid = pid

        def setName(self, name):
            self.name = name

        def setAddress(self, address):
            self.address = address

    def __str__(self):
        return str(self.pid) + " " + self.name + " " + self.address

person1 = Person(1, "Jeena", "Nepal")
print(person1)