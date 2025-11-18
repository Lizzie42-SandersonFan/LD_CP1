# LD 2nd Flexible Calculator
import statistics

# Build function for math
def math(*nums):
    total = 0
    if opp_choice == "sum":
        # loop thru nums list and add them together
        if isinstance(users_nums, list):
            for num in users_nums:
                total += num
            return total
    elif opp_choice == "average":
        # loop thru list and find average
        if isinstance(users_nums, list):
            total = statistics.mean(users_nums)
            return total
    elif opp_choice == "max":
        # loop thru list and find bigest num
        if isinstance(users_nums, list):
            total = max(users_nums)
            return total
    elif opp_choice == "min":
        # loop thru list and find smallest num
        if isinstance(users_nums, list):
            total = min(users_nums)
            return total
    elif opp_choice == "product":
        # loop thru list and multiply them all together
        if isinstance(users_nums, list):
            for num in users_nums:
                total *= num
            return total
    else:
        # Something went wrong
        return "What happened?"

# Big while loop for running game
print("Welcom to FlexCalc where you can preform five different calculations of any numbers of your choosing!")
while True:
    users_nums = []
    # While loop for gettign user's operation choice
    while True:
        print("\nOpperations you can do: sum, average, max, min, and product")
        opp_choice = input("Which would you like to do:\n").strip().lower()
        if opp_choice == "sum":
            print("Sum picked!")
            break
        elif opp_choice == "average":
            print("Average picked!")
            break
        elif opp_choice == "max":
            print("Max picked!")
            break
        elif opp_choice == "min":
            print("Min picked!")
            break
        elif opp_choice == "product":
            print("Product picked!")
            break
        else:
            print("Invalid. Check your spelling and try again")
            continue

    # While loop for getting list of numbers
    print("Great, lets get your numbers")
    print("Enter your numbers (type 'done' when you're done)")
    while True:
        user_choice = input("Number: ")
        if user_choice == "done":
            break
        else:
            number = int(user_choice)
            users_nums.append(number)
            continue
    
    print(f"Calculating {opp_choice} of:")
    for x in users_nums:
        print(x)
    # Finally calling function
    result = math(users_nums)
    print(f"Result: {result}")

    # Asking the user if they want to do it again
    again = input("Would you like to do another calculation (yes/no)?\n").strip().lower()
    if again == "yes":
        continue
    else:
        break

# When user is done, thank them
print("Good bye! Thank you for using FlexCalc!")