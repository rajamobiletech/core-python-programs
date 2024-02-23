
x = [1,2,3,4,5]

print(6 in x)

name = "Raja Duraisamy"

print('x' in name)


y = x

print(y is x)

z = [1,2,3,4,5]

print(z is x)   # Checking same object or not
print(z == x)   # Checking same value or not

print("______________________________________________________________________________________________")

#Class: A class is defined using the class keyword followed by the class name.
#It serves as a template for creating objects.

hello="python"
print('p' in hello)

hi="javaprogram"
print('c' in hi)

s=[1,2,3,4,5,8,6,1]
print(9 in s)


#is:-In Python, the is operator is used to test whether two variables refer to the same object in memory.
#It evaluates to True if the variables point to the same object, and False otherwise.

hello = [1,2,3]
hello = y

print(hello is y)
