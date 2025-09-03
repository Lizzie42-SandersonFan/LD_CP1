# LD 2nd Madlib Practice

# Used to make a cool printing effect :)
import time
delay = 0.03


# My functions - see line __ for start of running code
def usersStoryChoice():
    return story_choice == int(input("Would you like to do story one(1) or story two(2):\n"))

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

    first_sentance = dragon_name + " the Dragon needed a new thing to colect after finishing his " + colection_noun_one + " colection."

    second_sentance = dragon_name + " " + passed_tense_verb + " around his base, admiring each room deticated to a colection."

    third_sentance = "There was the " + colection_noun_two + " colection and it was very " + first_adjective + "."

    fourth_sentance = "After examining each of his " + second_adjective + " colections, " + dragon_name + " decided to do a " + silly_noun + " colection."

    fifth_sentance = dragon_name + " smiled at the idea of a " + silly_noun + " colection, and immediately got to work."

def storyTwo():
    # Story outline: 
    pass

# Welcome
welcome_message = "Hello there! This a short Midlibs style game where you get to enter a word coresponding with the prompt.\n"
for char in welcome_message:
    print(char, end="", flush=True)
    time.sleep(delay)

story_choice = int(input("Would you like to do story one(1) or story two(2):\n"))

if story_choice == 1:
    print("Hello")
    storyOne()
elif story_choice == 2:
    print("Hi")
else:
    print("That is not a valid input, please try again.")
    usersStoryChoice()


# All sentances concatinated
story = first_sentance + " " + second_sentance + " " + third_sentance + " " + fourth_sentance + " " + fifth_sentance + "\n"


# Printing the story
for char in story:
    print(char, end="", flush=True)
    time.sleep(delay)