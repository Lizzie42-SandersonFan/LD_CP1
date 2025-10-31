# LD 2nd Maze Generator
import turtle

# I need to draw my maze out for my own sanity's sake
# I want each row/column to be 75 pixels
# Start with setting up the maze grid as a list with lists inside for rows/columns
maze = [["This is row one"], ["This is row two"], ["This is row three"], ["This is row four"], ["This is row five"], ["This is row six"]]

# Make the turtle draw the boarder first
# For loop to draw the maze itself. For item in maze, then for border in item: draw. If border is true, then pendown and draw then penup for every item

border_turtle = turtle.Turtle()
border_turtle.hideturtle() # DO THIS WHEN DRAWING
border_turtle.penup()
border_turtle.goto(-200, 200)
border_turtle.pendown()
# Drawing the maze border
border_turtle.forward(200)
border_turtle.penup()
border_turtle.forward(75)
border_turtle.pendown()
border_turtle.forward(200)
border_turtle.right(90)
border_turtle.forward(450)
border_turtle.right(90)
border_turtle.forward(200)
border_turtle.penup()
border_turtle.forward(75)
border_turtle.pendown()
border_turtle.forward(200)
border_turtle.right(90)
border_turtle.forward(450)
# /\ this is ugly, I know :(

turtle.done()