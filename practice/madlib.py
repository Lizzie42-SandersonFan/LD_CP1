# LD 2nd Madlib Practice

# Used to make a cool printing effect :)
import time
delay = 0.03

# 5 different user inputs
# 2 of the inputs must be used twice

# Story Out-Line:
# {Name} the Dragon needed a new thing to colect after finishing his {Noun i.e. gold} colection. {Same Name} {verb, pass tensed} around his base, admiring each room deticated to a colection.There was the {New Noun} colection; it was very {Adjective}. 
# After examining each of his {New Adjective} colections, {Same Name} decided to do a {Silly Noun} colection. {Same Name} smiled at the idea of a {Same Silly Noun} colection, and got to work.

# Welcome
welcome_message = "Hello there! This a short Midlibs style game where you get to enter a word coresponding with the prompt. Have fun!!"
for char in welcome_message:
    print(char, end="", flush=True)
    time.sleep(delay)

# Variables in order based on story outline
dragon_name = input("\nGive me a Name:\n").capitalize().strip()
colection_noun_one = input("\nGive me a Noun:\n").lower().strip()
passed_tense_verb = input("\nGive me a verb in PASSED TENSE: \n").lower().strip()
colection_noun_two = input("\nGive me a NEW noun: \n").lower().strip()
first_adjective = input("\nGive me an adjective: \n").lower().strip()
second_adjective = input("\nGive me a NEW adjective: \n").lower().strip()
silly_noun = input("\nGive me a silly/unusual noun: \n").lower().strip()

# Sentance variables concatinated to be printed later
first_sentance = dragon_name + " the Dragon needed a new thing to colect after finishing his " + colection_noun_one + " colection."

second_sentance = dragon_name + " " + passed_tense_verb + " around his base, admiring each room deticated to a colection."

third_sentance = "There was the " + colection_noun_two + " colection and it was very " + first_adjective + "."

fourth_sentance = "After examining each of his " + second_adjective + " colections, " + dragon_name + " decided to do a " + silly_noun + " colection."

fifth_sentance = dragon_name + " smiled at the idea of a " + silly_noun + " colection, and immediately got to work."

# All sentances concatinated
story = first_sentance + " " + second_sentance + " " + third_sentance + " " + fourth_sentance + " " + fifth_sentance + "\n"

# Printing the story
for char in story:
    print(char, end="", flush=True)
    time.sleep(delay)