# -*- coding: utf-8 -*-
import unittest

import gphoto2 as gp
from flexmock import flexmock

from .context import CameraAdapter
from .context import ErrorPage
from .context import PartyBooth
from .context import PartyBoothController
from .context import PhotoReviewPage


class PhotoBoothControllerTest(unittest.TestCase):
    def setUp(self):
        PartyBooth.configureLogging()
        self.cameraAdapterMock = flexmock(
            connectToCamera=lambda: None,
            takePicture=lambda x: None
        )

        self.partyBoothMock = flexmock(
            showPage=lambda page: None
        )

        flexmock(CameraAdapter).new_instances(self.cameraAdapterMock)
        self.boothController = PartyBoothController(self.partyBoothMock)
        self.photoset = self.boothController.createPhotoset()

    def test_CapturePhoto_RoutesToErrorPage_OnGphotoError(self):
        (flexmock(self.cameraAdapterMock)
         .should_receive('takePicture')
         .and_raise(gp.GPhoto2Error, gp.GP_ERROR_TIMEOUT))

        flexmock(self.partyBoothMock).should_receive('showPage').with_args(ErrorPage.__name__).once()
        flexmock(self.partyBoothMock).should_receive('showPage').with_args(PhotoReviewPage.__name__).times(0)

        self.boothController.capturePhoto(self.photoset)
