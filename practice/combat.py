# LD 2nd Combat Program Practice
import random
import time
delay = 0.06

# Step one: Get user stats by having them select the type of fighter to play
welcome = "Welcome combatant! There are a couple of questions before fighting begins.\n"
for char in welcome:
    print(char, end="", flush=True)
    time.sleep(delay)
name = input("What is your name: ").strip().capitalize()
while True:
    class_choice = int(input("What class would you like to play as:\n1 for Bard\n2 for Rogue\n3 for Warlock\n4 for Wizard\n"))
    if class_choice == 1 or class_choice == 2 or class_choice == 3 or class_choice == 4:
        break
    else:
        print("Invalid choice. Try again")
        continue

# Step 1.5: make turn functions
def playerTurn(attack_method):
    # First display action options and have the user pick one
    while True:
        choice = int(input(f"What would you like to do:\n1 for attack with {attack_method}\n2 for Super Attack (deal 2x damage but also damage yourself)\n3 for heal (+5 health back)\n4 for dodge\n"))
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            break
        else:
            print("Invalid choice. Try again")
            continue
    # Return the choice
    return choice
    

def monsterTurn():
    # Have a random number selected. The random number will determine weather the monster does one attack or a different attack
    monster_move = random.randint(1,3)
    # Return the choice
    return monster_move

# Step two: Describe the combat situation. Show stats, tell what is being fought, and tell whos turn it is by rolling initiative using random.
if class_choice == 1:
    class_name = "Bard"
    health = 22
    aromor = 13
    attack = random.randint(1,21) + 3
    atk_print = "1d20 + 3"
    damage = random.randint(1,7) + 2
    dmg_print = "1d6 + 2"
    weapon = "Shortsword"
elif class_choice == 2:
    class_name = "Rogue"
    health = 26
    aromor = 13
    attack = random.randint(1,21) + 4
    atk_print = "1d20 + 4"
    damage = random.randint(1,7) + 3
    dmg_print = "1d6 + 3"
    weapon = "Dagger"
elif class_choice == 3:
    class_name = "Warlock"
    health = 22
    aromor = 13
    attack = random.randint(1,21) + 3
    atk_print = "1d20 + 3"
    damage = random.randint(1,7) + 2
    dmg_print = "1d6 + 2"
    weapon = "Dagger"
elif class_choice == 4:
    class_name = "Wizard"
    health = 22
    aromor = 12
    attack = random.randint(1,21) + 3
    atk_print = "1d20 + 3"
    damage = random.randint(1,9) + 2
    dmg_print = "1d8 + 2"
    weapon = "Longsword"
else:
    print("Something went horribly wrong...")

stats_show = f"Great, here are your stats for {class_name}!\nHealth: {health}\nDefense: {aromor}\nAttack: {atk_print}\nDamage: {dmg_print}\n"
for char in stats_show:
    print(char, end="", flush=True)
    time.sleep(delay)
print("You are fighting a Giant Badger!")
badger_health = 15
badger_aromor = 13
while True:
    player_initiative = random.randint(1,21)
    badger_initiative = 10
    player_dodge = False
    # \/ Badger stats to be randomized
    badger_attack = random.randint(1,21) + 3
    badger_bite = random.randint(1,7) + 1
    badger_claws = random.randint(1,5) + random.randint(1,5) + 1
    # \/ Player stats that need to be randmized every time
    if class_choice == 1:
        attack = random.randint(1,21) + 3
        damage = random.randint(1,7) + 2
    elif class_choice == 2:
        attack = random.randint(1,21) + 4
        damage = random.randint(1,7) + 3
    elif class_choice == 3:
        attack = random.randint(1,21) + 3
        damage = random.randint(1,7) + 2
    elif class_choice == 4:
        attack = random.randint(1,21) + 3
        damage = random.randint(1,9) + 2
    else:
        print("Something went horribly wrong...")
    # If player goes first: 
    if player_initiative >= badger_initiative:
        # Have them select type of move choice via function
        info = f"\nIt is your turn!\nHere are the stats:\nYour Health: {health}\nWeapon in Use: {weapon}\nGiant Badger Health: {badger_health}\n\n"
        for char in info:
            print(char, end="", flush=True)
            time.sleep(delay)
        attack_choice = playerTurn(weapon)
        # 1 = attack, 2 = super attack, 3 = heal (+5), 4 = dodge
        if attack_choice == 1:
            # player is aatacking and need to ckeck if attack roll is succesful. If it is, do damage to enemy
            if attack >= 13:
                badger_health -= damage
                print(f"You hit! You did {damage} damage to the Giant Badger!")
            else:
                print("You did not hit! Your turn is over.")
        elif attack_choice == 2:
            # player is super attacking. Check if roll is successful and do double damage to enemy
            if attack >= 16: # Higher because its a stronger move and should be harder to do
                badger_health -= (damage*2)
                health -= 3
                print(f"You hit! You did {damage*2} damage to the Giant Badger!")
            else:
                print("You did not hit! Your turn is over.")
        elif attack_choice == 3:
            # player is healing. Add 5 to health. I guess its fine if they go over starting health. I dont want to figure that out
            health += 5
            print(f"You healed! You are now at {health} HP")
        else:
            # player is dodging. Set dodge to true so it can be used when badger attacks. Make sure to reset it at the end of turn
            player_dodge = True
            display = "You are ready to dodge when the Giant Badger tries to attack!\nBe warned, if the Giant Badger does not land the attack, you will not be able to dodge the next time.\n\n"
            for char in display:
                print(char, end="", flush=True)
                time.sleep(delay)

    # If enemy goes first:
    if badger_initiative > player_initiative:
        print("It's the Giant Badger's turn!")
    # Have enemy do its move via function
        monster_attack = monsterTurn()
        if monster_attack == 1:
            # Bite attack: damage = 4(1d6 + 1)
            if badger_attack > aromor:
                if player_dodge == True:
                    print("The Giant Badger attacked you, but you dodged!")
                else:
                    health -= badger_bite
                    print(f"You have been bitten by the Giant Badger! You took {badger_bite} damage!")
            else:
                print("The Giant Badger did not hit you!")
        else:
            # Claws attack: damage = 6(2d4 + 1)
            if badger_attack > aromor:
                if player_dodge == True:
                    print("The Giant Badger attacked you, but you dodged!")
                else:
                    health -= badger_claws
                    print(f"You have been cut by the Giant Badger's claws! You took {badger_claws} damage!")
            else:
                print("The Giant Badger did not hit you!")
    player_dodge = False

    # If somehow both combatants ended at 0 health at the same time
    if health <= 0 and badger_health <= 0:
        end = "\nYou and the Giant Badger both died at the same time!"
        for char in end:
            print(char, end="", flush=True)
            time.sleep(delay)
        break
    # If enemy health is less than or equal to 0
    elif badger_health <= 0 and health > 0:
        # end the game and display the player won
        end = f"\nYou defeated the Giant Badger!!!\nCongradulations {name}!!!!\n"
        for char in end:
            print(char, end="", flush=True)
            time.sleep(delay)
        break
    # If player health is less than or equal to 0
    elif health <= 0 and badger_health > 0:
        # end the game and tell the player they died and lost
        end = "\nOh no!! You were killed by the Giand Badger!! Game Over"
        for char in end:
            print(char, end="", flush=True)
            time.sleep(delay)
        break
    # If both combatants are above 0
    else:
        # Both players should be above 0
        continue
# End of while game loop