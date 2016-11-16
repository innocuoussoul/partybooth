import Tkinter as tk

import time

from constants import TITLE_FONT


class CountDownPage(tk.Frame):

    COUNTDOWN_TICK_LENGTH = 1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,width=400, height=120)
        self.pack_propagate(0)
        self.controller = controller

        self.countdownLength = 1

        self.countdownText = tk.StringVar()
        self.countdownText.set(self.countdownLength)
        self.countdownLabel = tk.Label(self, fg='white', bg='red', borderwidth=10,
                                       textvariable=self.countdownText, font=("Sans", 80))

        self.countdownLabel.pack(fill=tk.BOTH,expand=True)
        self.bind("<<FRAME_ACTIVATED>>", self.countDown) # Not needed after refactoring

    # TODO has to be refactored intro controller, Pages are only for display and binding controller calls
    def countDown(self, event):

        self.countdownText.set("Get ready!")
        self.countdownLabel.update()
        time.sleep(self.COUNTDOWN_TICK_LENGTH)

        counter = self.countdownLength
        self.countdownText.set(str(counter))
        for i in range(counter):
            self.countdownText.set(str(counter - i))
            self.countdownLabel.update()
            time.sleep(self.COUNTDOWN_TICK_LENGTH)

        self.countdownText.set("Smile!")
        self.countdownLabel.update()
        time.sleep(self.COUNTDOWN_TICK_LENGTH)

        photoset = self.controller.createPhotoset()
        self.controller.capturePhoto(photoset)