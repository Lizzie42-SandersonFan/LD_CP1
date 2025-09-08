# LD 2nd Formatting Outputs Notes

name = "Jake"
age = 21
grade = .75
money = 25

print("Hello {}, nice to meet you! \nYou are {:b} and that is really old! \nYou have a {:%} in this class. \nYou have ${:.2f}, that is a lot of money!".format(name, age, grade, money))

print(f"Hello {name}, nice to meet you! \nYou are {age:b} and that is really old! \nYou have a {grade:%} in this class. \nYou have ${money:.2f}, that is a lot of money!")