# LD 2nd Basic Calculator Practice

# (Addition, Subtraction, Multiplication, Division, Integer Division and Modulo, and Exponents)
# You will need 2 different inputs
# Convert to correct data types to run equations
# Your output needs to include the written equation and the result
# All floats need to be rounded to 2 decimal places
# Use a while loop to make the code run till the user chooses to leave (you will need a while loop).  Then let the user select which equation they would like to run instead of running all of them (You can do this with a conditional or with match)

# Functions(?) for asking questions
def numOneAsk():
    global num_one
    global one_validation
    num_one = int(input("Give me a WHOLE number:\n"))
    one_validation = num_one.isdigit()

def numTwoAsk():
    global num_two
    num_two = int(input("Give me another WHOLE number:\n"))

def equationChoiceAsk():
    global equation_choice
    equation_choice = input("Which equation would you like to do (Type corresponding number)\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Integer Division/Modulo 6) Exponants \n\n")


# Ask questions first time
numOneAsk()

# Ifs to check inputs
if one_validation == True:
    numTwoAsk()
else:
    print("That is not a valid input, please try again.")
    numOneAsk()

if num_two == int:
    equationChoiceAsk()
else:
    print("That is not a valid input, please try again.")
    numTwoAsk()
# While loop to run the equations and periodicly ask if they want to stop
