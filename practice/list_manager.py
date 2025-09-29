# LD class Shopping List Manager
import time
delay = 0.06

opening = "Hello and welcom to your shopping list manager!\n"
for char in opening:
    print(char, end="", flush=True)
    time.sleep(delay)

shopping_list = []
while True:
    action = input("\nWhat you like to do to your shopping list:\n\tAdd\n\tRemove\n\tView\n\tExit\n").strip().lower()
    
    if action == "remove" and not shopping_list:
        print("\nSorry, you can do that action; your shopping list is empty!\n")
    elif action == "add":
        item_add = input("\nWhat would you like to add to your shopping list:\n").strip().capitalize()
        shopping_list.append(item_add)
    elif action == "remove":
        item_gone = input("\nWhat would you like to remove from your shopping list:\n").strip().capitalize()
        shopping_list.remove(item_gone)
    elif action == "view":
        print("This is your shopping list!\n")
        for x in shopping_list:
            print(x)
    elif action == "exit":
        break
    else:
        print("\nSorry, that is not an action you can do, please try again.\n")