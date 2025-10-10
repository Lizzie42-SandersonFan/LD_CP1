# LD 2nd Password Strength Checker Unit Final

# First thing to do is to set up the user input for a password and variables for later
password = input("Hello, please enter a password to be strength checked:\n")
password_score = 0
special_charcters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/"]
# I want my response to be "Score: {Score}. Strength: {Strength response}. {Anything the user is missing}"
# Next to find out if the password is long enough and get response parts set up. Also add one to PASSWORD_SCORE if there is
length = len(password)
print(length)
if length >= 8:
    password_score += 1
else:
    missing1 = "Your password needs to be longer"
# Then we find out if the password has at least one uppercase and add one to PASSWORD_SCORE if there is
uppercase = any(char.isupper() for char in password)
if uppercase == True:
    password_score += 1
else:
    missing2 = "You need an Uppercase letter"
# Then find out if there is at least one lowercase and add one to PASSWORD_SCORE if there is
lowercase = any(char.islower() for char in password)
if lowercase == True:
    password_score += 1
else:
    missing3 = "You need an lowercase letter"
# Then find out if there is at least one number and add one to PASSWORD_SCORE if there is
digit = any(char.isdigit() for char in password)
if digit == True:
    password_score += 1
else:
    missing4 = "You need a digit"
# Then find out if there is at least one special character and add one to PASSWORD_SCORE if there is
special = False
for char in password:
    if char in special_charcters:
        pass # KEEP WORKING

# After the password is checked, we use variable responses from above to build a response to the user. If something is missing, we need to tell them such. This needs if to determine strength response