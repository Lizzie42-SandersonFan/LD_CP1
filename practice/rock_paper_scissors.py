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
    player_alpha = player_choice.isalpha()

    # Ways to Win: Rock > scissors, Paper > rock, Scissors > paper

    # Player Wins if
    if (player_choice >= '5' or player_choice <= '0') or player_alpha == True:
        print("Sorry, that is not a valid input, please try again!\n")
        continue
    elif player_choice == '4':
        if player_score == computer_score:
            end = "It was a draw!\n"
        elif player_score > computer_score:
            end = "You beat the computer!!\n"
        elif computer_score > player_score:
            end = "Sorry, the computer beat you!!\n"
        else:
            end = "How in the world????\n"
        goodbye = f"Thank you for playing!!\nFinal Score:\nYou scored {player_score}\nComputer Scored {computer_score}\nASCII Art from 'wynand1004' on GitHub!\n"

        for char in goodbye:
            print(char, end="", flush=True)
            time.sleep(delay)
        time.sleep(1)
        for char in end:
            print(char, end="", flush=True)
            time.sleep(delay)
        break
    elif player_choice == '1' and computer_play == 3:
        print("""
You Played:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer Played:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              """
)
        print("You Won!!")
        player_score += 1
    elif player_choice == '2' and computer_play == 1:
        print("""
You Played:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
              
Computer Played:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You won!!")
        player_score += 1
    elif player_choice == '3' and computer_play == 2:
        print("""
You Played:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              
Computer Played:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You won!!")
        player_score += 1
    # Computer Win if
    elif computer_play == 1 and player_choice == '3':
        print("""
Computer Played:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You Played:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              """
)
        print("Sorry, the computer beat you!")
        computer_score += 1
    elif computer_play == 2 and player_choice == '1':
        print("""
Computer Played:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
              
You Played:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("Sorry, the computer beat you!")
        computer_score += 1
    elif computer_play == 3 and player_choice == '2':
        print("""
Computer Played:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              
You Played:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("Sorry, the computer beat you!")
        computer_score += 1
    # Draw if
    elif computer_play == 1 and player_choice == '1':
        print("""
You Played:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
              
Computer Played:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("Oh No! It's a draw!")
    elif computer_play == 2 and player_choice == '2':
        print("""
You Played:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
              
Computer Played:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("Oh No! It's a draw!")
    elif computer_play == 3 and player_choice == '3':
        print("""
You Played:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              
Computer Played:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("Oh No! It's a draw!")
    else:
        print("How was this triggered?")

    score_display = f"Your Score: {player_score}\nComputer Score: {computer_score}\n\n"
    for char in score_display:
        print(char, end="", flush=True)
        time.sleep(delay)