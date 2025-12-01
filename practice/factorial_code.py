# LD 2nd Factorial based on Elbow Partner's pseudocode

#num_list = []
num_list = []

# Define factorial(number, num_list):
#append number to num_list
# while num_list >1:
# factored_number = number - 1
# factored_number append to num_list

#define print_factoral(number, factored_number, num_list):
# multiply all numbers in num_list and save as factored number

def factorial(number):
    num_list.append(number)
    while number > 1:
        number -= 1
        num_list.append(number)


def print_factorial():
    factored_number = 1
    for num in num_list:
        factored_number *= num
    return factored_number

# while true:
# num = input("Enter a whole factorable number:")
# if num.isdiget == True:
# factoral(num, num_list)
# elif num.isdiget() == False:
# display: Invalid input, please retry with a whole number
# contiue
while True:
    user_num = input("Enter a whole, factorable number:\n")
    if user_num.isnumeric() == True:
        num = int(user_num)
        factorial(num)
        break
    else:
        print("Invalid input, please retry with a whole number")
        continue

factored_num = print_factorial()
print(f"{num} factored is {factored_num}")

# LD notes:
# need to break in while loop
# print funtion doesn't need factor_number parameter
# factoral function doesn't need paramters
# in factorial funtion, do not need to compare list, but the number, and also just do number and not all this factored_num thing
# input needs to be a string, then check if it is numeric then convert to int
# line 17: cannot have >=, just >