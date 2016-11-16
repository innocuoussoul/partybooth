#! /usr/bin/python

# import tkinter as tk   # python3
import Tkinter as tk  # python
import os
import uuid
import logging

from PIL import ImageTk

import constants as CONSTANTS
from lib.CameraController import FakeCameraController, CameraController
from lib.pages.CountDownPage import CountDownPage
from lib.pages.PhotoReviewPage import PhotoReviewPage
from lib.pages.StartPage import StartPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PartyBooth")

class PartyBooth(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.prepare_directory_structure()

        self.cameraController = self.createCameraController()

        # self.geometry("800x480")
        self.attributes("-fullscreen", True)

        image = ImageTk.PhotoImage(file='resources/images/splash.png')
        background = tk.Label(self, image=image)
        background.image = image
        background.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others, or grid.remove()d
        self.container = tk.Frame(self)
        # container.pack(side="top", fill="both", expand=True)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        # container.grid_propagate(0)

        self.frames = {}
        for F in (StartPage, CountDownPage, PhotoReviewPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(StartPage.__name__)
        # background.lower()

    def showFrame(self, page_name):
        logger.info("Showing Frame: " + page_name)
        # Show a frame for the given page name
        # only raise frame in question leaving the rest untouched
        # frame = self.frames[page_name]
        # frame.tkraise()

        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
        self.update()
        frame.event_generate("<<FRAME_ACTIVATED>>")
        return frame

    def startCountDown(self):
        self.showFrame(CountDownPage.__name__)

    @staticmethod
    def createPhotoset():
        guid = uuid.uuid4().hex[:16]
        return {'id': guid, 'photos': [], 'thumbs': []}

    def capturePhoto(self, photoset):
        self.cameraController.takePicture(photoset)
        frame = self.showFrame(PhotoReviewPage.__name__)
        frame.displayLastPhoto(photoset)

    def prepare_directory_structure(self):
        self.create_folder(CONSTANTS.CAPTURE_FOLDER)
        self.create_folder(CONSTANTS.TEMP_FOLDER)
        self.create_folder(CONSTANTS.PHOTOS_FOLDER)

    def create_folder(self, path):
        try:
            os.makedirs(path)
            self.logger.info("Created folder " + path)
        except OSError:
            if not os.path.isdir(path):
                raise

    def createCameraController(self):
        useFake = os.environ.get(CONSTANTS.ENV_USE_CAMERA_STUB)

        if useFake:
            logger.warn("USE_CAMERA_STUB IS ACTIVE!")
            return FakeCameraController()
        else:
            logger.info("USING REAL CAMERA CONTROLLER")
            return CameraController()

if __name__ == "__main__":
    app = PartyBooth()
    app.mainloop()
