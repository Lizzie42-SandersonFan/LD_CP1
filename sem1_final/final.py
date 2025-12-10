# LD 2nd Final Game
import time
delay = 0.06

def typePrint(strng):
    for char in strng:
        print(char, end="", flush=True)
        time.sleep(delay)

def startRoom():
    for key in moves.keys():
        if key == "sword":
            description1 = "You look around the room. All you see is a sword on the ground. Would you like to pick it up?\n"
            typePrint(description1)
            while True:
                pick_up = input("Pick up sword:\nYes\nNo").upper()
                if pick_up == "YES":
                    moves["sword"] = 10
                    break
                elif pick_up == "NO":
                    # user does not have sword
                    break
                else:
                    print("Invalid input, try again")
                    continue
        else:
            description1 = "You have already picked up the sword on the ground.\n"
            typePrint(description1)
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
    # this has corpse one
    room1 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room1)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            if corpse1_raided == False:
                found = "You find a small vile of liquid labled 'Health Bonus' and you drink it. You have gained 5 health.\n"
                typePrint(found)
                user_health += 5
                corpse1_raided = True
                break
            else:
                found = "Seems you have already raided this corpse.\n"
                typePrint(found)
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
            roomFour()
        elif hallway == "3":
            roomFive()
        elif hallway == "GO BACK":
            startRoom()
        else:
            print("Invalid input, try again")
            continue

def roomTwo():
    # this has corpse two
    room2 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room2)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            if corpse2_raided == False:
                found = "You find a potion labled 'Health Restore'. You pocket the healing potion\n"
                typePrint(found)
                full_health_potions += 1
                corpse2_raided = True
                break
            else:
                found = "Seems you have already raided this corpse.\n"
                typePrint(found)
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
            roomFive()
        elif hallway == "2":
            roomSix()
        elif hallway == "3":
            roomSeven()
        elif hallway == "GO BACK":
            startRoom()
        else:
            print("Invalid input, try again")
            continue

def roomThree():
    if god_gift == False:
        room3 = "You enter the first hallway and find yourself in an empty room.\nSuddenly, you see a giant flash of light, temporally blinding you while a figure decends from the light.\nIt is God, and he speeaks:\n'Welcome brave traveler. There are chalenges awiting you further into this cave. To help you, I have decided to grand you more power in your attacks. Use this power wisely.'\nYou feel a wave of power wash over you and you fell your attack power increase.\nGod leaves.\n" 
        god_gift = True
        typePrint(room3)
    else:
        room3 = "God has already given you your bonus. Move to a new room.\n"
        typePrint(room3)
    description1 = "You notice two hallways forward."
    typePrint(description1)
    while True:
        hallway = ("Which hallway:\n1\n2\nGo back a room(type 'Go back' if you want to do this)").upper()
        if hallway == "1":
            roomEight()
        elif hallway == "2":
            roomTen()
        elif hallway == "GO BACK":
            roomOne()
        else:
            print("Invalid input, try again")
            continue

def roomFour():
    # this has corpse three
    room4 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room4)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            if corpse3_raided == True:
                found = "You find 10 arrows. Sweet!\n"
                typePrint(found)
                arrows += 10
                corpse3_raided = True
                break
            else:
                found = "Seems you have already raided this corpse.\n"
                typePrint(found)
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
    # this has corpses four, five, and six
    room2 = "You enter the hallway and find yourself in a room with three corspes.\n"
    typePrint(room2)
    while True:
        raid = input("Would you like to raid the corpses:\nYes\nNo").upper()
        if raid == "YES":
            if corpse4_raided == False and corpse5_raided == False and corpse6_raided == False:
                found = "You find three items on the corpses:\n- A set of daggers\n- A full heal potion\n- A splash potion of fire (deals 40 damge)\n"
                typePrint(found)
                full_health_potions += 1
                moves["daggers"] = 12
                splash_potions += 1
                corpse4_raided = True
                corpse5_raided = True
                corpse6_raided = True
                break
            else:
                found = "Seems you have already raided these corpses.\n"
                typePrint(found)
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
            while True:
                room = input("Which room would you like to go back to:\nOne\nTwo").upper()
                if room == "ONE":
                    roomOne()
                elif room == "TWO":
                    roomTwo()
                else:
                    print("Invalid input. Try again")
                    continue
        else:
            print("Invalid input, try again")
            continue

