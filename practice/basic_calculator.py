# LD 2nd Basic Calculator Practice

# Functions for asking questions
def numOneAsk():
    global num_one
    num_one = int(input("Give me a WHOLE number:\n"))

def numTwoAsk():
    global num_two
    num_two = int(input("\nGive me another WHOLE number:\n"))

def equationChoiceAsk():
    global equation_choice
    equation_choice = int(input("\nWhich equation would you like to do (Type corresponding number)\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Integer Division/Modulo\n6) Exponants \n\n"))

    if equation_choice == equation_choice:
        pass
    else:
        print("That is not a valid input, please try again.")
        equationChoiceAsk()

    if equation_choice == 1:
        while equation_choice == 1:
            print(f"{num_one} + {num_two} = {num_two + num_two}")
            stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
            if stop == "YES":
                break
            else:
                pass
    elif equation_choice == 2:
        while equation_choice == 2:
            print(f"{num_one} - {num_two} = {num_two - num_two}")
            stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
            if stop == "YES":
                break
            else:
                pass
    elif equation_choice == 3:
        while equation_choice == 3:
            print(f"{num_one} * {num_two} = {num_two * num_two}")
            stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
            if stop == "YES":
                break
            else:
                pass
    elif equation_choice == 4:
        while equation_choice == 4:
            print(f"{num_one} / {num_two} = {num_two / num_two}")
            stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
            if stop == "YES":
                break
            else:
                pass
    elif equation_choice == 5:
        while equation_choice == 5:
            print(f"{num_one} % {num_two} = {num_two % num_two}")
            stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
            if stop == "YES":
                break
            else:
                pass
    elif equation_choice == 6:
        while equation_choice == 6:
            print(f"{num_one} ** {num_two} = {num_two ** num_two}")
            stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
            if stop == "YES":
                break
            else:
                pass
    else:
        print("That is not a valid input, please try again.")
        equationChoiceAsk()

# Ask questions first time
numOneAsk()

# Ifs to check inputs
if num_one == num_one:
    numTwoAsk()
else:
    print("That is not a valid input, please try again.")
    numOneAsk()

if num_two == num_two:
    equationChoiceAsk()
else:
    print("That is not a valid input, please try again.")
    numTwoAsk()

if equation_choice == equation_choice:
    pass
else:
    print("That is not a valid input, please try again.")
    equationChoiceAsk()

#Ifs that check the problem choice and then do a while loop
if equation_choice == 1:
    while equation_choice == 1:
        print(f"{num_one} + {num_two} = {num_two + num_two}")
        stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
        if stop == "YES":
            break
        else:
            pass
elif equation_choice == 2:
    while equation_choice == 2:
        print(f"{num_one} - {num_two} = {num_two - num_two}")
        stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
        if stop == "YES":
            break
        else:
            pass
elif equation_choice == 3:
    while equation_choice == 3:
        print(f"{num_one} * {num_two} = {num_two * num_two}")
        stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
        if stop == "YES":
            break
        else:
            pass
elif equation_choice == 4:
    while equation_choice == 4:
        print(f"{num_one} / {num_two} = {num_two / num_two}")
        stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
        if stop == "YES":
            break
        else:
            pass
elif equation_choice == 5:
    while equation_choice == 5:
        print(f"{num_one} % {num_two} = {num_two % num_two}")
        stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
        if stop == "YES":
            break
        else:
            pass
elif equation_choice == 6:
    while equation_choice == 6:
        print(f"{num_one} ** {num_two} = {num_two ** num_two}")
        stop = input("\nWould you like to stop the code (YES or NO):\n").upper().strip()
        if stop == "YES":
            break
        else:
            pass
else:
    print("That is not a valid input, please try again.")
    equationChoiceAsk()