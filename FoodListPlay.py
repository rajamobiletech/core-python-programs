

veg = ["pulav", "Sambar", "Fried Rice", "Poori", "Dosai"]

nonveg = ["briyani", "chicken fry", "boti", "paya", "fish"]


print(veg[1:3])

veg[1] = "mushroom"

print(veg)

food = veg + nonveg

print(food)

food2 = food * 2

print(food2)

food.remove("pulav")

del food[3]

food.pop(4)

print(food)

for v in veg:
    print(v)


if "Dosai" in veg:
    print("Dosai is available")

if "Mutton Briyani" not in nonveg:
    print("Mutton items is not available")

