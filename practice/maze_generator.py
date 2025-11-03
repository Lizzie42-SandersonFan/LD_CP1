# LD 2nd Maze Generator
import turtle
import random

# I want each row/column to be 25 pixels
# Set up grid, this is two lists. one for rows and other for columns
pen = turtle.Turtle()
pen.hideturtle()

rows = [
    [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)]
]
columns = [
    [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)], [random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2), random.randint(0,2)]
]

# Randomly generate maze from lists

# Function to check if maze is solvable
def isSolvable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size - 1:
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[y][x+1] == 0:
            stack.append((x+1, y))

        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.append((x, y+1))

        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1, y))

        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y-1))

    return False

# For loop to draw the maze itself. For item in maze, then for border in item: draw. If border is true(1), then pendown and draw then penup for every item. False(0) dont draw
# Set possition for drawing rows \/
pen.penup()
pen.setpos(-90, 90)
pen.pendown()

for row in rows:
    for section in row:
        if section == 0:
            pen.penup()
            pen.forward(30)
        else:
            pen.pendown()
            pen.forward(30)
            pen.penup()

# Set possition for drawing columns \/
pen.penup()
pen.right(90)
pen.setpos(-90, 90)
pen.pendown()

for column in columns:
    for wall in column:
        if wall == 0:
            pen.penup()
            pen.forward(30)
        else:
            pen.pendown()
            pen.forward(30)
            pen.penup()

# true_maze = isSolvable(rows, columns)
# print(true_maze)

turtle.done()