
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


print("================================================================================================================")
class college:
    firstName = ""
    lastName = ""
    group=""
    age=""

    def __init__(self, first, second,third,fourth):
        self.firstName= first
        self.lastName = second
        self.group=third
        self.age=fourth

    def studentinformation(self):
        return self.firstName +" "+ self.lastName +" "+ self.group+" "+ self.age

one = college("virat","kohli","mpc","24")
print(one.studentinformation())
second= college("pavan","kalyan","mpc","25")
print(second.studentinformation())
three=college("AB","devilliears","mpc","23")
print(three.studentinformation())
four=college("faf","duplicis","mpc","24")
print(four.studentinformation())
five=college("mad","max","mpc","25")
print(five.studentinformation())