# LD 2nd Race Turtles
# Import libraries
import random
import turtle

# Set up visuals first:
# turtle speed range: 1 to 10. 10 being fastest and 1 being slowest
t1_name = "Red Turtle"
t1 = turtle.Turtle()
t1.penup()
t1.setpos(-200, 200)
t1.pendown()
t1.shape("turtle")
t1.color("#EE0303")

t2_name = "Orange Turtle"
t2 = turtle.Turtle()
t2.penup()
t2.setpos(-200, 100)
t2.pendown()
t2.shape("turtle")
t2.color("#EE7503")

t3_name = "Yellow Turtle"
t3 = turtle.Turtle()
t3.penup()
t3.setpos(-200, 0)
t3.pendown()
t3.shape("turtle")
t3.color("#E6BB00")

t4_name = "Green Turtle"
t4 = turtle.Turtle()
t4.penup()
t4.setpos(-200, -100)
t4.pendown()
t4.shape("turtle")
t4.color("#007510")

t5_name = "Blue Turtle"
t5 = turtle.Turtle()
t5.penup()
t5.setpos(-200, -200)
t5.pendown()
t5.shape("turtle")
t5.color("#0371EE")

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.setpos(300, 300) # 300 is the minimum for a turtle to reach to win
finish_line.pendown()
finish_line.right(90)
finish_line.forward(600)

def isWinner():
    if t1.xcor() >= 300:
        return True, "Red"
    elif t2.xcor() >= 300:
        return True, "Orange"
    elif t3.xcor() >= 300:
        return True, "Yellow"
    elif t4.xcor() >= 300:
        return True, "Green"
    elif t5.xcor() >= 300:
        return True, "Blue"
    else:
        return False
# Do python code part:
# Make turtles move
# Check for when a turtle crosses the finish line
# if a turtle does, stop the game and show which turtle color won the race
while True:
    t1.forward(random.randint(1, 75))
    if t1.xcor() >= 300:
        print("Red Turtle Won!!")
        break
    elif t2.xcor() >= 300:
        print("Orange Turtle Won!!")
        break
    elif t3.xcor() >= 300:
        print("Yellow Turtle Won!!")
        break
    elif t4.xcor() >= 300:
        print("Green Turtle Won!!")
        break
    elif t5.xcor() >= 300:
        print("Blue Turtle Won!!")
        break
    t2.forward(random.randint(1, 75))
    if t1.xcor() >= 300:
        print("Red Turtle Won!!")
        break
    elif t2.xcor() >= 300:
        print("Orange Turtle Won!!")
        break
    elif t3.xcor() >= 300:
        print("Yellow Turtle Won!!")
        break
    elif t4.xcor() >= 300:
        print("Green Turtle Won!!")
        break
    elif t5.xcor() >= 300:
        print("Blue Turtle Won!!")
        break
    t3.forward(random.randint(1, 75))
    if t1.xcor() >= 300:
        print("Red Turtle Won!!")
        break
    elif t2.xcor() >= 300:
        print("Orange Turtle Won!!")
        break
    elif t3.xcor() >= 300:
        print("Yellow Turtle Won!!")
        break
    elif t4.xcor() >= 300:
        print("Green Turtle Won!!")
        break
    elif t5.xcor() >= 300:
        print("Blue Turtle Won!!")
        break
    t4.forward(random.randint(1, 75))
    if t1.xcor() >= 300:
        print("Red Turtle Won!!")
        break
    elif t2.xcor() >= 300:
        print("Orange Turtle Won!!")
        break
    elif t3.xcor() >= 300:
        print("Yellow Turtle Won!!")
        break
    elif t4.xcor() >= 300:
        print("Green Turtle Won!!")
        break
    elif t5.xcor() >= 300:
        print("Blue Turtle Won!!")
        break
    t5.forward(random.randint(1, 75))
    if t1.xcor() >= 300:
        print("Red Turtle Won!!")
        break
    elif t2.xcor() >= 300:
        print("Orange Turtle Won!!")
        break
    elif t3.xcor() >= 300:
        print("Yellow Turtle Won!!")
        break
    elif t4.xcor() >= 300:
        print("Green Turtle Won!!")
        break
    elif t5.xcor() >= 300:
        print("Blue Turtle Won!!")
        break
