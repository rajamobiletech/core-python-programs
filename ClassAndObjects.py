
class Employee:
    firstName = "King"
    lastName = "Maker"
    
    def __init__(self):
        print("Init code")


    def getFullName(self):
        return self.firstName +" "+ self.lastName

s1 = Employee()
print(s1.getFullName())

s2 = Employee()
print(s2.getFullName())


name = "Raja"
 
string = "My name is {}. Article is about {}.".format(name, "Python")

print(string)