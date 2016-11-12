import os
import uuid

from lib.CameraController import CameraController, FakeCameraController
from lib.CollageGenerator import CollageGenerator

PWD = os.path.abspath(os.path.dirname(__file__))


class FunBox:
    def __init__(self):
        self.camera_controller = None
        self.collage_generator = None

    def shoot_sequence(self, photoset):
        for i in range(4):
            self.camera_controller.takePicture(photoset)

    def set_camera_controller(self, controller):
        self.camera_controller = controller

    def set_collage_generator(self, controller):
        self.collage_generator = controller

    @staticmethod
    def create_photoset():
        guid = uuid.uuid4().hex[:16]
        return {'id': guid, 'photos': []}


def main():
    app = FunBox()
    app.set_camera_controller(FakeCameraController(PWD))
    # app.set_camera_controller(CameraController(PWD))
    app.set_collage_generator(CollageGenerator)
    photoset = app.create_photoset()
    app.shoot_sequence(photoset)
    print(photoset)


if __name__ == '__main__':
    main()
