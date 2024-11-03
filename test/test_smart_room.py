import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_room_occupancy(self, mock_object: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        pass
