"""
This is code for getting the names of the players!.
"""
# TODO: To choose different fonts and colours to make it look better.
# TODO: We may want to restrict the names entered to a certain criteria, and pop-up a messagebox.showwarning.

# The Import Section
from tkinter import *
from tkinter import messagebox
from GameBoard import GameBoard


class GetPlayerNames2P(Tk):
    def __init__(self):
        super().__init__()
        self.title("XOX GAME!")
        # Kind of a Heading
        self.HeadingLabel = Label(self, text="Enter your names: ", padx=20)

        self.Names = Frame(self)

        self.Player1Label = Label(self.Names, text="Player 1: ", padx=40, pady=20)

        self.Player1Name = Entry(self.Names, text="")

        self.Player2Label = Label(self.Names, text="Player 2: ", padx=40, pady=20)

        self.Player2Name = Entry(self.Names, text="")

        self.top = Frame(self)

        self.submitLabel = Button(self, text="Submit", command=self.confirm_popup, bg="#90EE90", bd=10)
        self.Quit = Button(self, text="Quit", command=self.destroy, bg="#dc143c", bd=10)

        self.placeWidgets()

    def placeWidgets(self):
        self.HeadingLabel.pack()
        self.HeadingLabel.config(font=('Helvetica bold', 20))

        self.Names.pack()

        self.Player1Label.config(font=('Helvetica', 15))
        self.Player1Label.grid(row=0, column=0)

        self.Player1Name.grid(row=0, column=1)

        self.Player2Label.config(font=('Helvetica', 15))
        self.Player2Label.grid(row=1, column=0)

        self.Player2Name.grid(row=1, column=1)

        self.top.pack(side=TOP)

        self.submitLabel.config(font=('Helvetica', 15))

        self.Quit.config(font=('Helvetica', 15))

        self.resizable(False, False)

        self.submitLabel.pack(in_=self.top, side=LEFT)

        self.Quit.pack(in_=self.top, side=LEFT)

    def valid_names(self):
        return self.Player1Name.get() and self.Player2Name.get()

    def confirm_popup(self):
        if not self.valid_names():
            result = messagebox.askokcancel("Oops!", "Please recheck the player names!")
            if not result:  # When the user clicks cancel.
                self.Player1Name.delete(0, 'end')
                self.Player2Name.delete(0, 'end')
            return
        popup = Toplevel()
        popup.title("Confirmation")
        popup.geometry("200x200")
        requestLabel = Label(popup, text="Please Confirm Your Names!", font=('Helvetica', 11))
        requestLabel.pack()
        showPlayer1 = Label(popup, text="Player 1: " + self.Player1Name.get(), font=('Helvetica', 11))
        showPlayer1.pack()
        showPlayer2 = Label(popup, text="Player 2: " + self.Player2Name.get(), font=('Helvetica', 11))
        showPlayer2.pack()
        confirmButton = Button(popup, text="Confirm", command=self.startGame, bg="#90EE90", bd=10)
        Edit = Button(popup, text="Edit", command=popup.destroy, bg="#0275d8", bd=10)
        confirmButton.pack()
        Edit.pack()

    def startGame(self):
        g = GameBoard(self.Player1Name.get(), self.Player2Name.get())
        self.destroy()
        g.mainloop()