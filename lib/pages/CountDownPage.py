import Tkinter as tk
import time

import constants as CONSTANTS


class CountDownPage(tk.Frame):
    COUNTDOWN_TICK_LENGTH = 1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=140)
        self.pack_propagate(0)
        self.controller = controller

        self.countdownLength = 3

        self.countdownText = tk.StringVar()
        self.countdownText.set(self.countdownLength)
        self.countdownLabel = tk.Label(self, fg='white', bg='red', borderwidth=10,
                                       textvariable=self.countdownText, font=(CONSTANTS.FONT_FACE, CONSTANTS.FONT_SIZE_BIG))

        self.countdownLabel.pack(fill=tk.BOTH, expand=True)
        self.bind("<<FRAME_ACTIVATED>>", self.countDown)  # Not needed after refactoring

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
