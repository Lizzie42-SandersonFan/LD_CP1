# LD 2nd Caeser Cipher Practice

# Any variables eventually needed. Messsage and shift value
message = ""
shift_value = 0
lower_a = 97
lower_z = 122
upper_A = 65
upper_Z = 90

# Functions
# Funtion that will encode using the message and shift value. use the ord() function to get each cahracter's value then add the shift value. Use chr() to get the new letter replacement, build all results into a string then RETURN final value
# Uppercase is 65-90
# Lowercase is 97-122
def encode(msg, shift):
    shift = shift % 26
    new_message = ""
    for char in msg:
        if ord(char) >= lower_a and ord(char) <= lower_z:
            # 1 add the shift
            shifted_letter = ord(char) + shift
            # 2 make sure it stays lowercase
            if shifted_letter < lower_a:
                shifted_letter += 26
            elif shifted_letter > lower_z:
                shifted_letter -= 26
            else:
                pass # It's already in the right spot
            # 3 put it into the final string
            new_message += chr(shifted_letter)
        elif ord(char) >= upper_A and ord(char) <= upper_Z:
            # 1 add the shift
            shifted_letter = ord(char) + shift
            # 2 make sure it stays uppercase
            if shifted_letter < upper_A:
                shifted_letter += 26
            elif shifted_letter > upper_Z:
                shifted_letter -= 26
            else:
                pass # It's already in the right spot
            #3 put it into the final string
            new_message += chr(shifted_letter)
        else:
            # put into final string
            new_message += char
    return new_message


# Funtion that will decode using the message and shift value. Encode but backwards.
def decode(msg, shift):
    return encode(msg, 26-shift)

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
