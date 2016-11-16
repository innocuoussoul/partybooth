import Tkinter as tk
import os
import logging

from PIL import ImageTk, Image

from constants import CAPTURE_FOLDER

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PhotoReviewPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.imageLabel = tk.Label(self, padx=0, pady=0, borderwidth=5, background='white')
        self.imageLabel.bind("<Button-1>", lambda event: controller.showFrame('StartPage'))
        self.imageLabel.pack()


    # TODO has to be refactored intro controller
    def displayLastPhoto(self, photoset):

        load = Image.open(os.path.join(CAPTURE_FOLDER, photoset['photos'][len(photoset['photos'])-1]))
        logger.info("Image Format: ", load.format, load.size, load.mode)

        load = load.resize((700, 466), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image=load)

        self.imageLabel.image = render
        self.imageLabel.configure(image = render)
        self.update()

        self.after(3000, self.controller.showFrame, 'StartPage')
