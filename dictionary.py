#dictioary creation:-
food={"whiterice":"pappu",
      "parota":"chicken",
      "poori":"chutny"}

#get all keys from dic
print(food.keys())

#get all values from dic
print(food.values())

#give the values
print(food["parota"])
print(food["poori"])

# that value check is thare are not
print("poori" in food)
print("lemonrice" in food)

#gives keys valiues in a orddered way
for i in food.keys():
    print(i)

#gives values list in a ordered way     

for j in food.values():
    print(j)

#it gives a keys list and also values list at a time
for i,j in food.items():
    print(f"{i} we use {j}")

#add
food["idli"]="sambar"
print(food)

#update
food["idli"]="chutny and sambar"
for i , j in food.items():
    print(f"{i} : {j}")

del food["poori"]    

food["lemonrice"]="picle"
del food["lemonrice"]

food["lemonrice"]="mangopicle"

for i , j in food.items():
    print(f"{i} : {j}")

#len:-it is check the lenth of dictionary
print(len(food))

food.pop("lemonrice")
print(food)

food.pop("idli")
print(food)


food.update({"chapathi":"eggcurry"})
food.update({"eggrice":"chickensharva"})
print(food)


food["poori"]="chutny"
food["pulav"]="rasam"
print(food)
a=dict.fromkeys({"java","python"},"rajasir")
b=dict.fromkeys({"java","python"},"rajasir")
print(a)
print(b)

print("______________________________________________________________________________________________________")


     


