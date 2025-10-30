# LD 2nd Race Turtles
# Import libraries
import random
import turtle

# Set up visuals first:
t1_name = "Red Turtle"
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("#EE0303")
t1.penup()
t1.setpos(-200, 200)
t1.pendown()

t2_name = "Orange Turtle"
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("#EE7503")
t2.penup()
t2.setpos(-200, 100)
t2.pendown()

t3_name = "Yellow Turtle"
t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("#E6BB00")
t3.penup()
t3.setpos(-200, 0)
t3.pendown()

t4_name = "Green Turtle"
t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("#007510")
t4.penup()
t4.setpos(-200, -100)
t4.pendown()

t5_name = "Blue Turtle"
t5 = turtle.Turtle()
t5.shape("turtle")
t5.color("#0371EE")
t5.penup()
t5.setpos(-200, -200)
t5.pendown()

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.setpos(300, 300) # 300 is the minimum for a turtle to reach to win
finish_line.pendown()
finish_line.right(90)
finish_line.forward(600)

# Functions
def isWinner():
    if t1.xcor() >= 300:
        return True
    elif t2.xcor() >= 300:
        return True
    elif t3.xcor() >= 300:
        return True
    elif t4.xcor() >= 300:
        return True
    elif t5.xcor() >= 300:
        return True
    else:
        return False
    
# Do python code part:
# Make turtles move
# Check for when a turtle crosses the finish line
# if a turtle does, stop the game and show which turtle color won the race
while True:
    t1.forward(random.randint(1, 75))
    winner = isWinner()
    if winner == True:
        turtle.write("Red Turtle Won!!!", True, align = "right", font=("Arial", 35, "normal"))
        break
    t2.forward(random.randint(1, 75))
    winner = isWinner()
    if winner == True:
        turtle.write("Orange Turtle Won!!!", True, align = "right", font=("Arial", 35, "normal"))
        break
    t3.forward(random.randint(1, 75))
    winner = isWinner()
    if winner == True:
        turtle.write("Yellow Turtle Won!!!", True, align = "right", font=("Arial", 35, "normal"))
        break
    t4.forward(random.randint(1, 75))
    winner = isWinner()
    if winner == True:
        turtle.write("Green Turtle Won!!!", True, align = "right", font=("Arial", 35, "normal"))
        break
    t5.forward(random.randint(1, 75))
    winner = isWinner()
    if winner == True:
        turtle.write("Blue Turtle Won!!!", True, align = "right", font=("Arial", 35, "normal"))
        break
turtle.done()