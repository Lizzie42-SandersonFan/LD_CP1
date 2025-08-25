# LD 2nd Advanced Who Are You

# Have the program save each person's information, if a name is given for someone who has already been in the program then instead of asking the last two questions, tell them what they have already answered. (this program should just keep running)
# Trying to use dictionaries for the repeat users

name = input("What is your name: ")
age = input("Great, how old are you: ")
fav_color = input("Last one, what is your favorite color: ")

user_dict_one = {
    "name": name,
    "age": age,
    "fav_color": fav_color
}

print(name, "is", age, "years old and", fav_color, "is their favorite color!")