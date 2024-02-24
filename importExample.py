import random                   #Importing
# import random as r            #Aliasing
# from random import randint    #Importing functions from modules
# from random import *          #Importing Everything


a = random.randint(1,100)

print(a)


import random as rd
b=rd.randint(1,20)
print(b)

b=[]
for m in range(10):
    b.append(rd.randint(1,5))
    print(b)