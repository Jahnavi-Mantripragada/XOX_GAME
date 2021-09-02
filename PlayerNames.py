"""
This is code for getting the names of the players!.
"""
# TODO: To choose different fonts and colours to make it look better.
# TODO: We may want to restrict the names entered to a certain criteria, and pop-up a messagebox.showwarning.

# The Import Section
from tkinter import *
from tkinter import messagebox



def messageBoxAskOrCancel(title, text):
    root = Tk()
    root.withdraw()
    r = messagebox.askokcancel(title, text)
    root.destroy()
    return r


class PlayerNameInput(Tk):
    def __init__(self, player_index):
        super().__init__()
        self.title("XOX GAME!")

        self.player_index = player_index

        self.player_name = ""

        # Kind of a Heading
        self.HeadingLabel = Label(self, text="Enter your name: ", padx=20)

        self.Names = Frame(self)

        self.PlayerLabel = Label(self.Names, text="Player {}: ".format(self.player_index), padx=40, pady=20)

        self.PlayerName = Entry(self.Names, text="")

        self.top = Frame(self)

        self.submitLabel = Button(self.top, text="Submit", command=self.confirm_popup, bg="#90EE90", bd=10)
        self.Quit = Button(self.top, text="Quit", command=self.destroy, bg="#dc143c", bd=10)

        self.placeWidgets()

    def placeWidgets(self):
        self.HeadingLabel.pack()
        self.HeadingLabel.config(font=('Helvetica bold', 20))

        self.Names.pack()

        self.PlayerLabel.config(font=('Helvetica', 15))
        self.PlayerLabel.grid(row=0, column=0)

        self.PlayerName.grid(row=0, column=1)

        self.top.pack(side=TOP)

        self.submitLabel.config(font=('Helvetica', 15))

        self.Quit.config(font=('Helvetica', 15))

        self.resizable(False, False)

        self.submitLabel.pack(in_=self.top, side=LEFT)

        self.Quit.pack(in_=self.top, side=LEFT)

    def valid_names(self):
        return len(self.PlayerName.get()) != 0

    def confirm_popup(self):
        if not self.valid_names():
            result = messageBoxAskOrCancel("Oops!", "Please recheck the player name!")
            if not result:  # When the user clicks cancel.
                self.PlayerName.delete(0, 'end')
            return

        popup = Toplevel(self)
        popup.title("Confirmation")
        popup.geometry("200x200")
        requestLabel = Label(popup, text="Please Confirm Your Name!", font=('Helvetica', 11))
        requestLabel.pack()
        showPlayer = Label(popup, text="Player{}: {}".format(self.player_index, self.PlayerName.get()),
                           font=('Helvetica', 11))
        showPlayer.pack()
        confirmButton = Button(popup, text="Confirm", command=self.confirmed_name, bg="#90EE90", bd=10)
        Edit = Button(popup, text="Edit", command=popup.destroy, bg="#0275d8", bd=10)
        confirmButton.pack()
        Edit.pack()

    def confirmed_name(self):
        self.player_name = self.PlayerName.get()
        self.destroy()


if __name__ == "__main__":
    g1 = PlayerNameInput(1)
    g1.mainloop()
    g2 = PlayerNameInput(2)
    g2.mainloop()
