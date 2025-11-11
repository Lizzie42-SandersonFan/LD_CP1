# LD 2nd Order Up Practice
import time
delay = 0.06

# Build a dictionary with menu items
menu = {
    "cookies": ["Milk Chocolate Chip", "Dirt Cake", "Raspberry Lemonade", "S'mores", "Chocolate Cake Batter", "Lemon Bar", "Birthday Cake", "Snickerdoodle Cupcake", "Original Pink Sugar", "Brownie Sundae", "Chocolate Peanut Butter Pie", "Cookie Dough", "Snickerdoodle"]
}
cookies_list = ["milk chocolate chip", "dirt cake", "raspberry lemonade", "s'mores", "chocolate cake batter", "lemon bar", "birthday cake", "snickerdoodle cupcake", "original pink sugar", "brownie sundae", "chocolate peanut butter pie", "cookie dough", "snickerdoodle"]
# Dictionary that is the item selected and its price
# This dictionary will slowly be built up through if statements to see what the user ordered
order = {

}
# Function for ordering
def ordering(cookie):
    if cookie in cookies_list:
        return True
    else:
        return False

# Welcome the user to Crumbl Cookie
welcome = f"Hello! Welcome to Crumbl Cookie!\nYou are able to order a box of six cookies!\n\n"
for char in welcome:
    print(char, end="", flush=True)
    time.sleep(delay)
# If statements that will ask the user what they want based on the menu dictionary
for key in menu.keys():
    if key == "cookies":
        print("Here is the cookie Menu:")
        for cookie in menu[key]:
            print(f"{cookie}")
    else:
        print("Something went very wrong :D")
# Should do some while loops to asked again if option is invalid
# While loop for cookie one choice
while True:
    cookie1 = input("\nWhat would you like your first cookie to be?\n").strip().lower()
    result = ordering(cookie1)
    if result == True:
        print(f"{cookie1} cookie added to your order!\n")
        order[cookie1] = 3.75
        break
    else:
        print("Invalid input.\nEither we don't have that cookie or your speeling was wrong.\n")
        continue

# While loop for cookie two choice
while True:
    cookie2 = input("What would you like your second cookie to be?\n").strip().lower()
    result = ordering(cookie2)
    if result == True:
        print(f"{cookie2} cookie added to your order!\n")
        order[cookie2] = 3.75
        break
    else:
        print("Invalid input.\nEither we don't have that cookie or your speeling was wrong.\n")
        continue

# While loop for cookie three choice
while True:
    cookie3 = input("What would you like your third cookie to be?\n").strip().lower()
    result = ordering(cookie3)
    if result == True:
        print(f"{cookie3} cookie added to your order!\n")
        order[cookie3] = 3.75
        break
    else:
        print("Invalid input.\nEither we don't have that cookie or your speeling was wrong.\n")
        continue

# While loop for cookie four choice
while True:
    cookie4 = input("What would you like your fourth cookie to be?\n").strip().lower()
    result = ordering(cookie4)
    if result == True:
        print(f"{cookie4} cookie added to your order!\n")
        order[cookie4] = 3.75
        break
    else:
        print("Invalid input.\nEither we don't have that cookie or your speeling was wrong.\n")
        continue

# While loop for cookie five choice
while True:
    cookie5 = input("What would you like your fifth cookie to be?\n").strip().lower()
    result = ordering(cookie5)
    if result == True:
        print(f"{cookie5} cookie added to your order!\n")
        order[cookie5] = 3.75
        break
    else:
        print("Invalid input.\nEither we don't have that cookie or your speeling was wrong.\n")
        continue

# While loop for cookie six choice
while True:
    cookie6 = input("What would you like your sixth cookie to be?\n").strip().lower()
    result = ordering(cookie6)
    if result == True:
        print(f"{cookie6} cookie added to your order!\n")
        order[cookie6] = 3.75
        break
    else:
        print("Invalid input.\nEither we don't have that cookie or your speeling was wrong.\n")
        continue

# Print out order and final price
print("Here is your final order!\n")
for cookie in order:
    pass