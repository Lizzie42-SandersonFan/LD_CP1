# LD 2nd Functions Notes
# Set global variables
num = 0
player_hp = 100
monster_hp = 100

# Write functions
def add(x , y):
    return x+y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg

 
# Write code
while num < add(5, 5):
    print("Duck")
    num+=1
print("Goose")
print(f" Reswults is: {add(8746, 86135)}")
total = add(.57235, .4145658)
print(add(add(-436, 24643), 10))
add(42, 7)

print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Xavier's initials are: {initials("Xavier LaRose")}")
monster_hp, player_hp = attack(15, "monster")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

monster_hp, player_hp = attack(15, "player")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")