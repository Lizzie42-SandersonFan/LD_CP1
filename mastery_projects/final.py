# LD 2nd Final for Class

# FUNCTIONS
# User attack(attacks){
    # Show user what they can do and have them pick. this can be accessed from getting the user dict index for the attacks
    # Determine what user picked and calculate subsiquent damage
    # return damage delt
# }

# mini boss attack(){
    # Have pick random number to determine attack
    # Determine what nummber picked and calculate subsiquent damage
    # return damage delt
# }

# final boss attack(){
    # Have pick random number to determine attack
    # Determine what nummber picked and calculate subsiquent damage
    # return damage delt
# }

# VARIABLES
# user dict{
    # health : 30
    # attacks {
        # sword : damge
        # Bow if aquired : damage
        # GIFT_OF_FIRE if aquired : damage
        # dodge : True/False
        # heal : reset health
    #}
#}
# the corpses and if they have been raided
# BACKSTORY "lots of words"
# USER_ROOM_CHOICE
# FINAL_BOSS_MONOLOGUE "lots of words"
# ENDING "lots of words that can change based on result of final boss fight"

# STORY
# give user BACKSTORY: They fell into a deep cave system when travaling with their family. They cannot go back the way they came, so they have to navigate the caves.
# print BACKSTORY to make it look like its typing

# there are two room the user could go into. Both rooms will have a corpse in them for the user to raid.

# room one will give the user a health bonus of plus 5 to default health
# room two will give the user a healing potion that will restore the user to full health

# From room one: there are three rooms. room one is God and they will grand a plus 7 attack damage for all weapons. This can use GOD_GIFT (add to user attacks dict) to determine if a weapone gets an upgrade and this room can lead to another corpse room or to the final boss where on the way, the user is given another heal potion. Room two is more corpses to raid, they can grant daggers, heal potions, potions to throw at the enemy, other stuff. Room three will lead to a room wil more bodies and this room will lead to the fianl boss and grant a weapon.
# From room two: the first choice will lead to the same room as choice 3 in room one. Choice two will lead to probably a chest will OP arrmor and this connects to mini boss and final boss. Choice three will lead to another room with corpses.

# In God room: the user sees a giant flash of light, temporally blinding them while a figure decends from the light. God speaks: "Welcome brave traveler. There are chalenges awiting you further into this cave. To help you, I have decided to grand you more power in your attacks. Use this power wisely." God leaves, GOD_GIFT = True, this affects weapon's damage, now user can go back to previous room or advance to final boss

# In the mini boss room: user will fight a dragon with 50 health. When defeated, the user will recive the GIFT_OF_FIRE(add to user attacks dict) and this is a new attack that will do fire damage
# LOOP for mini boss{
    # User goes first. Call user attack function
    # If statements to check if someone dead
    # mini boss's turn. Call its attack function
    # if statemets to check if someones dead
#}

# In Final Boss room: Big Spider has monologue "ha..ha..ha You have fallen into my trap like so many have before you. *big spider decends from celing* Dozens have come before and all have failed, what makes you think you can defeate me? *user squares up* Pitiful. I gues I get to add you to my calorie count!" Combat begins.
# LOOP for final boss{
    # User goes first. Call user attack function
    # If statements to check if someone dead
    # Spider's turn. Call its attack function
    # if statemets to check if someones dead
#}

# if user died: ENDING = "HAHAHAHAHAHA I beat you! I knew I would *user dies*" Ask if user wants to play again