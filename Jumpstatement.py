
#Break

for i in range(100):
    print(i)
    if i == 10:
        break
print("==================")

for i in range(5):
    for j in range(4):
        if j == 1:
            break
        print(f"i={i} j={j}")

print("==================")

for i in range(2):
    for j in range(2):
        for k in range(100):
            if k == 2:
                break
            print(f"i={i} j={j} k={k}")

print("==================")
for i in range(5):
    print(i)
    print("Raja")
print("Hi")


print("==================")

for i in range(5):
    if i == 3:
        break
    for j in range(4):
        if j == 2:
            break
        print(f"i={i} j={j}")

print("==================")

for i in range(11):
    if i == 5:
        continue
    print(i)
print("==================")

for i in range(11):
    if i >= 5 and i <= 9:
        continue
    print(i)
print("==================")

for i in range(11):
    if i%2 == 0:
        pass
    else:
        print(i)

print("==================")

def add(a, b):
    return a+b

def sub(x, y):
    return x-y

c = sub(23,7)
c += 5
print(c)
