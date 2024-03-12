
name="jaya kRIshna"
#string first letter comes always CAPS
print(name.capitalize())

#string first letter comes always small
print(name.lower())

#string all letters becomes a small
print(name.lower())

#first letter always CAPS and after space also first letter always becomes CAPS
print(name.title())

#in string values is all mixes with numbers and alphabets
print(name.isalnum())

#in string all values are alphabets it gives tru or false
print(name.isalpha())

#in string only write digits it is show true
print(name.isdigit())

#in string only we have space thst time it show true
print(name.isspace())

#in string all string converting into CAPS  
print(name.upper())

#in string checks it is numerics or not
print(name.isnumeric())

#in string find the index number 
print(name.find("hna"))

#in string swaps the particular simple or somthing else
print(name.swapcase())

#count the number of char lenth in string
print(len(name))

print("_____________________________________________________________________")

#import Template:-

#ex1:-
from string import Template
name=(input("enter your language"))
mobile=int(input("enter your mobile number"))
marks=int(input("enter your marks"))

a=Template("your name is $enemy and your mobile number is $mobile and your marks is $marks")
f=a.substitute(enemy=name,mobile=mobile,marks=marks)
print(f)

#ex2:-
from string import Template
class1=input("enter your class name")
language=input("enter your language")
marks=int(input("enter your marks"))
a=Template("this is your  $class1 class and this is your  $language language and this is your $marks marks")
s=a.substitute(class1=class1,language=language,marks=marks)
print(s)









