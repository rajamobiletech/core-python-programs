list1 = ["A", "B", "C", "D", "E", "F", "G"]

list1.append("H")

list1.extend(["i", "J", "j"])

list2 = ["K", "L", "K", "K"]

list1.extend(list2)
list1.remove("i")

list1.insert(8, "I")
print(list1)
list1.pop(10)

print(list1)

print(list1.count("K"))

list1.sort()

print(list1)

list1.reverse()


print(list1)


list3 = []
for ch in list1:
    if ch != "A":
        list3.append(ch)

print(list3)

print("==============")

list2 = ["A", "B", "A", "D", "A", "F", "A"]


count = list2.count("A")
print(count)

print("==============")


for _ in range(count):
    list2.remove("A")
    print(list2)

print(list2)









