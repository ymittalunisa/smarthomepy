import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_something(self, mock_object: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        pass

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_true(self, mock_infrared_pin: Mock):
        mock_infrared_pin.return_value=False
        sr=SmartRoom()
        self.assertTrue(sr.check_room_occupancy())

    @patch.object(GPIO, "input")
    def test_check_enough_light(self, mock_photoresistor_pin: Mock):
        mock_photoresistor_pin.return_value = False
        sr = SmartRoom()
        self.assertTrue(sr.check_enough_light())

    @patch.object(GPIO, "input")
    @patch.object(GPIO,"output")
    def test_manage_light_level(self, mock_infrared_pin: Mock, mock_photoresistor_pin: Mock, mock_smart_bulb: Mock):
        mock_photoresistor_pin.return_value = False
        mock_infrared_pin.return_value = True
        sr = SmartRoom()
        sr.light_on()
        mock_smart_bulb.assert_called_once_with(sr.LED_PIN, True)
        self.assertTrue(sr.light_on)