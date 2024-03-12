

number = ("First", "Second", "Third", "Fourth", "Second") 
print(number)

print(number[1:4])

print(number[0:4])

print(number[-3])

print(number[-3:-2])

print(number[:])


print(number.count("Second"))


print(number.index("Fourth"))

# Convert list to a tuple
a = tuple(['first', 'second', 'third'])
# Convert tuple to a list
b = list(('first', 'second', 'third'))
# Convert string to a list
c = list("Scaler")

print(a)
print(b)
print(c)


mulipleItemsInTuples = (1,2,(0,1), ("raja", 1), tuple())
print(mulipleItemsInTuples)
print(mulipleItemsInTuples[2])
print(mulipleItemsInTuples[3])

mulipleItemsInTuples1 = (1,2,[0,1, "sadasd", "asdsd"], ("raja", 1), tuple())

print(mulipleItemsInTuples1)


bag1 = ("Apple", "Banana")
bag2 = ("Apple", "Banana")

print(len(bag1))

print(max(bag1))

print(min(bag1))


#Comparing two tuples by cmp custom function
def cmp(a, b):
    return (a > b) - (a < b) 

print(cmp(bag1, bag2))

print("________________________________________________________________________________________________")

#creation of tuple:-
tup=("apple","papaya","mango","grapes","papaya","banana","banana","orange","gua","mosambi","banana","banana")
print(tup)

#slicing of tuple:-
print(tup[2])

print(tup[2:-1])

print(tup[0:2])

#counting a repeated values in tuples:-
print(tup.count("papaya"))

print(tup.count("banana"))

print(tup.count("orange"))

print(tup.count("apple"))

#giving a number value of perticular value:-
print(tup.index("banana"))

print(tup.index("orange"))

print(tup.index("grapes"))

#converting list to a tuple:-
#ex1:-
list=tuple(['five','six','seven'])
print(list)

#ex2:-
list2=(['1','2','3'])
print(list2)

#adding two tuples in one tuples:-
twotup=tup+list
print(twotup)

#lenth of tuple:-
#ex1:-
print(len(twotup))

#ex2:-
print(len(tup))

#ex3:-
print(len(list2))

print(max(twotup))

print(min(twotup))

print(max(tup))

print(min(tup))

print(twotup)