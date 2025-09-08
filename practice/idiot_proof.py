# LD 2nd Idiot Proof

# Functions
def phoneQuestionOne():
    global phone_num_pt_one
    global valid_one
    global length_one

    phone_num_pt_one = input("\nWhat are the first three numbers of your phone number (Area code):\n")
    valid_one = phone_num_pt_one.isdigit()
    length_one = len(phone_num_pt_one)

    if valid_one == True and length_one == 3:
        pass
        # Passing because nothing needs to be done, the next question is called later 
    else:
        print("Sorry, that is not a valid input. Please try again.\n")
        phoneQuestionOne()

def phoneQuestionTwo():
    global phone_num_pt_two
    global valid_two
    global length_two

    phone_num_pt_two = input("\nWhat are the second three numbers of your phone number:\n")
    valid_two = phone_num_pt_two.isdigit()
    length_two = len(phone_num_pt_two)

    if valid_two == True and length_two == 3:
        pass
        # Passing because nothing needs to be done, the next question is called later
    else:
        print("Sorry, that is not a valid input. Please try again.\n")
        phoneQuestionTwo()

def phoneQuestionThree():
    global phone_num_pt_three
    global valid_three
    global length_three

    phone_num_pt_three = input("\nWhat are the last four numbers of your phone number:\n")
    valid_three = phone_num_pt_three.isdigit()
    length_three = len(phone_num_pt_three)

    if valid_three == True and length_three == 4:
        pass
        # Passing because nothing needs to be done, the next question is called later
    else:
        print("Sorry, that is not a valid input. Please try again.\n")
        phoneQuestionThree()


def GPACheck():
    global gpa
    global rounded_gpa
    global busted_gpa
    global gpa_length

    gpa = input("\nWhat is (or was) your high school GPA (Grade Point Average):\n")
    busted_gpa = gpa.isalpha()
    gpa_length = len(gpa)

    if busted_gpa == False and gpa_length <= 4:
        float_gpa = float(gpa)
        rounded_gpa = round(float_gpa, 2)
    else:
        print("That is not a valid input, please try again:\n")
        GPACheck()
    

# Start of questions
# Name question
name = input("What is your name:\n").strip().title()

# Phone Question One
phoneQuestionOne()
if valid_one == True and length_one == 3:
    pass
    # Passing because nothing needs to be done, the next question is called later 
else:
    print("Sorry, that is not a valid input. Please try again.\n")
    phoneQuestionOne()

# Phone Question Two
phoneQuestionTwo()
if valid_two == True and length_two == 3:
    pass
    # Passing because nothing needs to be done, the next question is called later
else:
    print("Sorry, that is not a valid input. Please try again.\n")
    phoneQuestionTwo()

# Phone Question Three
phoneQuestionThree()
if valid_three == True and length_three == 4:
    pass
    # Passing because nothing needs to be done, the next question is called later
else:
    print("Sorry, that is not a valid input. Please try again.\n")
    phoneQuestionThree()

phone_number = phone_num_pt_one + " " + phone_num_pt_two + " " + phone_num_pt_three

# GPA Question
GPACheck()
if busted_gpa == False and gpa_length <= 4:
    float_gpa = float(gpa)
    rounded_gpa = round(float_gpa, 2)
else:
    print("That is not a valid input, please try again:\n")
    GPACheck()

# Final Output
print(f"Hello {name}. The phone number to reach you is {phone_number} and your high school GPA is/was {rounded_gpa}.")