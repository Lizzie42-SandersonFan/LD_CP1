# LD 2nd User Sign-In Practice
import time
delay = 0.06


users = [["lizzie.delong", "password123"], ["daniel.delong", "pAsSwOrD-OhBOY-WEEE"]]

user_name = input("What is your user name:\n").strip()
user_password = input("What is your password:\n").strip()


if user_name == users[0][0] and user_password == users[0][1]:
    print(f"Welcome user {users[0][0]}!")
elif user_name == users[1][0] and user_password == users[1][1]:
    print(f"Welcome user {users[1][0]}!")
else:
    message = "Please check that your user name and/or password is correct.\nYou might also not be in our system. Make sure that you know if you are in the system."
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)