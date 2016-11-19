import logging
import os
import shutil
import subprocess

import constants as CONSTANTS


class CameraController:
    IMAGE_EXTENSION = '.jpg'
    logger = logging.getLogger("CameraController")

    def __init__(self):
        self.logger.info("Configuring Camera...")
        subprocess.call(['gphoto2', '--set-config', 'capturetarget=1'])
        subprocess.call(['gphoto2', '--set-config', 'imageformat=2'])
        self.logger.info("Configuring Camera completed")

    def takePicture(self, photoset):
        # shutil.copyfile(self.STUB_IMAGE_FOLDER + '/' + str(aufnahmeNummer) + self.IMAGE_EXTENSION,
        #                self.CAPTURE_FOLDER + '/' + str(aufnahmeNummer) + self.IMAGE_EXTENSION)

        filename = "%s_%s.jpg" % (photoset['id'], len(photoset['photos']) + 1)
        path = os.path.join(CONSTANTS.PWD, CONSTANTS.CAPTURE_FOLDER, filename)

        self.logger.info("Taking Photo...")
        subprocess.call(['gphoto2', '--capture-image-and-download', '--keep', '--force-overwrite', '--filename', path])

        if os.path.isfile(path):
            photoset['photos'].append(path)
            self.logger.info("Added Photo to Photoset " +  path)
        else:
            self.logger.error("Error while taking Photo: " + path)

class FakeCameraController (CameraController):

    logger = logging.getLogger("FakeCameraController")

    def takePicture(self, photoset):
        source_path = os.path.join(CONSTANTS.PWD, CONSTANTS.STUB_IMAGE_FOLDER, str(len(photoset['photos']) + 1) + self.IMAGE_EXTENSION)

        photoset['photos'].append(source_path)
        self.logger.info("Added Photo to Photoset " + source_path)

