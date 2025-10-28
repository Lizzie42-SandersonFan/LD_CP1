# LD 2nd Libraries & Build in Functions Notes
import random
import turtle
number = random.randint(100, 500)

turtle.shape("classic")
turtle.color("#78007C")
turtle.pensize(10)
turtle.fillcolor("blue")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.done() # Does not close the window whens its done