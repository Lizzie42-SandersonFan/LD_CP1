# LD 2nd Combat Program Practice
import random
import time
delay = 0.03

# Step one: Get user stats by having them select the type of fighter to play
welcome = "Welcome combatant! There are a couple of qestions before fighting begins."
for char in welcome:
    print(char, end="", flush=True)
    time.sleep(delay)
name = input("What is your name: ").strip().capitalize()
while True:
    class_choice = int(input("What class would you like to play as:\n1 for Bard\n2 for Rogue\n3 for Warlock\n4 for Wizard"))
    if class_choice != 1 or class_choice != 2 or class_choice != 3 or class_choice != 4:
        print("Invalid choice. Try again")
        continue
    else:
        break

# Step two: Describe the combat situation. Show stats, tell what is being fought, and tell whos turn it is by rolling initiative using random.
if class_choice == 1:
    class_name = "Bard"
    health = 22
    aromor = 13
    attack = random.randint(1,21) + 3
    damage = random.randint(1,7) + 2
    # Shortsword
elif class_choice == 2:
    class_name = "Rogue"
    health = 26
    aromor = 13
    attack = random.randint(1,21) + 4
    damage = random.randint(1,7) + 3
    # Dagger
elif class_choice == 3:
    class_name = "Warlock"
    health = 22
    aromor = 13
    attack = random.randint(1,21) + 3
    damage = random.randint(1,7) + 2
    # Dagger
elif class_choice == 4:
    class_name = "Wizard"
    health = 22
    aromor = 12
    attack = random.randint(1,21) + 3
    damage = random.randint(1,9) + 2
    # Longsword
else:
    print("Something went horribly wrong...")

stats_show = f"Great, here are your stats for {class_name}!\nHealth: {health}\nDefense: {aromor}\nAttack: {attack}\nDamage: {damage}\n"
# /\ print that
print("You are fighting a Giant Badger!")
player_initiative = random.randint(1,21)
badger_initiative = 10
# \/ Badger stats
badger_health = 15
badger_aromor = 13
badger_attack = random.randint(1,21)
badger_dmg = random.randint(1,5) + random.randint(1,5) + 1
# If player goes first: 
    # Have them select type of move choice
    # Check if the move's damage is greater than enemy's defense.
        # If it is, have enemy take damage and update health
        # If not, end turn and go to enemy's turn
# If enemy goes first:
# Have enemy do its move
    # Check if the move's damage is greater than player's defense.
        # If it is, have player take damage and update player's health
        # If not, end turn and go to player's turn

# If enemy health is less than or equal to 0
    # end the game and display the player won
# If player health is less than or equal to 0
    # end the game and tell the player they died and lost. Ask if they want to try again
# If both combatants are above 0
    # continue play