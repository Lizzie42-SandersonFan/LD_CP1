# LD 2nd This is to write code in to explain stuff to seat partners

user = "lizzie.delong"
password = "password"

user_name = input("What is your user name:\n").strip()
user_password = input("What is your password:\n").strip()

if user_name:
    if user_name == user:
        if user_password:
            if user_password == password:
                print("hello")