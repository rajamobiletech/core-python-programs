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

print("________________________________________________________________________________________________________________")
#another example of list and list methods:-

herolist=["ntr","alluarjun","maheshbabu","prabhas","surya","ramcharan","varuntej","pavankalyan","balayya","varuntej",]

herolist.append("kalyanram")

herolist.pop(6)

herolist.remove("varuntej")

herolist.remove("maheshbabu")

herolist.insert(1,"maheshbabu")


herolist.pop(6)

herolist.extend(["nithin","varuntej","nani"])

heroinlist=["samantha","kajal","poojahegde","saipallavi","rashikhanna"]

heroinlist.pop(1)

heroinlist.pop(0)

heroinlist.insert(0,"samantha")

heroinlist.extend(["zoya","keerthisuresh","kritisanon","kiaraadvani"])

heroinlist.pop(4)
 
heroinlist.pop(-2)

movieactores=herolist+heroinlist

movieactores .append("tamanna")


movieactores.insert(3,"varuntej")

movieactores.sort()

movieactores.reverse()

movieactores.reverse()

print(movieactores)

print("============================================================================================")
 
list1=[1,3,2,5,4,6,7,8,9]
list2=["A","b","c","d","E","f"]
list1.remove(1)
print(list1)
list2.remove("c")
print(list2)
list1.insert(0,1)
print(list1)
list2.insert(2,"c")
print(list2)
list1.pop(8)
list1.pop(7)
list1.pop(6)
print(list1)
list3=list2+list1
print(list3)
list1.sort()
print(list1)
list3.extend(["g","h","i"])
list3.reverse()
print(list3)





