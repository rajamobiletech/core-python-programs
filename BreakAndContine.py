scores = [134, 67, 99, 15, 34, 102, 45]


for s in scores:
    if s > 100:
        print(f"{s} is Invalid")
        print(s)
        break
        
print("=================")

for r in scores:
    if r > 100:
        # print(f"{r} is invalid")
        continue
    else:
         print(f"{r} is valid")
