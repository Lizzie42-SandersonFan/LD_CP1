# LD 2nd Lists Notes
import random

names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Eric", 5, 3.14, False]

print(names)
print(names[3])
print(names[random.randint(1, len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names.remove(3.14)
x = names.index(5)
names.pop(x)
print(names)


fruits = ['apple', 'banana', 'cherry']
y = fruits.index("cherry")
print(y)