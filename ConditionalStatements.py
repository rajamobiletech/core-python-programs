#defination of [if]:-
'''if: The if statement is used to execute a block of code only if a specified condition is true.
It can be followed by an optional elif (short for "else if") and else statements.
If the condition is not true, the code block is skipped.'''

#example:-
print("example")

salary=500
if salary>=10000 and salary<=15000:
    print("your salary is high")

'''elif: The elif statement allows you to check multiple conditions. 
If the condition for if is False, it checks the elif condition
and executes the block of code associated with the first elif that is true.
salary''' 
 #example:
salary=500
if salary>=10000 and salary<=15000:
    print("your salary is avg")
elif salary>=5000 and salary<=10000:
    print("your salary is avg")

'''  else: The else statement is used to execute a block of code if 
the condition for the if statement is False'''
#example:    
salary=500
if salary>=10000 and salary<=15000:
    print("your salary is avg")
elif salary>=5000 and salary<=10000:
    print("your salary is avg")
else:
    print("your salary is low")

#total example including [if,elif,else]
    
salary = 500
if salary >= 10000 and salary <= 20000:
    print("your salary is high")
elif salary >= 5000 and salary <=10000:
    print("your salary is average")
else:
    print("Your salary is low")

print("Completed")


