scores = [134, 67, 99, 15, 34, 102, 45]


for s in scores:
    if s > 100:
        print(f"{s} is Invalid")
        print(s)
        break
        
print("=================")

for r in scores:
    if r > 100:
        #print(f"{r} is invalid")
        continue
    else:
         print(f"{r} is valid")

print("============================================================================================================")

runs=[43,56,87,123,147,102,84,91,99,100,101]
for k in runs:
    if k >100:  #print only greater than 100 values
      print(f"{k} it greater than  100 ")

for i in runs:
    if i < 100:  #print only less than 100 values
        print(f"{i} it is  less than 100") 


for g in runs:
    if g > 90:  #skip all greater than 90 values 
        continue
    print(f"{g} is bellow 90")   

for h in runs:
    if h >90:  #break when start numbers above 90
        break
    print(f"{h} it is valid ")



