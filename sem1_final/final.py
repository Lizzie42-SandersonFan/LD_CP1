# LD 2nd Final Game
import time
delay = 0.06

def typePrint(strng):
    for char in strng:
        print(char, end="", flush=True)
        time.sleep(delay)

def startRoom():
    # When most code written, find a way to see of the sword is picked up; if it is, change description
    description1 = "You look around the room. All you see is a sword on the ground. Would you like to pick it up?\n"
    typePrint(description1)
    while True:
        pick_up = input("Pick up sword:\nYes\nNo").upper()
        if pick_up == "YES":
            pass # add sword to dictionary when created
            break
        elif pick_up == "NO":
            pass # have user move one without sword
            break
        else:
            print("Invalid input, try again")
            continue
    description2 = "Looking further down the room, you see two hallways forward. Which one would you like to go down?\n"
    typePrint(description2)
    while True:
        hallway = ("Which hallway:\n1\n2").upper()
        if hallway == "1":
            roomOne()
        elif hallway == "2":
            roomTwo()
        else:
            print("Invalid input, try again")
            continue

def roomOne():
    room1 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room1)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            found = "You find a small vile of liquid labled 'Health Bonus' and you drink it. You have gained 5 health.\n"
            typePrint(found)
            # add 5 to user health when created
            break
        elif raid == "NO":
            nope = "You ignore the corpse and continue looking around the room.\n"
            typePrint(nope)
            break
        else:
            print("Invalid input, try again")
            continue
    description1 = "After looking around the room you notice three hallways forward."
    typePrint(description1)
    while True:
        hallway = ("Which hallway:\n1\n2\n3\nGo back a room(type 'Go back' if you want to do this)").upper()
        if hallway == "1":
            roomThree()
        elif hallway == "2":
            pass # call room 4 func
        elif hallway == "3":
            pass # call room 5 func
        elif hallway == "GO BACK":
            startRoom()
        else:
            print("Invalid input, try again")
            continue

def roomTwo():
    room2 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room2)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            found = "You find a potion labled 'Health Restore'. You pocket the healing potion\n"
            typePrint(found)
            # add healing potion to user invintory
            break
        elif raid == "NO":
            nope = "You ignore the corpse and continue looking around the room.\n"
            typePrint(nope)
            break
        else:
            print("Invalid input, try again")
            continue
    description1 = "After looking around the room you notice three hallways forward."
    typePrint(description1)
    while True:
        hallway = ("Which hallway:\n1\n2\n3\nGo back a room(type 'Go back' if you want to do this)").upper()
        if hallway == "1":
            pass # call room 5 func
        elif hallway == "2":
            pass # call room 6 func
        elif hallway == "3":
            pass # call room 7 func
        elif hallway == "GO BACK":
            startRoom()
        else:
            print("Invalid input, try again")
            continue

def roomThree():
    room3 = "You enter the first hallway and find yourself in an empty room.\nSuddenly, you see a giant flash of light, temporally blinding you while a figure decends from the light.\nIt is God, and he speeaks:\n'Welcome brave traveler. There are chalenges awiting you further into this cave. To help you, I have decided to grand you more power in your attacks. Use this power wisely.'\nYou feel a wave of power wash over you and you fell your attack power increase.\n" # Set GOD_GIFT to true so that it increases any weapons power
    typePrint(room3)
    description1 = "After God leaves, you notice two hallways forward."
    typePrint(description1)
    while True:
        hallway = ("Which hallway:\n1\n2\nGo back a room(type 'Go back' if you want to do this)").upper()
        if hallway == "1":
            pass # call room 8 func
        elif hallway == "2":
            pass # call room 10 func
        elif hallway == "GO BACK":
            roomOne()
        else:
            print("Invalid input, try again")
            continue

def roomFour():
    room4 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room4)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            found = "You find 10 arrows. Sweet!\n"
            typePrint(found)
            # add 100 arrows to arrow count
            break
        elif raid == "NO":
            nope = "You ignore the corpse and continue looking around the room.\n"
            typePrint(nope)
            break
        else:
            print("Invalid input, try again")
            continue
    description1 = "After looking around the room you notice no hallways forward."
    typePrint(description1)
    while True:
        hallway = ("Would you like to go back a room:\nYes").upper()
        if hallway == "YES":
            roomOne()
        else:
            print("Invalid input, try again")
            continue