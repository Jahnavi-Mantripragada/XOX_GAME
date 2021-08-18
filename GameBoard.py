"""
This is code for XOX Game using tkinter.
"""
# The Import Section
from tkinter import *
from functools import partial

# The Constants
BACKGROUND = "bg"
TEXT = "text"
STATE = "state"
DISABLED_FOREGROUND = "disabledforeground"
FOREGROUND = "fg"
X, O = "X", "O"

curr_player = [X]
pressed = [0]

# The properties of the cell change on a press according to the player who pressed it.
players = {
    X: {DISABLED_FOREGROUND: "blue", BACKGROUND: "#87CEEB", STATE: DISABLED, TEXT: X},
    O: {DISABLED_FOREGROUND: "red", BACKGROUND: "#FFCCCB", STATE: DISABLED, TEXT: O}
}

# When we want to reset the board.
resetting = {
    FOREGROUND: "grey", BACKGROUND: "#C0C0C0", STATE: NORMAL, TEXT: ""
}


# Before we start a new Game.
def initialState():
    curr_player[0] = X
    pressed[0] = 0
    AnnouncementLabel["text"] = "X's Turn"


# Since this is a two-player game, and there would alternate chances.
def changePlayer():
    curr_player[0] = X if curr_player[0] == O else O


# Creating widgets: buttons! as a board.
def buildBoard():
    for i in range(3):
        rows = []
        for j in range(3):
            b = Button(f, text="", padx=40, pady=20, command=partial(move, i, j), bg="#C0C0C0", bd=10)
            b.grid(row=i + 1, column=j + 1)
            b.config(width=10, height=2)
            rows.append(b)
        board.append(rows)


# After a game ends (either a win or draw), we disable all the cells.
def disableAllCells():
    for i in range(3):
        for j in range(3):
            board[i][j][STATE] = DISABLED


# When we reset the board, or we are getting ready for a rematch.
def resetAllCells():
    initialState()
    reLabel["text"] = "Reset"
    for i in range(3):
        for j in range(3):
            for reset_options in resetting:
                board[i][j][reset_options] = resetting[reset_options]


# We keep checking the board after every turn, so, we can find if a player won.
def checkIfAPlayerWon(i, j):
    player = curr_player[0]
    # check the row
    for r in range(3):
        if board[r][j][TEXT] != player:
            break
    else:
        return True

    # check the column if current player won.
    for c in range(3):
        if board[i][c][TEXT] != player:
            break
    else:
        return True

    for r, c in zip(range(3), range(3)):
        if board[r][c][TEXT] != player:
            break
    else:
        return True

    for r, c in zip(range(3), range(2, -1, -1)):
        if board[r][c][TEXT] != player:
            break
    else:
        return True
    return False


# Move here is to imply each turn played.
def move(i, j):
    player = curr_player[0]
    pressed[0] += 1
    for values in players[player]:
        board[i][j][values] = players[player][values]
    if checkIfAPlayerWon(i, j):
        winLabel = "{} WINS!".format(curr_player[0])
        AnnouncementLabel["text"] = winLabel
        disableAllCells()
        rematch = "Rematch?"
        reLabel["text"] = rematch
    elif pressed[0] == 9:
        TieLabel = "That's a Draw!"
        AnnouncementLabel["text"] = TieLabel
        disableAllCells()
        rematch = "Rematch?"
        reLabel["text"] = rematch
    else:
        changePlayer()
        AnnouncementLabel["text"] = "{}'s Turn".format(curr_player[0])


# The Board:
board = []

# The Window:
root = Tk()
root.title("XOX GAME!")

# The Place where we display the verdict or tell its X's or O's Turn.
AnnouncementLabel = Label(root, padx=20)
AnnouncementLabel.pack()
AnnouncementLabel.config(font=('Helvetica bold', 20))

# Initialization for a new game.
initialState()

# This frame holds the cells of the board. (Buttons)
f = Frame(root, width=50, height=50)
buildBoard()
f.pack()

# We are using a frame to get the two buttons, reLabel, Quit side-by-side.
top = Frame(root)
top.pack(side=TOP)

reLabel = Button(root, text="Reset", padx=40, pady=20, command=resetAllCells, bg="#90EE90", bd=10)
Quit = Button(root, text="Quit", padx=40, pady=20, command=root.destroy, bg="#dc143c", bd=10)

reLabel.config(font=('Helvetica bold', 15))
Quit.config(font=('Helvetica bold', 15))

reLabel.pack(in_=top, side=LEFT)
Quit.pack(in_=top, side=LEFT)

root.resizable(False, False)
root.mainloop()
