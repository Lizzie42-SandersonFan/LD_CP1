# LD 2nd Password Strength Checker Unit Final
import time
delay = 0.06

# First thing to do is to set up the user input for a password and other variables for later
password = input("Hello, please enter a password to be strength checked:\n")
password_score = 0
special_charcters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/"]
# I want my response to be "Score: {Score}. Strength: {Strength response}. {Anything the user is missing}"
# Next to find out if the password is long enough and get response parts set up. Also add one to PASSWORD_SCORE if there is
length = len(password)
if length >= 8:
    password_score += 1
    missing1 = "Your password is long enough"
else:
    missing1 = "Your password needs to be longer"
# Then we find out if the password has at least one uppercase and add one to PASSWORD_SCORE if there is
uppercase = any(char.isupper() for char in password)
if uppercase == True:
    password_score += 1
    missing2 = "You have an uppercase letter"
else:
    missing2 = "You need an Uppercase letter"
# Then find out if there is at least one lowercase and add one to PASSWORD_SCORE if there is
lowercase = any(char.islower() for char in password)
if lowercase == True:
    password_score += 1
    missing3 = "You have a lowercase letter"
else:
    missing3 = "You need an lowercase letter"
# Then find out if there is at least one number and add one to PASSWORD_SCORE if there is
digit = any(char.isdigit() for char in password)
if digit == True:
    password_score += 1
    missing4 = "You have a digit"
else:
    missing4 = "You need a digit"
# Then find out if there is at least one special character and add one to PASSWORD_SCORE if there is
for char in password:
    if char in special_charcters:
        missing5 = "You have a special character"
        password_score +=1 
        break
else:
    missing5 = "You need a special character in your password"

# After the password is checked, we use variable responses from above to build a response to the user. If something is missing, we need to tell them such. This needs if to determine strength response
if password_score == 5:
    strength_response = "Your password is very strong"
elif password_score == 4:
    strength_response = "Your password is strong"
elif password_score == 3:
    strength_response = "Your password is moderate"
elif password_score == 2 or password_score == 1:
    strength_response = "Your password is weak"
else:
    strength_response = "Your password is terrible"
final_response = f"Your password: {password}\nScore: {password_score}\nStrength: {strength_response}\nFeedback:\n\t{missing1}\n\t{missing2}\n\t{missing3}\n\t{missing4}\n\t{missing5}"

for char in final_response:
    print(char, end="", flush=True)
    time.sleep(delay)