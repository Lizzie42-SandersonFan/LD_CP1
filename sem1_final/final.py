# LD 2nd Final Game
import sys
import threading
import random
import time
delay = 0.06

def flashingText1(stop_event):
    sys.stdout.write("\033[?25l")  # Hide the cursor
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rPress ENTER to continue   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                                ") # Ensure the line is cleared properly
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\033[?25h")  # Show the cursor again
    sys.stdout.flush()

def typePrint(strng):
    for char in strng:
        print(char, end="", flush=True)
        time.sleep(delay)

def startRoom():
    global picked_up_sword
    description1 = "\nYou look around the room.\nScrammbling to find where you fell in, you relize you can't get back up.\nYou have to naviagte where you have ended up.\nTurning back around you notice something in the room.\nA sword on the ground in the middle of the room.\nWould you like to pick it up?\n"
    typePrint(description1)
    while True:
        pick_up = input("Pick up sword:\nYes\nNo\n").upper().strip()
        if pick_up == "YES":
            if picked_up_sword == False:
                moves["sword"] = 10
                picked_up_sword = True
                break
            else:
                description1 = "\nYou have already picked up the sword on the ground.\n"
                typePrint(description1)
        elif pick_up == "NO":
            # user does not have sword
            break
        else:
            print("Invalid input, try again")
            continue
    description2 = "Looking further down the room, you see two hallways forward. Which one would you like to go down?\n"
    typePrint(description2)
    while True:
        hallway = input("Which hallway:\n1\n2\n").upper().strip()
        if hallway == "1":
            roomOne()
            break
        elif hallway == "2":
            roomTwo()
            break
        else:
            print("Invalid input, try again")
            continue

def roomOne():
    global corpse1_raided
    global user_health
    global user_full_health
    room1 = "\nYou enter the hallway and find yourself in a room with a corspe.\n"
    typePrint(room1)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo\n").upper().strip()
        if raid == "YES":
            if corpse1_raided == False:
                found = "\nYou find a small vile of liquid labled 'Health Bonus' and you drink it. You have gained 5 health.\n"
                typePrint(found)
                user_health += 5
                user_full_health += 5
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
    description1 = "\nAfter looking around the room you notice three hallways forward.\n"
    typePrint(description1)
    while True:
        hallway = input("Which hallway:\n1\n2\n3\nGo back a room(type 'Go back' if you want to do this)\n").upper().strip()
        if hallway == "1":
            roomThree()
            break
        elif hallway == "2":
            roomFour()
            break
        elif hallway == "3":
            roomFive()
            break
        elif hallway == "GO BACK":
            startRoom()
            break
        else:
            print("Invalid input, try again")
            continue

def roomTwo():
    global corpse2_raided
    global full_health_potions
    room2 = "\nYou enter the hallway and find yourself in a room with a corspe.\n"
    typePrint(room2)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo\n").upper().strip()
        if raid == "YES":
            if corpse2_raided == False:
                found = "\nYou find a potion labled 'Health Restore'. You pocket the healing potion\n"
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
    description1 = "After looking around the room you notice three hallways forward.\n"
    typePrint(description1)
    while True:
        hallway = input("Which hallway:\n1\n2\n3\nGo back a room(type 'Go back' if you want to do this)\n").upper().strip()
        if hallway == "1":
            roomFive()
            break
        elif hallway == "2":
            roomSix()
            break
        elif hallway == "3":
            roomSeven()
            break
        elif hallway == "GO BACK":
            startRoom()
            break
        else:
            print("Invalid input, try again")
            continue

def roomThree():
    global god_gift
    global full_health_potions
    if god_gift == False:
        room3 = "\nYou enter the first hallway and find yourself in an empty room.\nSuddenly, you see a giant flash of light, temporally blinding you while a figure decends from the light.\nIt is God, and he speeaks:\n'Welcome brave traveler. There are chalenges awiting you further into this cave. To help you, I have decided to grand you more power in your attacks. Use this power wisely.'\nYou feel a wave of power wash over you and you fell your attack power increase.\nGod leaves.\n" 
        god_gift = True
        typePrint(room3)
    else:
        room3 = "\nGod has already given you your bonus. Move to a new room.\n"
        typePrint(room3)
    description1 = "You notice two hallways forward."
    typePrint(description1)
    while True:
        hallway = input("Which hallway:\n1\n2\nGo back a room(type 'Go back' if you want to do this)\n").upper().strip()
        if hallway == "1":
            roomEight()
            break
        elif hallway == "2":
            move = "On your way, you find a heal potion. Sick!\n"
            full_health_potions += 1
            typePrint(move)
            roomTen()
            break
        elif hallway == "GO BACK":
            roomOne()
            break
        else:
            print("Invalid input, try again")
            continue

def roomFour():
    global corpse3_raided
    global arrows
    room4 = "\nYou enter the hallway and find yourself in a room with a corspe.\n"
    typePrint(room4)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo\n").upper().strip()
        if raid == "YES":
            if corpse3_raided == False:
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
    description1 = "\nAfter looking around the room you notice no hallways forward.\n"
    typePrint(description1)
    while True:
        hallway = input("Would you like to go back a room:\nYes\n").upper().strip()
        if hallway == "YES":
            roomOne()
            break
        else:
            print("You have to go back to the previous room, please type 'Yes'")
            continue

def roomFive():
    global full_health_potions
    global moves
    global splash_potions
    global corpse4_raided
    global corpse5_raided
    global corpse6_raided
    room2 = "\nYou enter the hallway and find yourself in a room with three corspes.\n"
    typePrint(room2)
    while True:
        raid = input("Would you like to raid the corpses:\nYes\nNo\n").upper().strip()
        if raid == "YES":
            if corpse4_raided == False and corpse5_raided == False and corpse6_raided == False:
                found = "You find an items on each of the corpses:\n- A set of daggers\n- A full heal potion\n- A splash potion of fire (deals 20 damge)\n"
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
    description1 = "After looking around the room you notice one hallway forward.\n"
    typePrint(description1)
    while True:
        hallway = input("Would you like to go down the hallway:\nYes\nGo back a room(type 'Go back' if you want to do this)\n").upper().strip()
        if hallway == "YES":
            move = "On your way, you find a spear. Yippey!\n"
            moves["spear"] = 14
            typePrint(move)
            roomTen()
            break
        elif hallway == "GO BACK":
            while True:
                room = input("Which room would you like to go back to:\n1\n2").upper().strip()
                if room == "1":
                    roomOne()
                    break
                elif room == "2":
                    roomTwo()
                    break
                else:
                    print("Invalid input. Try again")
                    continue
        else:
            print("Invalid input, try again")
            continue

def roomSix():
    global chest_opened
    global user_armor
    global moves
    global arrows
    if chest_opened == False:
        description1 = "\nIn this room, you see a chest.\n"
        typePrint(description1)
        while True:
            pick_up = input("Would you like to open the chest:\nYes\nNo\n").upper().strip()
            if pick_up == "YES":
                find = "You find a set of armor! Your armor is increased.\n"
                typePrint(find)
                user_armor += 4
                break
            elif pick_up == "NO":
                break
            else:
                print("Invalid input, try again")
                continue
    else:
        nope = "\nYou walk into the room and the chest that you have already opened.\nMove to a new room.\n"
        typePrint(nope)
    description2 = "Looking further down the room, you see two hallways forward. Which one would you like to go down?\n"
    typePrint(description2)
    while True:
        hallway = input("Which hallway:\n1\n2\nGo back a room(type 'Go back' if you want to do this)\n").upper().strip()
        if hallway == "1":
            move = "On your way, you find a bow and 30 arrows. Handy!\n"
            moves["bow"] = 6
            arrows += 30
            typePrint(move)
            roomTen()
            break
        elif hallway == "2":
            roomNine()
            break
        elif hallway == "GO BACK":
            roomTwo()
            break
        else:
            print("Invalid input, try again")
            continue

def roomSeven():
    global corpse7_raided
    global arrows
    global full_health_potions
    room7 = "\nYou enter the hallway and find yourself in a room with two corspes.\n"
    typePrint(room7)
    while True:
        raid = input("Would you like to raid the corpses:\nYes\nNo\n").upper().strip()
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
    description1 = "\nAfter looking around the room you notice no hallways forward.\n"
    typePrint(description1)
    while True:
        hallway = input("Would you like to go back a room:\nYes\n").upper().strip()
        if hallway == "YES":
            roomTwo()
            break
        else:
            print("You have to go back to the previous room, please type 'Yes'")
            continue

def roomEight():
    global corpse9_raided
    global moves
    room8 = "\nYou enter the hallway and find yourself in a room with a corspe.\n"
    typePrint(room8)
    while True:
        raid = input("Would you like to raid the corpse:\nYes\nNo").upper().strip()
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
        hallway = input("Would you like to go back a room:\nYes").upper().strip()
        if hallway == "YES":
            roomThree()
            break
        else:
            print("You have to go back to the previous room, please type 'Yes'")
            continue

def roomNine():
    global mini_boss_dead
    global mini_boss_health
    global user_health
    global moves
    if mini_boss_dead == False:
        room9 = "\nYou enter the hallway and find yourself in a room with ... a dragon!\nInitiating combat\n"
        typePrint(room9)
        stat = f"\nStats:\nYour health: {user_health}\nDragon's health: {mini_boss_health}\n"
        typePrint(stat)
        while True:
            user_damage = userAttack()
            mini_boss_health -= user_damage
            if mini_boss_health <= 0 or user_health <= 0:
                break
            stat1 = f"\nStats:\nYour health: {user_health}\nDragon's health: {mini_boss_health}\n"
            typePrint(stat1)
            boss_damage = miniBossAttack()
            user_health -= boss_damage
            if mini_boss_health <= 0 or user_health <= 0:
                break
            stat2 = f"\nStats:\nYour health: {user_health}\nDragon's health: {mini_boss_health}\n"
            typePrint(stat2)
        # if someone dead, check who.
        if user_health <= 0:
            userDead()
        else:
            mini_boss_dead = True
            victory = "\nYou defeeated the dragon! You have been granted a new move called 'Fireball!'\nAfter defeating the dragon, you look around and only see the hallway you came in through.\n"
            typePrint(victory)
            moves["fireball"] = 13
    else:
        walkin = "\nYou walk into the room and it is empty. You remember that this is where you fought and defeated that dragon.\nMove to a different room.\n"
        typePrint(walkin)
    while True:
        hallway = input("Would you like to go back a room:\nYes\n").upper().strip()
        if hallway == "YES":
            roomSix()
            break
        else:
            print("You have to go back to the previous room, please type 'Yes'")
            continue

def roomTen():
    global final_boss_health
    global user_health
    global god_gift
    global moves

    # Setting up the god_gift thing
    if god_gift == True:
        for value in moves.values():
            value += 4

    room10 = "\nYou enter the hallway and find yourself in a room filled with spider webs. Something laughs above you...\n"
    typePrint(room10)
    time.sleep(1)
    monologue = "'MWAHAHAHAHAHAHA!'\n'What have we got here?'\n'Is it someone who dares chalenge me?'\n'I'm sure you have seen the bodies in this cave, what makes you think you can defeat me?'\nKALLACKS: Eight Legged Scourge of the Caves\n'Are you ready to do this, child?'\n\nInitiating combat\n"
    typePrint(monologue)
    stat = f"\nStats:\nYour health: {user_health}\nKallacks' health: {final_boss_health}\n"
    typePrint(stat)
    while True:
        user_damage = userAttack()
        final_boss_health -= user_damage
        if final_boss_health <= 0 or user_health <= 0:
            break
        stat1 = f"\nStats:\nYour health: {user_health}\nKallacks' health: {final_boss_health}\n"
        typePrint(stat1)
        boss_damage = finalBossAttack()
        user_health -= boss_damage
        if final_boss_health <= 0 or user_health <= 0:
            break
        stat2 = f"\nStats:\nYour health: {user_health}\nKallacks' health: {final_boss_health}\n"
        typePrint(stat2)
    # if someone dead, check who.
    if user_health <= 0:
        userDead() 
    else:
        victory = "\n'NOOOOOOOOOOOOOO! HOW COULD YOU DEFEAT ME?\n I AM KALLACKS, THE MOST POWERFUL MONSTER OUT THERE!\nHOW?\nHOOOOOWWW???'\n"
        typePrint(victory)
        continued = "Kallacks stummbles and finally falls down, limp and dead.\n"
        typePrint(continued)
        exitRoom()

def exitRoom():
    entry = "\nWalking past his corpse, you enter a room that seems to be glowing with the light of the setting sun.\nThere is a hole in the ceiling and you scrammble your way out.\nThere is a village and you see three figure standing at the village entrance talking with the locals.\nCould it be?\nIt is! It's your family you were separated from!\nSprinting your way to them, they catch you in a tight group hug.\nYou tell them about your journey through the caves and what you did.\nEveryone smiles and you decide to stay in the village for the night before continuing on your big family travels.\n"
    typePrint(entry)

def userAttack():
    global moves
    global arrows
    global full_health_potions
    global user_health
    global user_full_health
    global splash_potions
    print("\nIt is your turn!")
    # potential moves: sword, broadsword, heal, splash potion, daggers, bow, spear, fireball
    while True:
        for key in moves.keys():
            print(f"'{key}' Damage: {moves[key]}")
        print(f"You can also 'Heal' (get back to full health) and throw a 'Splash potion' (damage enemy from afar)\nYou have {full_health_potions} heal potions and {splash_potions} splash potions\n")
        move = input("What would you like to do? (Type the name of the move):\n").upper().strip()
        if move == "SWORD":
            dmg = moves["sword"]
            return dmg
        elif move == "BROADSWORD":
            dmg = moves["broadsword"]
            return dmg
        elif move == "DAGGERS":
            dmg = moves["daggers"]
            return dmg
        elif move == "BOW":
            if arrows >= 1:
                dmg = moves["bow"]
                arrows -= 1
                return dmg
            else:
                print("You are out of arrows! Pick a different move")
                continue
        elif move == "SPEAR":
            dmg = moves["spear"]
            return dmg
        elif move == "FIREBALL":
            dmg = moves["fireball"]
            return dmg
        elif move == "HEAL":
            if full_health_potions >= 1:
                user_health = user_full_health
                full_health_potions -= 1
                dmg = 0
                return dmg
            else:
                print("You don't have any heal potions to use.\nPlease pick a different move.")
                continue
        elif move == "SPLASH POTION":
            if splash_potions >= 1:
                dmg = 20
                splash_potions -= 1
                return dmg
            else:
                print("You don't have any splash potions to use.\nPlease pick a different move.")
                continue
        else:
            print("Invalid input, please try again")

def miniBossAttack():
    land_attack = random.randint(1, 20)
    print("\nIt's the dragon's turn!")
    move = random.randint(1, 3)
    if move == 1:
        # move is tail swing. 5 damage
        if land_attack > user_armor:
            print("They hit!")
            dmg = 5
            return dmg
        else:
            print("The Dragon missed!")
            dmg = 0
            return dmg
    elif move == 2:
        # move is bite. 8 damage
        if land_attack > user_armor:
            print("They hit!")
            dmg = 8
            return dmg
        else:
            print("The Dragon missed!")            
            dmg = 0
            return dmg
    elif move == 3:
        # move is fire spite. 9 damage
        if land_attack > user_armor:
            print("They hit!")
            dmg = 9
            return dmg
        else:
            print("The Dragon missed!")
            dmg = 0
            return dmg
    else:
        print("The Dragon missed!")
        dmg = 0
        return dmg

def finalBossAttack():
    land_attack = random.randint(1, 20)
    print("\nIt's Kallacks's turn!")
    move = random.randint(1, 3)
    if move == 1:
        # move is charge. 8 damage
        if land_attack > user_armor:
            print("He hit!")
            dmg = 8
            return dmg
        else:
            print("Kallacks missed!")
            dmg = 0
            return dmg
    elif move == 2:
        # move is web up. 5 damage
        if land_attack > user_armor:
            print("He hit!")
            dmg = 5
            return dmg
        else:
            print("Kallacks missed!")
            dmg = 0
            return dmg
    elif move == 3:
        # move is poison. 10 damage
        if land_attack > user_armor:
            print("He hit!")
            dmg = 10
            return dmg
        else:
            print("Kallacks missed!")
            dmg = 0
            return dmg
    else:
        print("Kallacks missed!")
        dmg = 0
        return dmg

def userDead():
    died = "Shucks, you died!\n"
    typePrint(died)

user_health = 30
user_full_health = 30
user_armor = 8
full_health_potions = 0
splash_potions = 0
god_gift = False
gift_of_fire = False
arrows = 0
moves = {
    
}
picked_up_sword = False
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

mini_boss_health = 30
final_boss_health = 70

# Begin actual game
while True:
    name = input("Welcome, what is your name:\n").title().strip()
    welcome = f"Welcome {name}!\nAre you ready to begin your adventure?\nIf your are, hit the 'Enter' key on your keyboard.\n"
    typePrint(welcome)
    # wait for user to hit enter
    stop_event = threading.Event()
    thread = threading.Thread(target=flashingText1, args=(stop_event,))
    thread.start()
    input()
    stop_event.set()
    thread.join()
    # more game
    backstory = "\nYou are a young Paladin who was traveling with your family on a big adventure together,\nwhen suddenly...\nYou all were walking along this wide river. You and your sibling decided to check out a rock hill nearby.\nYou poke around the rocks and find a loose one.\nWhile nudging it, it falls away and you fall into the rocks!\nYou hear your sibling scream in response to you falling away.\nSlinding down what every you fell into, you hit the bottom and everything goes black for a minute.\n"
    typePrint(backstory)
    startRoom()
    ending = "Thank you for playing!\n"
    typePrint(ending)
    play = input("Play again? 'Yes' or 'No':\n").upper().strip()
    if play == "YES":
        print("The game will restart in five seconds")
        time.sleep(5)
        continue
    else:
        print("The game will not be played again.\nThank you for playing!")
        break