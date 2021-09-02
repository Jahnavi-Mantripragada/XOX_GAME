# TODO: To choose different fonts and colours to make it look better.

# The Import Section
from tkinter import *
from PlayerNames import PlayerNameInput
from GameBoard import GameBoard


class NumberOfPlayers(Tk):
    def __init__(self):
        super().__init__()
        self.title("XOX GAME!")

        self.AskLabel = Label(self, padx=20)

        self.Single_Player = Button(self, text="Single Player (1P)", bg="#0275d8", width=25, command=self.P1)

        self.Two_Player = Button(self, text="Two Players (2P)", bg="#0275d8", width=25, command=self.P2)

        self.placeWidgets()

    def placeWidgets(self):
        self.AskLabel["text"] = "How many Players?"

        self.AskLabel.config(font=('Helvetica', 25))

        self.AskLabel.pack()

        self.Single_Player.config(font=('Helvetica', 13))

        self.Two_Player.config(font=('Helvetica', 13))

        self.Single_Player.pack()

        self.Two_Player.pack()

    def P1(self):
        self.destroy()
        player_1 = PlayerNameInput(1)
        player_1.mainloop()
        g = GameBoard(player_1.player_name)
        g.mainloop()

    def P2(self):
        self.destroy()
        player_1 = PlayerNameInput(1)
        player_1.mainloop()
        player_2 = PlayerNameInput(2)
        player_2.mainloop()
        g = GameBoard(player_1.player_name, player_2.player_name)
        g.mainloop()


if __name__ == "__main__":
    x = NumberOfPlayers()
    x.mainloop()
