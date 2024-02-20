
class Student:
    firstName = ""
    lastName = ""
    
    def __init__(self, first, second):
        self.firstName= first
        self.lastName = second

    def getFullName(self):
        return self.firstName +" "+ self.lastName

jay = Student("jay", "krishna")
print(jay.getFullName())

bhanu = Student("Bhanu", "Prakassh")
print(bhanu.getFullName())

