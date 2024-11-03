# Mock library of https://github.com/adafruit/Adafruit_CircuitPython_BMP280
from mock.board import I2C

class Adafruit_BMP280_I2C:

    def __init__(self, i2c: I2C, address: int = 0x77):
        pass

    @property
    def temperature(self):
        return self.temperature

    @temperature.setter
    def temperature(self, value):
        self.temperature = value
