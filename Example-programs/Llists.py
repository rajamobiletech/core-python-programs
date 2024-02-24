list1 = [1,2,3,4,5]
list2 = [7,8,9,10,11]
s= list1+list2
print(s)


malelist = ["jayanth", "gani", "pavan","charan", "kamal"]
femalelist = ["sam","anika","anjali", "mangali", "swaroopa"]

malelist.append("harsha")
femalelist.remove("sam")
malelist.pop()

classlist = malelist+femalelist

print(classlist)

print("==================")

print(malelist[-1])
print(femalelist[2])

classlist.sort()
print(classlist)


num1=[3,5,15,21,7,73,18,27,45,11,19,99,39,79]
f=[a for a in num1 if a%3==0]
print(f)

list1=[12,31,51,46,76,87,98,100,112,154,76,38,65,29,22,88,23,45,21,87,93,42]
r=[a for a in list1 if a%2==0]

list1.sort()
print(list1)

print(r)

a=90
b=28
c=10
d=121
e=12
f=21

maximum= max(a,b,c,d,e,f)

print(maximum)

a=90
b=28
c=10
d=121
e=12
f=21

minimum= min(a,b,c,d,e,f)

print(minimum)



#swapping two numbers
a=20
b=90

print(a,b)
temp=a 
a=b
b=temp

print(a,b)

for i in range(1,11):
    print(f"5 * {i} = {5 * i}")