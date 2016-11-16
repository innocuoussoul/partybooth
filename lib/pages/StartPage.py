import Tkinter as tk
import constants as CONSTANTS

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=650, height=120)
        self.pack_propagate(0)

        self.controller = controller

        self.label = tk.Label(self, fg='white', bg='red', borderwidth=10,
                              text="Tap to take photo!", font=("Sans", CONSTANTS.FONT_SIZE_BIG))
        self.label.bind("<Button-1>", lambda event: self.controller.startCountDown())
        self.label.pack(fill=tk.BOTH, expand=True)
