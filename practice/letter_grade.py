# LD 2nd Letter Grade Practice
import time
delay = 0.06


# Great user
opening = "Hello!\nThis program can tell you what your letter grade is for a class based off the percentage given!\n\n"
for char in opening:
    print(char, end="", flush=True)
    time.sleep(delay)

# Get input of grade percentage
percent = float(input("What is your percentage grade for Programming class (DO NOT INCLUDE %):\n"))
grade_percent = round(percent, 2)
letter_grade = ""

# Check actual grade and get the letter
if grade_percent <= 200.00 and grade_percent >= 94.00: # <- 200 because someone may have extra credit
    letter_grade = "A"
    output = 1
elif grade_percent <= 93.99 and grade_percent >= 90.00:
    letter_grade = "A-"
    output = 1
elif grade_percent <= 89.99 and grade_percent >= 87.00:
    letter_grade = "B+"
    output = 1
elif grade_percent <= 86.99 and grade_percent >= 84.00:
    letter_grade = "B"
    output = 1
elif grade_percent <= 83.99 and grade_percent >= 80.00:
    letter_grade = "B-"
    output = 1
elif grade_percent <= 79.99 and grade_percent >= 77.00:
    letter_grade = "C+"
    output = 1
elif grade_percent <= 76.99 and grade_percent >= 74.00:
    letter_grade = "C"
    output = 1
elif grade_percent <= 73.99 and grade_percent >= 70.00:
    letter_grade = "C-"
    output = 1
elif grade_percent <= 69.99 and grade_percent >= 67.00:
    letter_grade = "D+"
    output = 1
elif grade_percent <= 66.99 and grade_percent >= 64.00:
    letter_grade = "D"
    output = 1
elif grade_percent <= 63.99 and grade_percent >= 60.00:
    letter_grade = "D-"
    output = 1
elif grade_percent <= 59.99 and grade_percent >= 0.00:
    letter_grade = "F"
    output = 1
else:
    output = 0

# Final output
if output == 1:
    final_output = f"Your grade in Programming class is {grade_percent}% and the letter for this is {letter_grade}"
elif output == 0:
    final_output = "How do you have a negitive percentage grade? Please do this again."
else:
    final_output = "How in the world was this triggered? What did you do to my code?????? THIS SHOULD NOT BE POSSIBLE!"


for char in final_output:
    print(char, end="", flush=True)
    time.sleep(delay)