# LD 2nd Advanced Hello World

admin = "Ms. LaRose"
coder = "Liz"
returning_users = ["Bob", "Carl", "Derik"]

name = input("What is your name: ")

if name == admin or name == coder:
    print("Hello Admin", name)
elif name == returning_users:
    print("Hello", name)
else:
    print("Welcome", name)
    returning_users.append(name)