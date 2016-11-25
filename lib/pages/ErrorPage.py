# coding=UTF-8
import Tkinter as tk
import constants as CONSTANTS

class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=780, height=350)
        self.pack_propagate(0)

        self.controller = controller

        self.label = tk.Label(self, fg='white', bg='red', borderwidth=10,
                              text="Och nö! Irgendwas ist schief gelaufen :(\nBitte starte die PartyBooth neu", font=(CONSTANTS.FONT_FACE, CONSTANTS.FONT_SIZE_BIG))
        self.label.pack(fill=tk.BOTH, expand=True)
