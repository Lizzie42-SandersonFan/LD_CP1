# LD Crew Shares Mastery Project
import time
delay = 0.04

# KEY REMINDERS:
# You will need 2 different inputs (How much money earned and how many crew members there are)
# Your program should calculate the base share, captain's share, first mate's share, and what the crew still need to be paid
# The output has to change based on what the user has typed.
# Money needs to be rounded to 2 decimals

# INSTRUCTIONS
# The crew earned a whole bunch of money on the last outing (an input in dollars), but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. 
# The captain of the crew gets 7 shares (equal portions of the treasure)
# The first mate gets 3 shares
# Each member of the crew then gets 1 share, but the crew members have all already received $500.
# How much does the Captain get?  How much does the first mate get? How much needs to still be given to each member of the crew?

# Welcom user and give background
opening = "Hello! You are a captain on a ship and you and your crew just came back from an adventer looking for treasure.\nAfter your ship got to port, you didn't have enough time to calculate shares and just gave each of your crew members $500.\nThis progrm will calculate how much you, your first mate, and each crew member gets for you!\nBut first, some information is needed.\n"
for char in opening:
    print(char, end="", flush=True)
    time.sleep(delay)

# Get User inputs
treasure_earned = float(input("\nHow much did you and your team find on the adventure:\n"))
treasure_money = round(treasure_earned, 2)
crew_size = int(input("How many crew members are on your tem (Not Including You and the First Mate):\n"))

# Calculate base share


# Get Captain's Share (Base * 7)


# Get First Mate's Share (base * 3)


# Get crew's share STILL NEEDED (base - 500)


# Print Everything