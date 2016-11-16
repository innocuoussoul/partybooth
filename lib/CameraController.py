import logging
import os
import shutil
import subprocess

import constants as CONSTANTS


class CameraController:
    IMAGE_EXTENSION = '.jpg'
    logger = logging.getLogger("CameraController")

    def __init__(self):
        pass

    def takePicture(self, photoset):
        # shutil.copyfile(self.STUB_IMAGE_FOLDER + '/' + str(aufnahmeNummer) + self.IMAGE_EXTENSION,
        #                self.CAPTURE_FOLDER + '/' + str(aufnahmeNummer) + self.IMAGE_EXTENSION)

        filename = "%s_%s.jpg" % (photoset['id'], len(photoset['photos']) + 1)
        path = os.path.join(CONSTANTS.PWD, 'captures', filename)

        subprocess.call(['gphoto2', '--capture-image-and-download', '--force-overwrite', '--filename', path],
                        stdout=False)

        if os.path.isfile(path):
            photoset['photos'].append(path)
        else:
            logging.error("Error while taking Photo: " + path)

class FakeCameraController (CameraController):

    def takePicture(self, photoset):
        source_path = os.path.join(CONSTANTS.PWD, CONSTANTS.STUB_IMAGE_FOLDER, str(len(photoset['photos']) + 1) + self.IMAGE_EXTENSION)
        target_path = os.path.join(CONSTANTS.PWD, CONSTANTS.CAPTURE_FOLDER, str(len(photoset['photos']) + 1) + self.IMAGE_EXTENSION)
        shutil.copyfile(source_path, target_path)
        photoset['photos'].append(target_path)
