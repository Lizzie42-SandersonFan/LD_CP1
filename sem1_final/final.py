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
    # have a way to check if GOD_GIFT is true, if it is then change enter room text
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
            # add 10 arrows to arrow count
            break
        elif raid == "NO":
            nope = "You ignore the corpse and continue looking around the room.\n"
            typePrint(nope)
            break
        else:
            print("Invalid input, try again")
            continue
    description1 = "After looking around the room you notice no hallways forward.\n"
    typePrint(description1)
    while True:
        hallway = ("Would you like to go back a room:\nYes").upper()
        if hallway == "YES":
            roomOne()
        else:
            print("You have to go back to the previous room, please type 'Yes'")
            continue

def roomFive():
    room2 = "You enter the hallway and find yourself in a room with three corspes.\n"
    typePrint(room2)
    while True:
        raid = input("Would you like to raid the corpses:\nYes\nNo").upper()
        if raid == "YES":
            found = "You find three items on the corpses:\n- A set of daggers\n- A full heal potion\n- A splash potion of fire (deals 40 damge)\n"
            typePrint(found)
            # add healing potion to user invintory, daggers to attack dict, and splach potion to attacks dict
            break
        elif raid == "NO":
            nope = "You ignore the corpses and continue looking around the room.\n"
            typePrint(nope)
            break
        else:
            print("Invalid input, try again")
            continue
    description1 = "After looking around the room you notice one hallway forward."
    typePrint(description1)
    while True:
        hallway = ("Would you like to go down the hallway:\nYes\\nGo back a room(type 'Go back' if you want to do this)").upper()
        if hallway == "YES":
            pass # call room 10 func
        elif hallway == "GO BACK":
            startRoom()
        else:
            print("Invalid input, try again")
            continue

def roomSix():
    # When most code written, find a way to see if the chest is opened. if it is, change discription
    description1 = "In this room, you see a chest.\n"
    typePrint(description1)
    while True:
        pick_up = input("Would you like to open the chest:\nYes\nNo").upper()
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
            pass # call room 10 func
        elif hallway == "2":
            pass #call room 9 func
        else:
            print("Invalid input, try again")
            continue

def roomSeven():
    room7 = "You enter the first hallway and find yourself in a room with two corspes.\n"
    typePrint(room7)
    while True:
        raid = input("Would you like to raid the corpses:\nYes\nNo").upper()
        if raid == "YES":
            found = "You find 10 arrows and a full heal potion. Sweet!\n"
            typePrint(found)
            # add 100 arrows to arrow count
            break
        elif raid == "NO":
            nope = "You ignore the corpses and continue looking around the room.\n"
            typePrint(nope)
            break
        else:
            print("Invalid input, try again")
            continue
    description1 = "After looking around the room you notice no hallways forward.\n"
    typePrint(description1)
    while True:
        hallway = ("Would you like to go back a room:\nYes").upper()
        if hallway == "YES":
            roomTwo()
        else:
            print("You have to go back to the previous room, please type 'Yes'")
            continue

def roomEight():
    room8 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room8)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            found = "You find a broad sword. Nifty!\n"
            typePrint(found)
            # add broadsword to attack dict
            break
        elif raid == "NO":
            nope = "You ignore the corpse and continue looking around the room.\n"
            typePrint(nope)
            break
        else:
            print("Invalid input, try again")
            continue
    description1 = "After looking around the room you notice no hallways forward.\n"
    typePrint(description1)
    while True:
        hallway = ("Would you like to go back a room:\nYes").upper()
        if hallway == "YES":
            roomThree()
        else:
            print("You have to go back to the previous room, please type 'Yes'")
            continue

def roomNine():
    room9 = "You enter the hallway and find yourself in a room with ... a dragon!\nInitiating combat\n"
    typePrint(room9)
    while True:
        pass
        # call user attack
        # check if someone dead
        # call mini boss atack
        # check if someone dead
    # if someone dead, check who. 
    # if mini boss dead, have user be given GIFT_OF_FIRE which is a move they can preform. Have user advance back to roomSix()
    # if player dead, call playerDead func

def roomTen():
    room10 = "You enter the hallway and find yourself in a room filled with spider webs. Something laughs above you...\n"
    typePrint(room10)
    time.sleep(1)
    monologue = "'MWAHAHAHAHAHAHA!\nWhat have we got here? Is it someone who dares chalenge me?\nI'm sure you have seen the bodies in this cave, what makes you think you can defeat me?'\nKALLACKS: Eight Legged Scourge of the Caves\n'Are you ready to do this, child?'\n"
    while True:
        pass
        # call user attack
        # check if someone dead
        # call final boss atack
        # check if someone dead
    # if someone dead, check who. 
    # if final boss dead, have boss scream and protest. Have user advance. call exitRoom()
    # if player dead, call playerDead func

def exitRoom():
    entry = "You have defeated Kallacks!\nWalking past his corpse, you enter a room that seems to be glowing with the light of the setting sun.\nThere is a hole in the ceiling and you scrammble your way out.\nThere is a village and you see three figure standing at the village entrance talking with the locals.\nCould it be?\nIt is! It's your family you were separated from!\nSprinting your way to them, they catch you in a tight group hug.\nYou tell them about your journey through the caves and what you did.\nEveryone smiles and you decide to stay in the village for the night bore continuing on your big family travels.\n"
    typePrint(entry)

# user attack

#mini boss attack

# final boss attack

user_health = 30
user_armor = 15
full_health_potions = 0
God_gift = False
Gift_of_fire = False
arrows = 0
moves = {
    
}