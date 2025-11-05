# LD 2nd Maze Generator
import turtle
import random

# I want each row/column to be 30 pixels
# Establish the turtle for drawing
pen = turtle.Turtle()
pen.hideturtle()

# Function to check if maze is solvable
def isSolvable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = []
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size - 1:
            return True
        
        if (x, y) in visited:
            continue

        visited.append((x, y))
        # If row below me is there
        if x <= size - 1 and col_grid[y][x-1] == 0:
            stack.append((x-1, y))

        # If column to left is there
        if y <= size - 1 and row_grid[x][y-1] == 0:
            stack.append((x, y-1))

        # If row above is there
        if x >= 0 and col_grid[x][y] == 0:
            stack.append((x, y+1))

        # If column to right is there
        if y >= 0 and row_grid[x][y] == 0:
            stack.append((x+1, y))
    return False

# While loop to keep generating the random maze until one is solvable, then show the solvable maze
while True:
    # Set up grid, this is two lists. one for rows and other for columns
    # Randomly generate maze from lists
    rows = [
        [0, 1, 1, 1, 1, 1], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [1, 1, 1, 1, 1, 0]
    ]
    columns = [
        [1, 1, 1, 1, 1, 1], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)], [1, 1, 1, 1, 1, 1]
    ]
    
    # Use function to check if the generated maze is solvable; if it is, show maze. If not, go back and re-randamize the maze
    if isSolvable(rows, columns) == True:
        # For loop to draw the maze itself. For item in maze, then for border in item: draw. If border is true(1), then pendown and draw then penup for every item. False(0) dont draw
        for row in rows:
            for section in row:
                if section == 0:
                    pen.penup()
                    pen.forward(30)
                else:
                    pen.pendown()
                    pen.forward(30)
            pen.penup()
            pen.setpos(0, pen.ycor()-30)
            pen.pendown()
        
        # Reset turtle for columns
        pen.penup()
        pen.setpos(0,0)
        pen.right(90)
        for column in columns:
            for wall in column:
                if wall == 0:
                    pen.penup()
                    pen.forward(30)
                else:
                    pen.pendown()
                    pen.forward(30)
            pen.penup()
            pen.setpos(pen.xcor()+30, 0)
            pen.pendown()
        turtle.done()
        break
    else:
        continue
