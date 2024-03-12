import turtle
import random
import tkinter as tk

myPen = turtle.Turtle()
turtle.tracer(0)
myPen.speed(0)
myPen.hideturtle()

# Additional window for inputting trivia answer
input_window = tk.Tk()
input_window.geometry("600x100")
input_window.title("Trivia Answer")

def close_input_window():
    input_window.destroy()

def submit_answer(validate_function):
    global trivia_answer
    trivia_answer = entry.get()
    close_input_window()
    validate_function()

def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)

def box(intDim):
    myPen.begin_fill()
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

def generateMaze(rows, columns):
    def creation(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < columns and 0 <= ny < rows and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0
                maze[ny][nx] = 0
                creation(nx, ny)

    horLimit = random.randint(2, rows-2)
    vertLimit = random.randint(2, columns-2)

    maze = [[1]* columns for _ in range(rows)]

    if maze[horLimit-1][vertLimit-1] == 1 and maze[horLimit-1][vertLimit-1] != horLimit and vertLimit:
        maze[horLimit-1][vertLimit] = 0
        maze[horLimit][vertLimit-1] = 0
    maze[horLimit][vertLimit] = 2

    creation(random.randrange(0, columns-1, 2), random.randrange(0, rows-1, 2))

    # Place a single trivia square
    triviaRow = random.randint(0, rows - 1)
    triviaCol = random.randint(0, columns - 1)
    while maze[triviaRow][triviaCol] != 0 or (triviaRow == horLimit and triviaCol == vertLimit):
        triviaRow = random.randint(0, rows - 1)
        triviaCol = random.randint(0, columns - 1)
    maze[triviaRow][triviaCol] = 5

    # Place a single portal
    portalRow = random.randint(0, rows - 1)
    portalCol = random.randint(0, columns - 1)
    while maze[portalRow][portalCol] != 0 or (portalRow == horLimit and portalCol == vertLimit):
        portalRow = random.randint(0, rows - 1)
        portalCol = random.randint(0, columns - 1)
    maze[portalRow][portalCol] = 6

    return maze

palette=["#5e5d5d","#000000","#cf2121","#42b9f5","#ffffff","#803896","#f73bd8"]
maze = generateMaze(25,25)

def drawMaze(maze):
    boxSize = 10
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

def exploreMaze(maze, row, col):
    global trivia_answer
    triviaPool = {
        1: "Cuantos metros hay en un centimetro?",
        2: "Cuanto porcentaje de agua hay en un cuerpo humano? (numero)",
        3: "Cuando es el dia de la constitución (DD/MM)?",
        4: "Cuantas veces da la vuelta al sol la tierra en un año?",
        5: "Cuantos años hay en un lustro?",
        6: "Si son las 5 pm que horas son en formato de 24hrs? (HH:MM)",
    }

    triviaAnswers = {
        1: "0.01",
        2: "70",
        3: "05/02",
        4: "1",
        5: "5",
        6: "17:00"
    }

    if maze[row][col] == 2:
        text("¡Llegaste! ¡Felicidades!", -100, -150, 20)
        myPen.getscreen().update()
        return True

    if maze[row][col] == 5:
        index = random.randint(1,len(triviaPool))
        question_text.config(text=triviaPool[index])
        entry = tk.Entry(input_window)
        entry.pack()
        submit_button = tk.Button(input_window, text="Submit", command=lambda: submit_answer(lambda: validate_trivia_answer(maze, row, col, index, triviaAnswers[index])))
        submit_button.pack()
        input_window.mainloop()
        return False

    if maze[row][col] == 6:
        # Teleport near the exit
        exit_row, exit_col = -1, -1
        for r in range(len(maze)):
            for c in range(len(maze[0])):
                if maze[r][c] == 2:
                    exit_row, exit_col = r, c
                    break
            if exit_row != -1:
                break
        
        # Teleport near the exit
        maze[row][col] = 0
        for _ in range(10):
            new_row = random.randint(max(0, exit_row - 5), min(len(maze)-1, exit_row + 5))
            new_col = random.randint(max(0, exit_col - 5), min(len(maze[0])-1, exit_col + 5))
            if maze[new_row][new_col] == 0:
                row, col = new_row, new_col
                break

    elif maze[row][col] == 0:
        maze[row][col] = 3
        myPen.clear()
        drawMaze(maze)
        myPen.getscreen().update()
        if row < len(maze) - 1:
            if exploreMaze(maze, row + 1, col):
                return True
        if row > 0:
            if exploreMaze(maze, row - 1, col):
                return True
        if col < len(maze[row]) - 1:
            if exploreMaze(maze, row, col + 1):
                return True
        if col > 0:
            if exploreMaze(maze, row, col - 1):
                return True

        maze[row][col] = 4
        myPen.clear()
        drawMaze(maze)
        myPen.getscreen().update()
        print("Backtrack")

def validate_trivia_answer(maze, row, col, index, correct_answer):
    global trivia_answer
    if trivia_answer == correct_answer:
        maze[row][col] = 0
        if row < len(maze) - 1:
            if exploreMaze(maze, row + 1, col):
                return True
        if row > 0:
            if exploreMaze(maze, row - 1, col):
                return True
        if col < len(maze[row]) - 1:
            if exploreMaze(maze, row, col + 1):
                return True
        if col > 0:
            if exploreMaze(maze, row, col - 1):
                return True
    else:
        text("Path Blocked!", -100, -150, 20)
        myPen.getscreen().update()
        return False

# Define question_text
question_text = tk.Label(input_window, text="")
question_text.pack()

drawMaze(maze)
myPen.getscreen().update()

solved = exploreMaze(maze, 0, 0)
if solved:
    print("Maze Solved")
    text("Maze Solved", -100, -150, 20)
else:
    print("Cannot Solve Maze")
    text("Cannot Solve Maze", -130, -150, 20)

myPen.getscreen().update()
