
# from random import randint
import random
from random import *
import math

value = randint(1,100)

# print(value)

list1 = []
for _ in range(20):
    list1.append(randint(1,100))

print(list1)

print(round(3.4))

print(round(abs(-3.4)))

print(math.fabs(-3.42233232323))
print(abs(-3.42233232323))

print("______________________________________________________________________________________________________________")

from random import*

'''randint is a function used in programming to generate a random integer
 within a specified range. In Python, randint is a part of the random module. 
The function signature looks like this:'''

a = randint(1,100)
print(a)

print("___________________________________________________________________")

b = randint(1,10)
print(b)

print("___________________________________________________________________")

#append in randint

c = []
for j in range(10):
    c.append(randint(1,20))
print(c)

print("___________________________________________________________________")


#If you want to round all the numbers in a list in Python, you can use a list 
#comprehension along with the round function. Here's an example:

print(round(155.21))

print(round(51.36))

#abs function: Returns the absolute value of a number. For example:

print(round(abs(-35.33)))

print(round(abs(-532.56)))

print(abs(33.2323))

#fabs is a function in the math module that computes the absolute value of a floating-point number.
#It stands for "floating-point absolute value." The fabs function is similar to the built-in abs function
#but is specifically designed to work with floating-point numbers.

import math
print(math.fabs(-30.3232323))

print(math.fabs(-55.3232323))


 
