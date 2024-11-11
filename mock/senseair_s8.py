# Mock library of https://github.com/ndoornekamp/senseair_s8
class SenseairS8:

    def __init__(self, port="/dev/ttyS0", baudrate=9600, timeout=0.5):
        pass

    def co2(self):
        """
        Returns the measured CO2 value in parts per million (ppm), or None in case of an exception.
        :rtype: int | None
        """
        pass
