from sensor_interface import SensorInterface
import random
import time


class TestSensor(SensorInterface):

    def __init__(self, url, serial_no):
        self.start_measure = 5
        self._serial_no = serial_no
        print('SERIAL NUMBER: {}'.format(self._serial_no))
        super().__init__(url)

    def get_serial_number(self):
        return self._serial_no

    def measure(self):
        time.sleep(1.0 + random.random() * 0.2)
        self.start_measure += random.random() * 0.1 - 0.05
        return self.start_measure
