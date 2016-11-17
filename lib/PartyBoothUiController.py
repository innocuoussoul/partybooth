import logging
import os
import uuid

import constants as CONSTANTS
from lib.CameraController import FakeCameraController, CameraController
from lib.pages.CountDownPage import CountDownPage
from lib.pages.PhotoReviewPage import PhotoReviewPage


class PartyBoothController():
    logger = logging.getLogger("PartyBoothController")

    def __init__(self, partyBoothUI):
        self.partyBoothUI = partyBoothUI
        self.logger.info("Initialized")

        self.cameraController = self.createCameraController()

    def startCountDown(self):
        self.partyBoothUI.showFrame(CountDownPage.__name__)

    @staticmethod
    def createPhotoset():
        guid = uuid.uuid4().hex[:16]
        return {'id': guid, 'photos': [], 'thumbs': []}

    def capturePhoto(self, photoset):
        self.cameraController.takePicture(photoset)
        frame = self.partyBoothUI.showFrame(PhotoReviewPage.__name__)
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
            self.logger.warn("USE_CAMERA_STUB IS ACTIVE!")
            return FakeCameraController()
        else:
            self.logger.info("USING REAL CAMERA CONTROLLER")
            return CameraController()

    def showFrame(self, frame):
        self.partyBoothUI.showFrame(frame)
