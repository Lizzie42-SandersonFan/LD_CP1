# LD 2nd Caeser Cipher Practice

# Any variables eventually needed. Messsage and shift value
message = ""
shift_value = 0

# Functions
# Funtion that will encode using the message and shift value. use the ord() function to get each cahracter's value then add the shift value. Use chr() to get the new letter replacement, build all results into a string then RETURN final value
# Uppercase is 65-90
# Lowercase is 97-122
def encode(msg, shift):
    values = []
    new_message = ""
    for char in msg:
        x = ord(char) + shift
        # To deal with spaces, check to see if it was origanally a space and kepp if that
        if x > 90 and (char.isupper() == True):
            x -= 26
        elif x > 122 and (char.islower() == True):
            x -= 26
        else:
            pass # passing because I don't know what could go in here and x's new value is established
        values.append(x)
    for value in values:
        y = chr(value)
        new_message += y
    return new_message


# Funtion that will decode using the message and shift value. use the chr() function to get each cahracter's value then subrtact the shift value.Use chr() to get the new letter replacement (should be the original message), build all results into a string then RETURN final value
def decode(msg, shift):
    values = []
    og_message = ""
    for char in msg:
        x = ord(char) - shift
        if x > 90 and (char.isupper() == True):
            x -= 26
        elif x > 122 and (char.islower() == True):
            x -= 26
        else:
            pass # passing because I don't know what could go in here and x's new value is established
        values.append(x)
    for value in values:
        y = chr(value)
        og_message += y
    return og_message

# Begin code
# Use input() to get the stuff listed above, then ask the user if they want to encode or decode. Call corresponding function based on choice.
while True:
    choice = int(input("\nWould you like to\n1) ENCODE a message\n2) DECODE a message\n3) EXIT\n(Enter corrisponding number to choice):\n"))
    if choice == 1:
        print("\nType in a message you would like to ENCODE:")
        message = input()
        print("\nType in the shift value you want to use:")
        shift_value = int(input())
        encoded = encode(message, shift_value)
        print(f"The encoded message is {encoded}\n")
    elif choice == 2:
        print("\nType in the message you would like to DECODE:")
        message = input()
        print("\nType in the shift value you want to use:")
        shift_value = int(input())
        decoded = decode(message, shift_value)
        print(f"The decoded message is {decoded}\n")
    elif choice == 3:
        print("\nThank you! Have a good day!")
        break
    else:
        print("That is not a valid input. Try again")
        continue
