
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
