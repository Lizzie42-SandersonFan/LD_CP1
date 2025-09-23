# LD 2nd Elif and Logical Operators Notes

homework_done = True
chores = True
room = True

if homework_done and chores and room:
    print("You can go to your friends house.")
elif not chores or not room:
    print("Do your chores and clean your room!")
else:
    print("Go do your homework.")

username = input("Enter your user name: ")
password = input("Enter your password: ")

if username == "MsLaRose":
    if password == "1234":
        print("Welcome Ms. LaRose")
    else:
        print("Incorrect Password")
elif username == "Tia" and password == "password":
    print("Welcome Tia")
elif username == "Andrew" and password == "orange":
    print("Welcome Andrew")
else:
    print("That is not a valid sign in.")