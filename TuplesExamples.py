

number = ("First", "Second", "Third", "Fourth", "Second") 
print(number)
print(number[1:3])

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