import turtle
from random import randint

myPen = turtle.Turtle()
turtle.tracer(0)
myPen.speed(0)
myPen.hideturtle()


def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)


# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)


##Here is an example of how to draw a box	
# box(boxSize)


##Here are some instructions on how to move "myPen" around before drawing a box.
# myPen.setheading(0) #point to the right, 90 to go up, 180 to go to the left 270 to go down
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()

# Here is how your PixelArt is stored (using a "list of lists")
palette = ["#FFFFFF", "#000000", "#00ff00", "#ff00ff", "#AAAAAA"]
maze = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
maze.append([1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1])
maze.append([1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])
maze.append([1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1])
maze.append([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1])
maze.append([1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1])
maze.append([1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1])
maze.append([1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1])
maze.append([1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1])
maze.append([1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1])
maze.append([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1])
maze.append([1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1])
maze.append([1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1])
maze.append([1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
maze.append([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2])
maze.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


def drawMaze(maze):
    boxSize = 15
    # Position myPen in top left area of the screen
    myPen.penup()
    myPen.goto(-130, 130)
    myPen.setheading(0)
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            myPen.color(palette[maze[i][j]])
            box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180)
        myPen.forward(boxSize * len(maze[i]))
        myPen.setheading(0)
        myPen.pendown()


# A backtracking/recursive function to check all possible paths until the exit is found
def exploreMaze(maze, row, col):
    if maze[row][col] == 2:
        # We found the exit
        return True
    elif maze[row][col] == 0:  # Empty path, not explored
        maze[row][col] = 3
        myPen.clear()
        drawMaze(maze)
        myPen.getscreen().update()
        if row < len(maze) - 1:
            # Explore path below
            if exploreMaze(maze, row + 1, col):
                return True
        if row > 0:
            # Explore path above
            if exploreMaze(maze, row - 1, col):
                return True
        if col < len(maze[row]) - 1:
            # Explore path to the right
            if exploreMaze(maze, row, col + 1):
                return True
        if col > 0:
            # Explore path to the left
            if exploreMaze(maze, row, col - 1):
                return True
        # Backtrack
        maze[row][col] = 4
        myPen.clear()
        drawMaze(maze)
        myPen.getscreen().update()

        print("Backtrack")


drawMaze(maze)
myPen.getscreen().update()

solved = exploreMaze(maze, 0, 1)
if solved:
    print("Maze Solved")
    text("Maze Solved", -100, -150, 20)
else:
    print("Cannot Solve Maze")
    text("Cannot Solve Maze", -130, -150, 20)

myPen.getscreen().update()	
