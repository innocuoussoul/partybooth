import logging
import os

import gphoto2 as gp

import constants as CONSTANTS


class CameraAdapter(object):
    IMAGE_EXTENSION = '.jpg'
    logger = logging.getLogger("PartyBooth.CameraAdapter")

    def __init__(self):
        gp.check_result(gp.use_python_logging())
        self.context = gp.Context()
        self.camera = gp.Camera()

    def connectToCamera(self):
        self.logger.info("Connecting to Camera...")
        self.camera.init(self.context)
        self._setCaptureTargetToCard()
        self._setImageTypeToJpg()
        self.camera.exit(self.context)
        self.logger.info("Connection successful!")

    def takePicture(self, photoset):
        filename = "%s_%s.jpg" % (photoset['id'], len(photoset['photos']) + 1)
        target_path = os.path.join(CONSTANTS.PWD, CONSTANTS.CAPTURE_FOLDER, filename)

        self.logger.info("Taking Photo...")
        self.camera.init(self.context)
        # subprocess.call(['gphoto2', '--capture-image-and-download', '--keep', '--force-overwrite', '--filename', target_path])
        camera_path = self.camera.capture(gp.GP_CAPTURE_IMAGE, self.context)
        self.logger.info('Image on camera {0}/{1}'.format(camera_path.folder, camera_path.name))

        self.logger.debug('Copying image to {0}'.format(target_path))
        camera_file = self.camera.file_get(camera_path.folder, camera_path.name, gp.GP_FILE_TYPE_NORMAL, self.context)
        camera_file.save(target_path)
        self.camera.exit(self.context)

        if os.path.isfile(target_path):
            photoset['photos'].append(target_path)
            self.logger.info("Added Photo to Photoset " + target_path)
        else:
            self.logger.error("Error while taking Photo: " + target_path)

    def _setCaptureTargetToCard(self):
        self._setCameraParameter('capturetarget', 1)

    def _setImageTypeToJpg(self):
        self._setCameraParameter('imageformat', 0)
        self._setCameraParameter('imageformatcf', 0)

    def _setCameraParameter(self, parameter, to_value):
        # get configuration tree
        config = gp.check_result(gp.gp_camera_get_config(self.camera, self.context))
        # find the capture target config item
        capture_target = gp.check_result(
            gp.gp_widget_get_child_by_name(config, parameter))
        value = gp.check_result(gp.gp_widget_get_choice(capture_target, to_value))
        gp.check_result(gp.gp_widget_set_value(capture_target, value))
        # set config
        gp.check_result(gp.gp_camera_set_config(self.camera, config, self.context))

    def __delete__(self, instance):
        instance.camera.exit()


class FakeCameraAdapter(CameraAdapter):
    logger = logging.getLogger("FakeCameraAdapter")

    def takePicture(self, photoset):
        source_path = os.path.join(CONSTANTS.PWD, CONSTANTS.STUB_IMAGE_FOLDER,
                                   str(len(photoset['photos']) + 1) + self.IMAGE_EXTENSION)

        photoset['photos'].append(source_path)
        self.logger.info("Added Photo to Photoset " + source_path)

    def connectToCamera(self):
        pass

    def _setCaptureTargetToCard(self):
        pass

    def _setImageTypeToJpg(self):
        pass
