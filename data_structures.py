import random
x = {"Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Violet", "Maroon", "Pink", "Black"}

y = ["Black", "Pink", "Maroon", "Violet", "Blue", "Cyan", "Green", "Yellow", "Oragne", "Red"]


print ("Yellow" in x)

print (y[3])


print (x)

random.shuffle(y)
print (y)


z = {"Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Violet", "Maroon", "Pink", "Black", "White"}
x.update(z)
print(x)

y.append("White")
print(y)


x.remove("Red")
print(x)

y.remove("Black")
print(y)

x.remove("Pink")
y.remove("Pink")
print (x)
print (y)


