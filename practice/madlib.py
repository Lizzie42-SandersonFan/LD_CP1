# LD 2nd Madlib Practice

# Used to make a cool printing effect :)
import time
delay = 0.03

# My functions - see line __ for start of running code
def usersStoryChoice():
    global story_choice
    story_choice = int(input("Would you like to do story one(1) or story two(2):\n"))
    if story_choice == 1:
        storyOne()
        stroyOneSentances()
    elif story_choice == 2:
        storyTwo()
        storyTwoSentances()
    else:
        print("That is not a valid input, please try again.")
        usersStoryChoice()


def storyOne():
    # Variables in order based on story outline
    global dragon_name
    global colection_noun_one
    global passed_tense_verb
    global colection_noun_two
    global first_adjective
    global second_adjective
    global silly_noun

    dragon_name = input("\nGive me a Name:\n").capitalize().strip()
    colection_noun_one = input("\nGive me a Noun:\n").lower().strip()
    passed_tense_verb = input("\nGive me a verb in PASSED TENSE: \n").lower().strip()
    colection_noun_two = input("\nGive me a NEW noun: \n").lower().strip()
    first_adjective = input("\nGive me an adjective: \n").lower().strip()
    second_adjective = input("\nGive me a NEW adjective: \n").lower().strip()
    silly_noun = input("\nGive me a silly noun: \n").lower().strip()

def stroyOneSentances():
    # Sentance variables concatinated to be printed later
    global first_sentance
    global second_sentance
    global third_sentance
    global fourth_sentance
    global fifth_sentance
    global story

    first_sentance = dragon_name + " the Dragon needed a new thing to colect after finishing his " + colection_noun_one + " colection."

    second_sentance = dragon_name + " " + passed_tense_verb + " around his base, admiring each room deticated to a colection."

    third_sentance = "There was the " + colection_noun_two + " colection and it was very " + first_adjective + "."

    fourth_sentance = "After examining each of his " + second_adjective + " colections, " + dragon_name + " decided to do a " + silly_noun + " colection."

    fifth_sentance = dragon_name + " smiled at the idea of a " + silly_noun + " colection, and immediately got to work."

    story = first_sentance + " " + second_sentance + " " + third_sentance + " " + fourth_sentance + " " + fifth_sentance + "\n"

    for char in story:
        print(char, end="", flush=True)
        time.sleep(delay)

def storyTwo():
    # Story outline: On a [adjective] Halloween night, a [creature] crept out of the [place] holding a glowing [noun]. [Same creature] was searching for a [adjective] [object] said to be hidden behind the old [building]. Suddenly, a [same adjective] [same occupation] appeared, riding a flying [animal] and shouting [silly word]! They both screamed and ran through a forest full of [plural noun]. In the end, they shared a bag of [candy type] and promised to meet again next [holiday].
    global adjective_one
    global creature
    global place
    global noun_one
    global adjective_two
    global occupation
    global building
    global animal
    global silly_word
    global plural_noun
    global candy_type
    global holiday

    adjective_one = input("\nGive me a adjective:\n").lower().strip()
    creature = input("\nGive me a type of creature:\n").capitalize().strip()
    place = input("\nGive me a place: \n").lower().strip()
    noun_one = input("\nGive me a noun: \n").lower().strip()
    adjective_two = input("\nGive me another adjective: \n").lower().strip()
    occupation = input("\nGive me an occupation: \n").lower().strip()
    building = input("\nGive me a building type: \n").lower().strip()
    animal = input("\nGive me an animal: \n").lower().strip()
    silly_word = input("\nGive me a silly word: \n").lower().strip()
    plural_noun = input("\nGive me a plural noun: \n").lower().strip()
    candy_type = input("\nGive me a type of candy: \n").lower().strip()
    holiday = input("\nGive me a holiday: \n").capitalize().strip()

def storyTwoSentances():
    # Sentance variables concatinated to be printed later
    global first_sentance
    global second_sentance
    global third_sentance
    global fourth_sentance
    global fifth_sentance
    global story

    first_sentance = "On a " + adjective_one + " Halloween night, a " + creature + " crept out of the " + place + " holding a glowing " + noun_one + "."

    second_sentance = creature + " was searching for a(n) " + adjective_two + " " + occupation + " said to be hidden behind the old " + building + "."

    third_sentance = "Suddenly, a " + adjective_two + " " + occupation + " appeared, riding a flying " + animal + " and shouting " + silly_word + "!"

    fourth_sentance = "They both screamed and ran through a forest full of " + plural_noun + "."

    fifth_sentance = "In the end, they shared a bag of " + candy_type + " and promised to meet again next " + holiday + "."

    story = first_sentance + " " + second_sentance + " " + third_sentance + " " + fourth_sentance + " " + fifth_sentance + "\n"

    for char in story:
        print(char, end="", flush=True)
        time.sleep(delay)

# Welcome
welcome_message = "Hello there! This a short Midlibs style game where you get to enter a word coresponding with the prompt.\n"
for char in welcome_message:
    print(char, end="", flush=True)
    time.sleep(delay)

story_choice = int(input("Would you like to do story one(1) or story two(2):\n"))

if story_choice == 1:
    storyOne()
    stroyOneSentances()
elif story_choice == 2:
    storyTwo()
    storyTwoSentances()
else:
    print("That is not a valid input, please try again.")
    usersStoryChoice()
