import math as mth
import random as r
import time as t
from tkinter import *


# Algorithm
def get_char(row, column):
    return file_list[row][column]


def find_char(element):
    for x in range(len(file_list)):

        for y in range(len(file_list[x])):

            if get_char(x, y) == element:
                return [x, y]


def check_path(row, column, text):
    try:
        if get_char(row, column) == " ":
            x = "path"
        elif (get_char(row, column) == "B"):
            x = "end"
        else:
            x = "no_way"

        if x == "path":

            yy = "yes"
            for z in range(len(explored)):
                if row == explored[z][0] and column == explored[z][1]:
                    yy = "no"
        elif x == "end":
            yy = "solve"
        else:
            yy = "no"
    except:
        yy = "no"
    if (yy == "yes"):

        frontier.append([row, column, text])
        explored.append([row, column, text])

    elif (yy == "solve"):
        global solution_steps
        solution_steps = text

        global terminate
        terminate = TRUE


# Start
def start():
    # Variable Setting
    global start_time
    start_time = t.time()

    global file
    file = open("maze", "r")

    global file_list
    file_list = file.readlines()

    global starting_point
    starting_point = find_char("A")

    starting_point.append([find_char("A")])

    global ending_point
    ending_point = find_char("B")
    ending_point.append([find_char("B")])

    global method
    method = options.index(clicked.get()) + 1

    global frontier
    frontier = [starting_point]

    global explored
    explored = []

    global terminate
    terminate = FALSE

    # Solve Window
    def solve():
        solution = Tk()
        solution.title("Solution")
        mst_column = len(file_list)
        most_row = []

        for zzz in range(len(file_list)):
            most_row.append(len(file_list[zzz]) - 1)

        mst_row = max(most_row)

        if mst_row > mst_column:
            geometry = mth.floor(675 / mst_row)
        else:
            geometry = mth.floor(675 / mst_column)

        solution.geometry(str(geometry * mst_row) + "x" +
                          str(geometry * mst_column + 200))
        solution.configure(background="#252525")
        solution.iconbitmap('logo.ico')
        solved = False
        for xxxx in range(len(file_list)):

            for yyyy in range(len(file_list[xxxx])):
                if file_list[xxxx][yyyy] == "A":
                    grid = Frame(solution, height=geometry,
                                 width=geometry, bg="green")

                    grid.place(x=yyyy * geometry, y=xxxx * geometry)
                    aaa = Label(grid, text="A", font=(
                        "Times New Roman", round(geometry / 1.35), "bold"))
                    aaa.pack()
                elif file_list[xxxx][yyyy] == "B":
                    grid = Frame(solution, height=geometry, width=geometry)
                    grid.place(x=yyyy * geometry, y=xxxx * geometry)
                    bbb = Label(grid, text="B", font=(
                        "Times New Roman", round(geometry / 1.35), "bold"))
                    bbb.pack()

                if file_list[xxxx][yyyy] == "A" or file_list[xxxx][yyyy] == "B":
                    continue

                elif file_list[xxxx][yyyy] == " ":
                    grid = Frame(solution, height=geometry,
                                 width=geometry, bg="black")
                    grid.place(x=yyyy * geometry, y=xxxx * geometry)

                else:
                    grid = Frame(solution, height=geometry,
                                 width=geometry, bg="red")
                    grid.place(x=yyyy * geometry, y=xxxx * geometry)

                if "solution_steps" in globals():
                    if [xxxx, yyyy] in solution_steps:
                        grid = Frame(solution, height=geometry,
                                     width=geometry, bg="green")
                        grid.place(x=yyyy * geometry, y=xxxx * geometry)
                    solved = True

        if solved == True:
            steps_taken = Label(
                solution,
                text="Steps taken in Solution: " + str(len(solution_steps)),
                font=("Times New Roman", 25, "bold"),
                background="#252525",
                fg="white",
                anchor="center",
                cursor="crosshair"

            )

            steps_taken.place(x=5, y=geometry * mst_column)

            time_taken = Label(
                solution,
                text="Time Taken: " +
                     str(round((t.time() - start_time)
                         * 10000) / 10000) + " Seconds",
                font=("Times New Roman", 25, "bold"),
                background="#252525",
                fg="white",
                anchor="center",
                cursor="crosshair"

            )

            time_taken.place(x=5, y=geometry * mst_column + 50)

            score = Label(
                solution,
                text="Program Pressure Score: " +
                     str((10000 - (len(explored))) / 100) + "/100",
                font=("Times New Roman", 25, "bold"),
                background="#252525",
                fg="white",
                anchor="center",
                cursor="crosshair"

            )

            score.place(x=5, y=geometry * mst_column + 100)
        else:
            result = Label(
                solution,
                text="Maze cannot be Solved",
                font=("Times New Roman", 25, "bold"),
                background="#252525",
                fg="white",
                anchor="center",
                cursor="crosshair"

            )

            result.place(x=5, y=geometry * mst_column)

    while (True):
        if terminate == TRUE:
            solve()
            break
        elif not frontier:

            terminate = TRUE

        elif method == 1:

            down = [frontier[0][0] + 1, frontier[0][1], frontier[0]
                    [2] + [[frontier[0][0] + 1, frontier[0][1]]]]
            up = [frontier[0][0] - 1, frontier[0][1], frontier[0]
                  [2] + [[frontier[0][0] - 1, frontier[0][1]]]]
            right = [frontier[0][0], frontier[0][1] + 1, frontier[0]
                     [2] + [[frontier[0][0], frontier[0][1] + 1]]]
            left = [frontier[0][0], frontier[0][1] - 1, frontier[0]
                    [2] + [[frontier[0][0], frontier[0][1] - 1]]]

            frontier.pop(0)
            check_path(down[0], down[1], down[2])
            check_path(up[0], up[1], up[2])
            check_path(right[0], right[1], right[2])
            check_path(left[0], left[1], left[2])

        else:

            down = [frontier[-1][0] + 1, frontier[-1][1], frontier[-1]
                    [2] + [[frontier[-1][0] + 1, frontier[-1][1]]]]
            up = [frontier[-1][0] - 1, frontier[-1][1], frontier[-1]
                  [2] + [[frontier[-1][0] - 1, frontier[-1][1]]]]
            right = [frontier[-1][0], frontier[-1][1] + 1, frontier[-1]
                     [2] + [[frontier[-1][0], frontier[-1][1] + 1]]]
            left = [frontier[-1][0], frontier[-1][1] - 1, frontier[-1]
                    [2] + [[frontier[-1][0], frontier[-1][1] - 1]]]
            frontier.pop(-1)

            variabless = [up, left, down, right]

            for zx in range(r.randint(0, 4)):
                r.shuffle(variabless)

            for zx in range(4):
                check_path(variabless[0][0], variabless[0]
                           [1], variabless[0][2])
                variabless.pop(0)


# Windows Preparations:
maze = Tk()
maze.title("Maze Solver")
maze.geometry("300x300")
maze.configure(background="#252525")
maze.iconbitmap('logo.ico')

# Title

title = Label(
    maze,
    text="Maze Solver",
    font=("Times New Roman", 30, "bold"),
    background="#252525",
    fg="white",
    anchor="center",
    cursor="crosshair"

)

title.place(x=40, y=20)

# Dropdown
options = [
    "Breadth First Search",
    "Depth First Search"

]

clicked = StringVar()

clicked.set("Breadth First Search")

drop = OptionMenu(maze, clicked, *options)
drop.configure(bg="black", fg="white", font=("Times New Roman", 13, "bold"))
drop["menu"].config(bg="black", fg="white", font=("arial", 10, "bold"))
drop.place(x=50, y=100)

# Button
solve = Button(
    maze,
    activebackground="#808080",
    activeforeground="#F5F5F5",
    bd=7.5,
    bg="#F5F5F5",
    fg="#252525",
    text="Solve Maze",
    font=('Times New Roman', 18, 'bold'),
    relief="ridge",
    padx=15,
    pady=2.5,
    cursor="circle",
    command=start

)

solve.place(x=65, y=160)

# Close Window
maze.mainloop()
