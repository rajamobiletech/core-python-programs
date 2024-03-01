
name = "Raja"
print(name)

a = ''' Hello  World!
This       is a 
Multiline   String.'''
print(a)


a = "Python"
print(a[0], a[2], a[4])
print(a[-1], a[-3], a[-5])


a = "Hello"
# Slices the string from 0 to 3 indexes
print(a[0:3])
# Slices the string from 3 to -1(same as 4) indexes
print(a[2:-1])

print("================")

a = "RaJA DuRaISAMY"
print(a)
# Converts string to uppercase 
print(a.upper())
# Converts string to lowercase 
print(a.lower())
# Checks if string is uppercase 
print(a.isupper())
# Checks if string is lowercase 
print(a.islower())

print("================")
b = "            "
#Returns True if all characters in string are whitespaces
print(b.isspace())
c = "ajdjdn723DSFjd73nd"
#Returns True if given string is alphanumeric
print(c.isalnum())

a = "raja"
# Returns True if given character is alphabet
print(a.isalpha())

#Returns True if string starts with an uppercase letter and then rest of the characters are lowercase
print(a.istitle())




sentence1 = "Raja Duraisamy is taking python class in the morning session"
list = sentence1.split(' ')
print(list)

print(" * ".join(list))


first = "first"
second = "second"
s = "Sunday is the {0} day of the week, whereas Monday is the {1} day of the week".format(first, second)
print(s)



print("================")

#Returns length
name = "raja duraisssamy"
print(len(name))

print(name.capitalize())

print(name.center(30, '#'))

#Find first occurence
print(name.find("a"))

#Find start with
print(name.find("a", 4))

#Find between
print(name.find("a", 4, 8))

a = "234324"
# Returns True if given character is number
print(a.isdigit())


print(name.title())

name = "kjJJgvbkBHjKhJkhugU"

print(name.swapcase())


from string import Template

lang = input("Enter your language:")
classNo = int(input("Enter your class Number:"))

t = Template("You are studing $language in class no $class Number")
str = t.substitute(language=lang, classNumber = classNo)
print(str)


