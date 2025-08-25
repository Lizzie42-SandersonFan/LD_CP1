# Final project, River Stanley, Lila Shearer, Chiara Negron Wilson, Lizzie Delong

import time
delay = 0.04

#Chiara variables
cakeFlavor=1
frostingFlavor=2

#River varables
cakepan=1
cakeStat= 2
ovenTemp = 0

#Lizzie variables
frostPiped=1
allToppings = ["sprinkles", "strawberries", "fudge sauce"]
isSprinkles = False
isStrawberries = False
isFudge = False
notoppings = 0
toppings = 0

#Lila variables
response = 0
explanationMessage = 0
customerAnswer = 0
userNotTrying = 0
certificate = 0

#welcome banner, intro 
welcome = "\nWelcome to Baking Simulator!\nIn this game you will get to bake a cake and have a critic try it.\nThe critic will give feedback based on your cake.\nYour goal is to have the critic love your cake!\n"
important = "IMPORTANT NOTE:\nWhen answering questions, answer with the number of the option you want,\nUNLESS a different answering method is specified.\n:)\n"
warning = "Also, if you choose to not play the game correctly, something bad will happen...\n"

for char in welcome:
    print(char, end="", flush=True)
    time.sleep(delay)
for char in important:
    print(char, end="", flush=True)
    time.sleep(delay)
for char in warning:
    print(char, end="", flush=True)
    time.sleep(delay)

#Chiara What kind of cake? EX: vanilla, chocolate, carrot 
# 1 = vanilla, 2 = choco, 3 = carrot cake
flavor = input("\nWhat kind of cake would you like to make?\n (1 a vanilla cake\n (2 a chocolate cake\n (3 A carrot cake\n")

if flavor == "1":
    cakeFlavor=1
elif flavor == "2":
    cakeFlavor = 2
elif flavor=="3":
    cakeFlavor=3
else:    
    print("We don't have the ingredients to make that type of cake.\n")
    userNotTrying = 1

#Chiara what kind of frostingFlavor EX: Buttercream, cream cheese, swiss meringue
# 1 = buttercream, 2 = cream cheese, 3 = swiss meringue
frosttype= input("\nWhat type of frosting do you want on your cake?\n (1 A buttercream frosting\n (2 A cream cheese frosting\n (3 A swiss meringue frosting\n")

if frosttype== "1":
    frostingFlavor=1
elif frosttype== "2":
    frostingFlavor=2
elif  frosttype=="3":
    frostingFlavor=3
else:  
    print("We don't have this type of frosting in stock.\n")
    userNotTrying = 1


#River Cake pans circle, square, cupcakes 
#Has user pick a kind of cake
# 1 = circle, 2 = square, 3 = cupcakes  
shape=input("\nWhat kind of cake will you bake?\n (1 A circle cake\n (2 a square cake\n (3 multi tier cake\n")

if shape=="1":
    cakepan=1
elif shape=="2":
    cakepan=2
elif shape=="3":
    cakepan=3
else:
    print("We don't have that kind of cakepan\n")   
    userNotTrying = 1
 

#River temperature EX: 325-375 normal bake, under is underbaked, over by like 20 is overbaked any further is broken and on fire oven
# 1 = underbaked, 2 = perfect, 3 = overbaked
# make temp a conditional
# if checks if overbaked (majorly)

# temp a conditional
# checks the how the cake is cooked by what temp the user puts in

temp=int(input("\nWhat temperature will you set the oven to in fahrenheit(NUMBER PLEASE)?\n"))   
if temp>=350 and temp<=375: 
    temp=2
    cakeStat = 2
    print("Your cake is perfect!")
elif temp<349 and temp > 300:
     temp = 1
     cakeStat = 1
     print("Your cake is a little undercooked but it will work\n")
elif temp>376 and temp<=420:
     temp=3
     cakeStat = 3
     print("Your cake is a little overcooked but it will work\n")  
elif temp<=300:
     print("Your cake is still batter and the customer is furious. Game over. :(")  
     exit()
else:
     print("The oven has lit on fire and burned down the bakery, game over. :(")
     exit()


#Lizzie frosting EX: pipped on, spooned on, none 
# 1 = piped, 2 = spooned, 3 = none
frostPiped = input("\nHow would you like to add the frosting:\n (1 Piped\n (2 Spooned on\n (3 No frosting\n")
if frostPiped == "1":
    frostPiped = 1
elif frostPiped == "2":
    frostPiped = 2
elif frostPiped == "3":
    frostPiped = 3
else:
    print("We are unable to apply the frosting that way.")
    frostPiped = 3
#Lizzie toppings EX: sprinkles, strawberries, fudge sauce
# use a loop to loop through all topping options
# use a funtion to print out all topping request statement
def toppingRequest(theTopping):
    global response
    response = input(f"\nWould you like {theTopping} (YES or NO)?\n").strip().upper()

for item in allToppings:
    toppingRequest(item)
    if item == "sprinkles":
        if response == "YES" or response == "YA" or response == "SURE" or response == "YEAH" or response == "YEE":
            isSprinkles = True
    if item == "strawberries":
        if response == "YES" or response == "YA" or response == "SURE" or response == "YEAH" or response == "YEE":
            isStrawberries = True
    if item == "fudge sauce":
        if response == "YES" or response == "YA" or response == "SURE" or response == "YEAH" or response == "YEE":
            isFudge = True
    
#Lila results EX: The customer loved your (size, flavor, topping) cake! The custom demanded a refund as their cake was over/under baked
# change type for each variable. Use if statement to replace number with what it is (ex: if cakeFlavor = 1 then change it to cakeFlavor = 'chocolate')
# Use function to print out The customer (love, liked, dislike, hated) your (size) (flavor) cake with (frostingFlavor type) frostingFlavor and (topping or no toppings)

