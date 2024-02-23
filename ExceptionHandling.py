
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


