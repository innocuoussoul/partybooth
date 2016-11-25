import logging
import os
import uuid

import gphoto2 as gp

import constants as CONSTANTS
from lib.CameraAdapter import FakeCameraAdapter, CameraAdapter
from lib.pages.CountDownPage import CountDownPage
from lib.pages.PhotoReviewPage import PhotoReviewPage


class PartyBoothController():
    logger = logging.getLogger("PartyBooth.PartyBoothController")

    def __init__(self, partyBoothUI):
        self.partyBoothUI = partyBoothUI
        self.logger.debug("Initialized")
        self.cameraController = self.createCameraController()

    def startCountDown(self):
        page = self.partyBoothUI.showPage(CountDownPage.__name__)
        page.countDown()
        photoset = self.createPhotoset()
        self.capturePhoto(photoset)

    @staticmethod
    def createPhotoset():
        guid = uuid.uuid4().hex[:16]
        return {'id': guid, 'photos': [], 'thumbs': []}

    def capturePhoto(self, photoset):
        self.cameraController.takePicture(photoset)
        frame = self.partyBoothUI.showPage(PhotoReviewPage.__name__)
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
            return FakeCameraAdapter()
        else:
            self.logger.info("USING REAL CAMERA CONTROLLER")
            return CameraAdapter()

    def showPage(self, frame):
        return self.partyBoothUI.showPage(frame)

    def connectToCamera(self):
        frame = self.showPage("ConnectionPage")
        self.checkCameraConnection(frame)

    def checkCameraConnection(self, frame):
        self.logger.info("Checking camera connection...")

        try:
            self.cameraController.connectToCamera()
            self.showPage("StartPage")
        except gp.GPhoto2Error as ex:
            if ex.code == gp.GP_ERROR_MODEL_NOT_FOUND:
                self.logger.info("Could not connect to camera. Retrying ...")
                frame.after(2000, self.checkCameraConnection, frame)
            else:
                raise
