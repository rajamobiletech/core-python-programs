
def calcDivision(a, denominator):
    try:
        b = a/denominator
        print("Able to divide")
        return b
    except ZeroDivisionError as r:
        print(f"Error1={r}")
    except Exception as e:
        print(f"Erro2={e}") 
    finally:
        print("Done")


value = int(input("Enter the value:"))
denominator = int(input("Enter the denominator:"))
a = calcDivision(value,denominator)
print(a)


print("_________________________________________________________________________________________________________")


# denominator typically refers to the bottom part of a fraction, representing 
#the total number of equal parts into which a whole is divided.

def calculation(b,denominator):
    try:
        c=b/denominator
        return c
#defin of [zerodivisionerror]:-
#"ZeroDivisionError" occurs when you try to divide a number by zero. 
#Division by zero is mathematically undefined and not allowed in most programming languages, including Python.

    except ZeroDivisionError as zde:
        print(f"error value that is {zde}")

#An exception error in Python is an unexpected event that disrupts the normal flow of a program's execution,
#typically caused by errors in the program's logic or external factors like invalid user   
              
    except Exception as exc:
        print(f"the error is {exc}")
    finally:
        print("all done")

a=int(input("enter your value"))
denominator = int(input("enter your value"))
b=calculation(a,denominator)
print(b)      

