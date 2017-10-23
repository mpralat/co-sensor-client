from sensor_interface import SensorInterface
import random
import time


class TestSensor(SensorInterface):

    def __init__(self, url):
        self.start_measure = 5
        super().__init__(url)

    def get_serial_number(self):
        return "E8A44117E02E4147"

    def measure(self):
        time.sleep(1.0 + random.random() * 0.2)
        self.start_measure += random.random() * 0.1 - 0.05
        return self.start_measure
