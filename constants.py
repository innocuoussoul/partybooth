import os
import logging

# Set this environment Variable to "true" in order to activate stubbing of the real gphoto2 interface
ENV_USE_CAMERA_STUB = "USE_CAMERA_STUB"


# Do not change from here
PWD = os.path.abspath(os.path.dirname(__file__))

TITLE_FONT = ("Helvetica", 18, "bold")

CAPTURE_FOLDER = os.path.join(PWD, "captures")

TEMP_FOLDER = os.path.join(PWD, "temp")

PHOTOS_FOLDER = os.path.join(PWD, "photos")

STUB_IMAGE_FOLDER = os.path.join(PWD, "test/images")
