import Tkinter as tk
import os
import logging

from PIL import ImageTk, Image

import constants as CONSTANTS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PhotoReviewPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.imageLabel = tk.Label(self, padx=0, pady=0, borderwidth=5, background='white')
        self.imageLabel.bind("<Button-1>", lambda event: controller.showFrame('StartPage'))

        self.label = tk.Label(self, fg='white', bg='red', borderwidth=10,
                              text="Processing Image...", font=("Sans", CONSTANTS.FONT_SIZE_BIG))
        self.label.bind("<Button-1>", lambda event: self.controller.startCountDown())
        self.label.pack(fill=tk.BOTH, expand=True)


    # TODO has to be refactored intro controller
    def displayLastPhoto(self, photoset):

        load = Image.open(os.path.join(CONSTANTS.CAPTURE_FOLDER, photoset['photos'][len(photoset['photos'])-1]))
        logger.info("Image Format: (%s - %s - %s)" % (load.format, load.size, load.mode))

        load = load.resize((700, 466), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image=load)

        self.imageLabel.image = render
        self.imageLabel.configure(image=render)

        self.label.pack_forget()
        self.imageLabel.pack()

        self.after(3000, self.returnToStartPage)

    def returnToStartPage(self):
        self.imageLabel.pack_forget()
        self.label.pack(    )
        self.controller.showFrame('StartPage')