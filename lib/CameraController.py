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
        path = os.path.join(CONSTANTS.PWD, CONSTANTS.CAPTURE_FOLDER, filename)

        thumb_filename = "%s_%s_thumb.jpg" % (photoset['id'], len(photoset['photos']) + 1)
        thumb_path = os.path.join(CONSTANTS.PWD, CONSTANTS.TEMP_FOLDER, thumb_filename)

        self.logger.info("Taking Photo...")
        subprocess.call(['gphoto2', '--capture-image-and-download', '--force-overwrite', '--filename', path],
                        stdout=False)

        if os.path.isfile(path):
            photoset['photos'].append(path)
            self.logger.info("Added Photo to Photoset " +  path)
        else:
            self.logging.error("Error while taking Photo: " + path)

        self.logger.info("Creating Thumbnail " + thumb_path)
        subprocess.check_call(['convert', path, '-strip', '-thumbnail', '700', '-quality', '80', thumb_path])
        if os.path.isfile(thumb_path):
            photoset['thumbs'].append(thumb_path)
            self.logger.info("Added Thumbnail to Photoset " + thumb_path)
        else:
            self.logger.error("Error while creating thumbnail: " + thumb_path)


class FakeCameraController (CameraController):

    logger = logging.getLogger("FakeCameraController")

    def takePicture(self, photoset):
        source_path = os.path.join(CONSTANTS.PWD, CONSTANTS.STUB_IMAGE_FOLDER, str(len(photoset['photos']) + 1) + self.IMAGE_EXTENSION)
        target_path = os.path.join(CONSTANTS.PWD, CONSTANTS.TEMP_FOLDER, str(len(photoset['photos']) + 1) + self.IMAGE_EXTENSION)

        self.logger.info("Creating Thumbnail " + target_path)
        subprocess.check_call(['convert', source_path, '-strip', '-thumbnail', '700', '-quality', '80', target_path])

        photoset['photos'].append(source_path)
        self.logger.info("Added Photo to Photoset " + source_path)
        photoset['thumbs'].append(target_path)
        self.logger.info("Added Thumbnail to Photoset " + target_path)
