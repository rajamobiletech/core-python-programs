age = int(input("Enter Your age:"))
name = input("Enter Your name:")

if age >= 21 and age <= 30:
    print("your age is {0} and {1} is ready for marriage".format(age, name))
else:
    print(f"your age is {age} and {name} aren't ready for marriage")