#Lila - this part of my code sets the variable to be the choice the user made so that my print statement runs smoothly.
if frostingFlavor == 1:
    frostingFlavor = "buttercream"
elif frostingFlavor == 2:
    frostingFlavor = "cream cheese"
else:
    frostingFlavor = "swiss meringue"

if cakeFlavor == 1:
    cakeFlavor = "vanilla"
elif cakeFlavor == 2:
    cakeFlavor = "chocolate"
else:
    cakeFlavor = "carrot"

if cakepan == 1:
    cakepan = "circle"
elif cakepan == 2:
    cakepan = "square"
else:
    cakepan = "multi-tiered"

if frostPiped == 1:
    frostPiped = "very nice looking"
elif frostPiped == 2:
    frostPiped = "decent looking"
else:
    frostPiped = "nonexistant"

#Lila - This part of my code sets the toppings variable in my print statement so that it prints correctly
if isSprinkles == True and isStrawberries == True and isFudge == True:
    toppings = " sprinkles, strawberries, and fudge"
elif isSprinkles == True and isStrawberries == True and isFudge == False:
    toppings = " sprinkles and strawberries"
elif isSprinkles == True and isStrawberries == False and isFudge == True:
    toppings = " sprinkles and fudge"
elif isSprinkles == False and isStrawberries == True and isFudge == True:
    toppings = " strawberries and fudge"
elif isSprinkles == True and isStrawberries == False and isFudge == False:
    toppings = " sprinkles"
elif isSprinkles == False and isStrawberries == True and isFudge == False:
    toppings = " strawberries"
elif isSprinkles == False and isStrawberries == False and isFudge == True:
    toppings = " fudge"
elif isSprinkles == False and isStrawberries == False and isFudge == False:
    toppings = " no toppings"
else:
    toppings = "How did you do this?"


#Lila - This part of my code decides how the critic will respond by looking at what decisions werre made
if userNotTrying == 1:
    customerAnswer = "was HORRIFIED and DISGUSTGED BY"
    explanationMessage = "\nYou tried to use ingredients we didn't have, resulting in:\nyour cake failing,\nyou eternally living in your mother's basement,\nyour partner never meeting or marrying you,\nyour entire future being ruined,\nand a curse placed on all of your family members.\nNext time, use the ingredients provided!\n♡\n"
elif frostPiped == "very nice looking" and cakeStat == 2 and toppings != " no toppings":
    customerAnswer = "LOVED"
    explanationMessage = "\nYour cake was perfect!\nYou won the game!\n"
    certificate = 1
elif frostPiped == "very nice looking" and cakeStat == 2 and toppings == " no toppings":
    customerAnswer = "enjoyed"
    explanationMessage = "Your cake was very good, but it was a little boring on the outside.\nYou were so close to winning!\n"
elif frostPiped == "nonexistant" and cakeStat == 2 or frostPiped == "nonexistant" and toppings != " no toppings":
    customerAnswer = "sort of enjoyed"
    explanationMessage = "Your cake was lacking in some areas."
elif frostPiped == "very nice looking" and cakeStat >=1:
    customerAnswer = "liked"
    explanationMessage = "A few things could be improved, but overall you did a pretty good job. Consider watching the oven more closely next time."
elif frostPiped == "decent looking" and cakeStat == 2:
    customerAnswer = "liked"
    explanationMessage = "A few things could be improved, but overall you did a pretty good job. Consider improving your method for putting frosting on the cake."
else:
    customerAnswer = "hated"
    explanationMessage = "Your cake was not very good. It was lacking in several areas and was not enjoyable."

#Lila - This part of my code is the response. It takes the user's choices and puts them into a print statement.
def customerResponse(feelingAboutCake,size,theFLAVOUR,howYouapplyit,frostFlavor,howManyToppings, whyBadOrGood):
    global theAnswer
    theAnswer = f'The critic {feelingAboutCake} your {size} {theFLAVOUR} cake with {howYouapplyit} {frostFlavor} frosting.\nYou added{howManyToppings}.\n{whyBadOrGood}'

if userNotTrying == 1:
    for char in explanationMessage:
        print(char, end="", flush=True)
        time.sleep(delay)

elif certificate == 1:
    present = "\nTime to present your creation!\n"
    for char in present:
        print(char, end="", flush=True)
        time.sleep(delay)

    customerResponse(customerAnswer, cakepan, cakeFlavor, frostPiped, frostingFlavor, toppings, explanationMessage)
    for char in theAnswer:
        print(char, end="", flush=True)
        time.sleep(delay)

    name = input("Please enter your first name to recieve your personalized certificate!\n").strip().capitalize()
    finalResult = f"\nCongradulations, {name}!!!\nYou won Baking Simulator!!!!!!\nYou made a marvelous {cakeFlavor} cake!!!!\n:D"
    for char in finalResult:
        print(char, end="", flush=True)
        time.sleep(delay)

else:
    present = "\nTime to present your creation!\n"
    for char in present:
        print(char, end="", flush=True)
        time.sleep(delay)

    customerResponse(customerAnswer, cakepan, cakeFlavor, frostPiped, frostingFlavor, toppings, explanationMessage)
    for char in theAnswer:
        print(char, end="", flush=True)
        time.sleep(delay)


#Lizzie - fun cake image
ending = "\nThank you for playing!\n"
endingCake = " @@@@@@@ \n |_____|\n@@@@@@@@@\n|_______|\n:D\n"

for char in ending:
    print(char, end="", flush=True)
    time.sleep(delay)
for char in endingCake:
    print(char, end="", flush=True)
    time.sleep(delay)