

list = [0,1,2,3,4]
list2 = []
for i in list:
    list2.append(i+1)

print(list2)


list3 = [i+1 for i in list2]
print(list3)


list4 = [4,1,2,3,4, 3,6,2]

set1 = set(list4)
print(set1)

#Bug
set2 = {k**2  for k in set1}
print(set2)

list5 = [k**2  for k in set1]
print(list5)




a = {'Hello':'World', 'First': 1}
b = {}
for k, v in a.items():
    b.setdefault(v, k)
print(b)

b.update({'World':'Hello1'})
print(b)

c = {v: k for k , v in a.items()}

print(c)


