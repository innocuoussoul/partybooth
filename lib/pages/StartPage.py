import Tkinter as tk

from constants import TITLE_FONT
from lib.pages.CountDownPage import CountDownPage
from lib.pages.PhotoReviewPage import PhotoReviewPage


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.startCountDown())
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame(PhotoReviewPage.__name__))
        button1.pack()
        button2.pack()