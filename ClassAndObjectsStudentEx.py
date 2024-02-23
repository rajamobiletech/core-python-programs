
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

print("______________________________________________________________________________________________________________")



#Class: A class is defined using the class keyword followed by the class name. 
#It serves as a template for creating objects.

#ex1:-
class school:
    name = ""
    phnumber = ""
    adharno = ""
    marks = ""
    def __init__(self,name,phnumber,adharno,marks):
        self.name = name
        self.phnumber = phnumber
        self.adharno = adharno
        self.marks = marks
    def an(self):
        return self.name +" "+self.phnumber +" "+self.adharno +" "+ self.marks
     
a=school("balayya",  "xxxxxxxxxx",   "25461xxxxxx",   "70")
print(a.an())
b=school("hanumanth",   "89133333333",   "xxxxxxxxxxx",   "83")
print(b.an()) 
c=school("tarak","xxxxxxxxxx","484654654684","51")
print(c.an())



#ex2:-
class room:

    firstroom = ""
    secondroom = ""

    def __init__(self,roomno1,roomno2):
        self.firstroom = roomno1
        self.secondroom = roomno2

    def roomname (self):
        return self.firstroom +" "+ self.secondroom
    

room1 = room("pythonroom","pythonclasses")
print(room1.roomname())

room2 = room("javaroom","javaclasses")
print(room2.roomname())
