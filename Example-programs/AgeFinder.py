
age = int(input("Enter your Age:"))
if age <= 5:
    print("Kid")
elif age > 6 and age <=10:
    print("Too young")
elif age > 10 and age <=20:
    print("young")
elif age > 20 and age <=30:
    print("Teen")
elif age > 30 and age <=50:
    print("Middle age")
elif age > 50 and age <=70:
    print("Old")
else:
    print("Death")