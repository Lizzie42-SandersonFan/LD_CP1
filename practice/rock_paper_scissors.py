# LD 2nd Rock, Paper, Scissors Practice
import time
import random


delay = 0.06
player_score = 0
computer_score = 0
opening = "Welcome to Rock Paper Scissors!\n"

for char in opening:
    print(char, end="", flush=True)
    time.sleep(delay)

while True:
    computer_play = random.randint(1,3)
    play_print = """Would you like to play
    (1) Rock
    (2) Paper
    (3) Scissors
    (4) Exit
Enter the corisponding number for play:\n"""

    for char in play_print:
        print(char, end="", flush=True)
        time.sleep(delay)

    player_choice = input()

    # Ways to Win: Rock > scissors, Paper > rock, Scissors > paper

    # Player Wins if
    if player_choice == '4':
        print("Thank you for playing!")
        break
    elif player_choice == '1' and computer_play == 3:
        print("You won!!")
        player_score += 1
    elif player_choice == '2' and computer_play == 1:
        print("You won!!")
        player_score += 1
    elif player_choice == '3' and computer_play == 2:
        print("You won!!")
        player_score += 1
    # Computer Win if
    elif computer_play == 1 and player_choice == '3':
        print("Sorry, the computer beat you!")
        computer_score += 1
    elif computer_play == 2 and player_choice == '1':
        print("Sorry, the computer beat you!")
        computer_score += 1
    elif computer_play == 3 and player_choice == '2':
        print("Sorry, the computer beat you!")
        computer_score += 1
    # Draw if
    elif computer_play == 1 and player_choice == '1':
        print("Oh No! Must have been a draw!")
    elif computer_play == 2 and player_choice == '2':
        print("Oh No! Must have been a draw!")
    elif computer_play == 3 and player_choice == '3':
        print("Oh No! Must have been a draw!")
    else:
        print("How was this triggered?")

    score_display = f"Your Score: {player_score}\nComputer Score: {computer_score}\n\n"
    for char in score_display:
        print(char, end="", flush=True)
        time.sleep(delay)