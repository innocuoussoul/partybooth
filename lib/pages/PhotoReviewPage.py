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
                              text="Processing...", font=(CONSTANTS.FONT_FACE, CONSTANTS.FONT_SIZE_BIG))
        self.label.bind("<Button-1>", lambda event: self.returnToStartPage())
        self.label.pack(fill=tk.BOTH, expand=True)


    # TODO has to be refactored intro controller
    def displayLastPhoto(self, photoset):
        image_path = photoset['thumbs'][len(photoset['thumbs'])-1]
        logger.info("Loading Image " + image_path)
        load = Image.open(os.path.join(CONSTANTS.CAPTURE_FOLDER, image_path))
        logger.info("Image Format: (%s - %s - %s)" % (load.format, load.size, load.mode))

        render = ImageTk.PhotoImage(image=load)

        self.imageLabel.image = render
        self.imageLabel.configure(image=render)

        self.label.pack_forget()
        self.imageLabel.pack()

        self.after(5000, self.returnToStartPage)

    def returnToStartPage(self):
        self.imageLabel.pack_forget()
        self.label.pack(    )
        self.controller.showFrame('StartPage')
