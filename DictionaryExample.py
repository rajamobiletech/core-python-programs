#creation
teluguDic = {"Door":"thalupu", 
             "ten":"padhi",
             "dog":"kukka",
             "pig":"pandi"
             }

print(teluguDic["dog"])
print(teluguDic.keys())
print("================")
#Get all keys
for k in teluguDic.keys():
    print(k)

print("================")
#Get all values
for v in teluguDic.values():
    print(v)

print("================")

#Get all items as tuples
for i in teluguDic.items():
    print(i)

#Add
teluguDic['cat'] = "pilli"

#Update
teluguDic['dog'] = "shunakam"
print("================")
print(teluguDic)

print("================")
#delete
del teluguDic['cat']
print(teluguDic)

#Check key present or not
print("cat" in teluguDic)

print("================")
#copy
engDic = teluguDic.copy()
print(f"English Dic:{engDic}")

print("================")
#pop
teluguDic.pop("dog")
print(teluguDic)

print("================")
print(len(teluguDic))

#clear
engDic.clear()
print(engDic)

print(teluguDic.setdefault("dog", "shunakam"))

print(teluguDic.setdefault("dog", "kukka"))

teluguDic.update({"dog":"Dog"})


print(teluguDic)


a = dict.fromkeys({"bhanu", "ganesh"}, "python")
b = dict.fromkeys({"anji", "rajitha"}, "java")

print(a)
print(b)

print(a.update(b))