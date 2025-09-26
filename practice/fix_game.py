# LD 2nd Fix the Game Practice
import random

# OG Code (commented because it is broken):

# def start_game():
    # print("Welcome to the Number Guessing Game!")
    # print("I'm thinking of a number between 1 and 100.")
    # number_to_guess = random.randint(1, 100)
    # max_attempts = 10
    # attempts = 0
    # game_over = False
    # while not game_over:
        # guess = input("Enter your guess: ")
        # if attempts >= max_attempts:
            # print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            # game_over = True
        # if guess == number_to_guess:
            # print("Congratulations! You've guessed the number!")
            # game_over = True
        # elif guess > number_to_guess:
            # print("Too high! Try again.")
        # elif guess < number_to_guess:
            # print("Too low! Try again.")  
        # continue
    # print("Game Over. Thanks for playing!")
# start_game()


# Fixed code :) \/ \/ \/ \/

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) # #1;I would call this a run-tim error because the input needs to be an int. Later we are comparing it to an int and strings cant be compared to ints. This would be something like an invalid input. See line 14
        print(number_to_guess)
        if attempts >= max_attempts:
            print(f"Sorry, you've used all 10 attempts. The number was {number_to_guess}.") # #2; Logic. Replaced the {max_attempts} with 10 because if the user ends up here, we want them to know they had 10 attemps and not 0 when they reach the end. See line 16
            game_over = True
        elif guess == number_to_guess: # #3 <- I would call this a syntax error because it should be an elif. That way we dont need a bigilion ifs. See line 18
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            max_attempts -= 1 # #4; Syntaxt error. you acctually need to subract an attempt. That way it doesn't keep going See line 22
        else: # And this should be an else. Ifs always need an else.
            print("Too low! Try again.")  
            max_attempts -= 1 # #4; Syntaxt error. you acctually need to subract an attempt. That way it doesn't keep going. See line 24
        continue
    print("Game Over. Thanks for playing!")

start_game() # Not an error. I added an extra line space so that it looks nicer.