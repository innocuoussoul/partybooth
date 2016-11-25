import uuid

from constants import *
from lib.CameraAdapter import FakeCameraAdapter
from lib.CollageGenerator import CollageGenerator


class PartyBooth:
    def __init__(self):
        self.camera_controller = None
        self.collage_generator = None
        self.prepare_directory_structure()

    def shoot_sequence(self, photoset):
        for i in range(4):
            self.camera_controller.takePicture(photoset)

    def set_camera_controller(self, controller):
        self.camera_controller = controller

    def set_collage_generator(self, controller):
        self.collage_generator = controller

    def prepare_directory_structure(self):
        self.create_folder(CAPTURE_FOLDER)
        self.create_folder(TEMP_FOLDER)
        self.create_folder(PHOTOS_FOLDER)

    def create_folder(self, path):
        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise

    @staticmethod
    def create_photoset():
        guid = uuid.uuid4().hex[:16]
        return {'id': guid, 'photos': []}


def main():
    app = PartyBooth()
    app.set_camera_controller(FakeCameraAdapter(PWD))
    # app.set_camera_controller(CameraController(PWD))
    app.set_collage_generator(CollageGenerator)
    photoset = app.create_photoset()
    app.shoot_sequence(photoset)
    print(photoset)


if __name__ == '__main__':
    main()
