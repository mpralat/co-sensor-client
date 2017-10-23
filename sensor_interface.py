import serial


class SensorInterface:

    def __init__(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_serial_number(self):
        pass

    def measure(self):
        pass
