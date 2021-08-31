"""
This is code for XOX Game using tkinter.
"""
# The Import Section
from tkinter import *
from functools import partial
from tkinter import messagebox

# The Constants
BACKGROUND = "bg"
TEXT = "text"
STATE = "state"
DISABLED_FOREGROUND = "disabledforeground"
FOREGROUND = "fg"
X, O = "X", "O"


def messageBox(title, text):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, text)
    root.destroy()


class GameBoard(Tk):

    def __init__(self, player1="", player2=""):
        super().__init__()

        self.player1 = player1
        self.player2 = player2

        # This frame holds the cells of the board. (Buttons)
        self.f = Frame(self, width=50, height=50)
        # The Place where we display the verdict or tell its X's or O's Turn.
        self.AnnouncementLabel = Label(self, padx=20)
        self.title("XOX GAME!")
        self.curr_player = X
        self.pressed = 0
        # The Board:
        self.board = []
        # We are using a frame to get the two buttons, reLabel, Quit side-by-side.
        self.top = Frame(self)
        self.reLabel = Button(self.top, text="Reset", padx=40, pady=20, command=self.resetAllCells, bg="#90EE90", bd=10)
        self.Quit = Button(self.top, text="Quit", padx=40, pady=20, command=self.destroy, bg="#dc143c", bd=10)

        # The properties of the cell change on a press according to the player who pressed it.
        self.players = {
            X: {DISABLED_FOREGROUND: "blue", BACKGROUND: "#87CEEB", STATE: DISABLED, TEXT: X},
            O: {DISABLED_FOREGROUND: "red", BACKGROUND: "#FFCCCB", STATE: DISABLED, TEXT: O}
        }

        # When we want to reset the board.
        self.resetting = {
            FOREGROUND: "grey", BACKGROUND: "#C0C0C0", STATE: NORMAL, TEXT: ""
        }
        self.setWidgets()
        self.resizable(False, False)

    def getPlayerName(self):
        if self.curr_player == X:
            return self.player1
        return self.player2

    def setWidgets(self):
        self.AnnouncementLabel.pack()
        self.AnnouncementLabel.config(font=('Helvetica bold', 20))

        # Initialization for a new game.
        self.initialState()

        self.buildBoard()
        self.f.pack()

        self.top.pack(side=TOP)

        self.reLabel.config(font=('Helvetica bold', 15))
        self.Quit.config(font=('Helvetica bold', 15))

        self.reLabel.pack(in_=self.top, side=LEFT)
        self.Quit.pack(in_=self.top, side=LEFT)

    # Before we start a new Game.
    def initialState(self):
        self.curr_player = X
        self.pressed = 0
        self.AnnouncementLabel["text"] = "{}'s Turn".format(self.getPlayerName())

    # Creating widgets: buttons! as a board.
    def buildBoard(self):
        for i in range(3):
            rows = []
            for j in range(3):
                b = Button(self.f, text="", padx=40, pady=20, command=partial(self.move, i, j), bg="#C0C0C0")
                b.grid(row=i + 1, column=j + 1)
                b.config(width=10, height=2)
                rows.append(b)
            self.board.append(rows)

    # Since this is a two-player game, and there would alternate chances.
    def changePlayer(self):
        self.curr_player = X if self.curr_player == O else O

    # After a game ends (either a win or draw), we disable all the cells.
    def disableAllCells(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j][STATE] = DISABLED

    # When we reset the board, or we are getting ready for a rematch.
    def resetAllCells(self):
        self.initialState()
        self.reLabel["text"] = "Reset"
        for i in range(3):
            for j in range(3):
                for reset_options in self.resetting:
                    self.board[i][j][reset_options] = self.resetting[reset_options]

    # We keep checking the board after every turn, so, we can find if a player won.
    def checkIfAPlayerWon(self, i, j):
        player = self.curr_player
        # check the row
        for r in range(3):
            if self.board[r][j][TEXT] != player:
                break
        else:
            return True

        # check the column if current player won.
        for c in range(3):
            if self.board[i][c][TEXT] != player:
                break
        else:
            return True

        for r, c in zip(range(3), range(3)):
            if self.board[r][c][TEXT] != player:
                break
        else:
            return True

        for r, c in zip(range(3), range(2, -1, -1)):
            if self.board[r][c][TEXT] != player:
                break
        else:
            return True
        return False

    # Move here is to imply each turn played.
    def move(self, i, j):
        player = self.curr_player
        self.pressed += 1
        for values in self.players[player]:
            self.board[i][j][values] = self.players[player][values]
        if self.checkIfAPlayerWon(i, j):
            winLabel = "{} WINS!".format(self.getPlayerName())
            self.AnnouncementLabel["text"] = winLabel
            self.disableAllCells()
            rematch = "Rematch?"
            self.reLabel["text"] = rematch
            messageBox("Winner!", winLabel)
        elif self.pressed == 9:
            TieLabel = "That's a Draw!"
            self.AnnouncementLabel["text"] = TieLabel
            self.disableAllCells()
            rematch = "Rematch?"
            self.reLabel["text"] = rematch
            messageBox("Well Played!", TieLabel)
        else:
            self.changePlayer()
            self.AnnouncementLabel["text"] = "{}'s Turn".format(self.getPlayerName())
