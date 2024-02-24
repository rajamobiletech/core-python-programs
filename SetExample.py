

list1 = [2,3,9,5,6,7,8,2,3,7,4,5,3]
print(list1)

set1 = {7,2,8,3}
print(set1)

set2 = set(list1)
print(set2)


#Add
set1.add(10)
print(set1)

#clear
set2.clear()
print(set2)

#Copy
set2 = set1.copy()
print(set2)

set1 = {7,2,8,3}
set3 = {5,4,2,8}

print(set1.difference(set3))
print(set3.difference(set1))

# set1.difference_update(set3)
# print(set1)

set1.discard(8)
print(set1)
