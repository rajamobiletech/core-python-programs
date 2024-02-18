
def mulitplicationTable(a):
    for i in range(1,11):
        print(f"{i} * {a} = {a*i}")

def additionTable(b):
    for i in range(1,11):
        print(f"{i} + {b} = {b+i}")

def subtractionTable(c):
    for i in range(1,11):
        print(f"{c} - {i} = {c-i}")

num = int(input("Enter your number:"))
mulitplicationTable(num)
print("===================")
additionTable(num)
print("===================")
subtractionTable(num)


def summa(name, className, sub, reg):
    print(sub)
    print(reg)
    print(name)
    print(className)

summa("raja", "class1", "math", 1)
summa(reg=1, sub="math", className="class1", name="raja")
summa("raja", "class1", sub="math", reg=1)

print("=======")

