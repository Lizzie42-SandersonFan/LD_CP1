# LD 2nd Idiot Proof

#Create a program that takes in a users name, phone number and GPA. The program should change the inputs to be formatted correctly for their type (First and last name capitalized, all other letters lower case, phone number with spaces 000 000 0000 {remove the dashes}, and GPA as a float rounded to 1 decimal place.) 

# Minimum of 5 user inputs (all stored in separate variables)
# 3 separate inputs need to be created
# inputs need to have string methods to ensure that they are formatted correctly
# Output needs to display the users name, phone number and email address) 
# If a user types in something incorrectly make them answer the same question again until they type in a valid input for that question. 

name = input("What is your name:\n").strip().capitalize()
phone_num_pt_one = int(input("What are the first three numbers of your phone number (Area code):\n"))
# if checking if the input contains three numbers

phone_num_pt_two = int(input("\nWhat are the second three numbers of your phone number:\n"))
# if checking if the input contains three numbers

phone_num_pt_three = int(input("\nWhat are the last four numbers of your phone number:\n"))
# if checking if the input contains three numbers

gpa = float(input("\nWhat is (or was) your high school GPA (Grade Point Average):\n"))