# LD Crew Shares Mastery Project
import time
delay = 0.04


# Welcom user and give background
opening = "Hello! You are a captain on a ship and you and your crew just came back from an adventure looking for treasure.\nAfter your ship got to port, you didn't have enough time to calculate shares and just gave each of your crew members $500.\nThis program will calculate how much you, your first mate, and each crew member gets for you!\nBut first, some information is needed.\n"
for char in opening:
    print(char, end="", flush=True)
    time.sleep(delay)

# Get User inputs
treasure_earned = float(input("\nHow much did you and your team find on the adventure(do Not include the $):\n"))
treasure_money = round(treasure_earned, 2)
crew_size = int(input("How many crew members are on your team (Not Including You and the First Mate):\n"))

# Calculate base share
base_share = treasure_money / (crew_size + 10)
rouned_share = round(base_share, 2)

# Get Captain's Share (Base * 7)
captain_base = rouned_share * 7
captains_share = round(captain_base, 2)

# Get First Mate's Share (base * 3)
first_mate_base = rouned_share * 3
first_mates_share = round(first_mate_base, 2)

# Get crew's share STILL NEEDED (base - 500)
crew_base = rouned_share - 500
crew_share_left = round(crew_base, 2)

# Print Everything
final_output = f"""
Calculations have been run! Here are the final results:\n
The money you earned was ${treasure_money:,}.
There are {crew_size} people on your ship crew, not including you and your first mate.
You, the captain, get ${captains_share:,} of the total ${treasure_money:,}.
Your First Mate gets ${first_mates_share:,} of the total ${treasure_money:,}.
Each member of your crew still needs ${crew_share_left:,} on top of their intial $500.
"""
for char in final_output:
    print(char, end="", flush=True)
    time.sleep(delay)