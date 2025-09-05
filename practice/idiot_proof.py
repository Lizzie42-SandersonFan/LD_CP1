# LD 2nd Idiot Proof

# Functions
def phoneQuestionOne():
    global phone_num_pt_one
    global valid_one
    global length_one

    phone_num_pt_one = input("What are the first three numbers of your phone number (Area code):\n")
    valid_one = phone_num_pt_one.isdigit()
    #print(valid_one)
    length_one = len(phone_num_pt_one)
    #print(length_one)

def phoneQuestionTwo():
    global phone_num_pt_two
    global valid_two
    global length_two

    phone_num_pt_two = input("\nWhat are the second three numbers of your phone number:\n")
    valid_two = phone_num_pt_two.isdigit()
    #print(valid_two)
    length_two = len(phone_num_pt_two)
    #print(length_two)

def phoneQuestionThree():
    global phone_num_pt_three
    global valid_three
    global length_three

    phone_num_pt_three = input("\nWhat are the last four numbers of your phone number:\n")
    valid_three = phone_num_pt_three.isdigit()
    #print(valid_three)
    length_three = len(phone_num_pt_three)
    #print(length_three)

def GPACheck():
    global gpa
    global rounded_gpa

    gpa = float(input("\nWhat is (or was) your high school GPA (Grade Point Average):\n"))
    busted_gpa = gpa.isalpha()
    rounded_gpa = round(gpa, 1)

# Start of questions
# Name question
name = input("What is your name:\n").strip().title()

# Phone Question One
phoneQuestionOne()
# if checking if the input contains three numbers and is the correct length
if valid_one == True and length_one == 3:
    pass
    # Passing because nothing needs to be done, the next question is called later 
else:
    print("Sorry, that is not a valid input. Please try again.\n")
    phoneQuestionOne()

# Phone Question Two
phoneQuestionTwo()
# if checking if the input contains three numbers and is the correct length
if valid_two == True and length_two == 3:
    pass
    # Passing because nothing needs to be done, the next question is called later
else:
    print("Sorry, that is not a valid input. Please try again.\n")
    phoneQuestionTwo()

# Phone Question Three
phoneQuestionThree()
# if checking if the input contains three numbers and is the correct length
if valid_three == True and length_three == 4:
    pass
    # Passing because nothing needs to be done, the next question is called later
else:
    print("Sorry, that is not a valid input. Please try again.\n")
    phoneQuestionThree()

phone_number = phone_num_pt_one + " " + phone_num_pt_two + " " + phone_num_pt_three

# GPA Question
GPACheck()
# IF TO SEE IF GPA IN NOT EQUAL TO ALPHA

# Final Output
print(f"Hello {name}. The phone number to reach you is {phone_number} and your high school GPA is/was {rounded_gpa}.")