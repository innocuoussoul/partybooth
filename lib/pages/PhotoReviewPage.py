import Tkinter as tk
import os
import logging
import subprocess

from PIL import ImageTk, Image

import constants as CONSTANTS

class PhotoReviewPage(tk.Frame):
    logger = logging.getLogger("PhotoReviewPage")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.imageLabel = tk.Label(self, padx=0, pady=0, borderwidth=5, background='white')
        self.imageLabel.bind("<Button-1>", lambda event: controller.showPage('StartPage'))

        self.label = tk.Label(self, fg='white', bg='red', borderwidth=10,
                              text="Processing...", font=(CONSTANTS.FONT_FACE, CONSTANTS.FONT_SIZE_BIG))
        self.label.bind("<Button-1>", lambda event: self.returnToStartPage())
        self.label.pack(fill=tk.BOTH, expand=True)


    # TODO has to be refactored intro controller
    def displayLastPhoto(self, photoset):

        photo_path = photoset['photos'][len(photoset['thumbs']) - 1]

        thumb_filename = "%s_%s_thumb.jpg" % (photoset['id'], len(photoset['photos']))
        thumb_path = os.path.join(CONSTANTS.PWD, CONSTANTS.TEMP_FOLDER, thumb_filename)

        self.logger.info("Creating Thumbnail " + thumb_path)
        subprocess.check_call(['convert', photo_path, '-strip', '-thumbnail', '700', '-quality', '80', thumb_path])
        if os.path.isfile(thumb_path):
            photoset['thumbs'].append(thumb_path)
            self.logger.info("Added Thumbnail to Photoset " + thumb_path)
        else:
            self.logger.error("Error while creating thumbnail: " + thumb_path)

        self.logger.info("Loading Thumbnail " + thumb_path)
        load = Image.open(os.path.join(CONSTANTS.CAPTURE_FOLDER, thumb_path))
        self.logger.info("Thumbnail Format: (%s - %s - %s)" % (load.format, load.size, load.mode))

        render = ImageTk.PhotoImage(image=load)

        self.imageLabel.image = render
        self.imageLabel.configure(image=render)

        self.label.pack_forget()
        self.imageLabel.pack()

        self.after_id = self.after(5000, self.returnToStartPage)

    def returnToStartPage(self):
        self.imageLabel.pack_forget()
        self.after_cancel(self.after_id)
        self.label.pack()
        self.controller.showPage('StartPage')
