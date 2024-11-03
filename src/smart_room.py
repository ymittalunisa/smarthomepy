import time
try:
    import adafruit_bmp280
    import board
    import RPi.GPIO as GPIO
except:
    import mock.adafruit_bmp280 as adafruit_bmp280
    import mock.board as board
    import mock.GPIO as GPIO


class SmartRoom:
    GAS_PIN = 29
    SERVO_PIN = 31
    BUZZER_PIN = 36
    INFRARED_PIN = 22
    LIGHT_PIN = 37
    PHOTO_PIN = 13

    def __init__(self):
        # GPIO pin setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GAS_PIN, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN, GPIO.IN)
        GPIO.setup(self.PHOTO_PIN, GPIO.IN)
        GPIO.setup(self.LIGHT_PIN, GPIO.OUT)
        GPIO.setup(self.BUZZER_PIN, GPIO.OUT)
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)

        i2c = board.I2C()
        self.bmp280_indor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
        self.bmp280_outdoor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x68)

        self.servo = GPIO.PWM(self.SERVO_PIN, 50) # Sets up the pin as a PWM pin
        self.servo.start(2) # Starts generating PWM on the pin with a duty cycle equal to 2% (corresponding to 0 degree)
        time.sleep(1) # Waits 1 second so that the servo motor has time to make the turn
        self.servo.ChangeDutyCycle(0) # Sets duty cycle equal to 0% (corresponding to a low signal)

        self.light_on = False
        self.window_open = False
        self.buzzer_on = False

        GPIO.output(self.LIGHT_PIN, GPIO.LOW)
        GPIO.output(self.BUZZER_PIN, GPIO.LOW)

    def check_room_occupancy(self) -> bool:
        # To be implemented
        pass

    def check_enough_light(self) -> bool:
        # To be implemented
        pass

    def manage_light_level(self) -> None:
        # To be implemented
        pass

    def open_window(self) -> None:
        # To be implemented
        pass

    def close_window(self) -> None:
        # To be implemented
        pass

    def manage_window(self) -> None:
        # To be implemented
        pass

    def monitor_air_quality(self) -> None:
        # To be implemented
        pass

    def change_servo_angle(self, duty_cycle) -> None:
        """
        Changes the servo motor's angle by passing it the corresponding PWM duty cycle
        :param duty_cycle: the width of the PWM duty cycle (it's a percentage value)
        """
        self.servo.ChangeDutyCycle(duty_cycle) # Changes the duty cycle
        time.sleep(1) # Waits 1 second so that the servo motor has time to make the turn
        self.servo.ChangeDutyCycle(0) # Set duty cycle equal to 0%


class SmartRoomError(Exception):
    pass