def roomSix():
    # When most code written, find a way to see if the chest is opened. if it is, change discription
    if chest_opened == False:
        description1 = "In this room, you see a chest.\n"
        typePrint(description1)
        while True:
            pick_up = input("Would you like to open the chest:\nYes\nNo").upper()
            if pick_up == "YES":
                find = "You find a set of arromor! Your arromor is increased.\n"
                typePrint(find)
                user_armor += 8
                break
            elif pick_up == "NO":
                break
            else:
                print("Invalid input, try again")
                continue
    else:
        nope = "You have already opened the chest!\n"
        typePrint(nope)
    description2 = "Looking further down the room, you see two hallways forward. Which one would you like to go down?\n"
    typePrint(description2)
    while True:
        hallway = ("Which hallway:\n1\n2").upper()
        if hallway == "1":
            roomTen()
        elif hallway == "2":
            roomNine()
        else:
            print("Invalid input, try again")
            continue

def roomSeven():
    # this has corpses seven and eight
    room7 = "You enter the first hallway and find yourself in a room with two corspes.\n"
    typePrint(room7)
    while True:
        raid = input("Would you like to raid the corpses:\nYes\nNo").upper()
        if raid == "YES":
            if corpse7_raided == False and corpse8_raided == False:
                found = "You find 10 arrows and a full heal potion. Sweet!\n"
                typePrint(found)
                arrows += 10
                full_health_potions += 1
                break
            else:
                found = "Seems you have already raided these corpses.\n"
                typePrint(found)
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
    # this has corpse nine
    room8 = "You enter the first hallway and find yourself in a room with a corspe.\n"
    typePrint(room8)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper()
        if raid == "YES":
            if corpse9_raided == False:
                found = "You find a broad sword. Nifty!\n"
                typePrint(found)
                moves["broadsword"] = 20
                break
            else:
                found = "Seems you have already raided this corpse.\n"
                typePrint(found)
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
    # this will use if mini_boss_dead
    room9 = "You enter the hallway and find yourself in a room with ... a dragon!\nInitiating combat\n"
    typePrint(room9)
    while True:
        pass
        # call user attack
        # check if someone dead
        # call mini boss atack
        # check if someone dead
    # if someone dead, check who. 
    # if mini boss dead, have user be given GIFT_OF_FIRE which is a move they can preform and make mini_boss_dead true. Have user advance back to roomSix()
    # if player dead, call playerDead func

def roomTen():
    room10 = "You enter the hallway and find yourself in a room filled with spider webs. Something laughs above you...\n"
    typePrint(room10)
    time.sleep(1)
    monologue = "'MWAHAHAHAHAHAHA!\nWhat have we got here? Is it someone who dares chalenge me?\nI'm sure you have seen the bodies in this cave, what makes you think you can defeat me?'\nKALLACKS: Eight Legged Scourge of the Caves\n'Are you ready to do this, child?'\n"
    typePrint(monologue)
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

# mini boss attack

# final boss attack

# player died func

user_health = 30
user_armor = 15
full_health_potions = 0
splash_potions = 0
god_gift = False
gift_of_fire = False
arrows = 0
moves = {
    
}
corpse1_raided = False
corpse2_raided = False
corpse3_raided = False
corpse4_raided = False
corpse5_raided = False
corpse6_raided = False
corpse7_raided = False
corpse8_raided = False
corpse9_raided = False
chest_opened = False
mini_boss_dead = False

# Begin actual game
