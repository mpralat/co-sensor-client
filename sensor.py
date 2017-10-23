import serial
from sensor_interface import SensorInterface


class Sensor(SensorInterface):

    def __init__(self, url):
        self.serial = serial.Serial("/dev/ttyACM0", 9600)
        super().__init__(url)

    def get_serial_number(self):
        cpu_serial = "ERROR000000000"

        with open('/proc/cpuinfo', 'r') as file:
            for line in file:
                if line[0:6] == 'Serial':
                    cpu_serial = line[10:26].upper()
                    file.close()
                    break

        return cpu_serial

    def measure(self):
        value = int(self.serial.readline())
        return value / 32
