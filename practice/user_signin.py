# LD 2nd User Sign-In Practice

# You will need 2 user inputs
# Check for username
# Check for password
# Only output the welcome message if BOTH username and password are correct. 
# Have a selection of several different users with different passwords. Check to see if the username is one of the options, then check to see if the password matches for that given user. (I recommend using a list of users with the username and password set up as their own list)
# Ex: users = [["userone", "password"], ["usertwo", "diffpass"]]

users = [["lizzie.delong", "password123"], ["daniel.delong", "pAsSwOrD-OhBOY-WEEE"]]

user_name = input("What is your user name:\n")
user_password = input("What is your password:\n")

# How to acces list item in list from stack overflow: >>> list1 = [[10,13,17],[3,5,1],[13,11,12]] >>> list1[0][2] 17