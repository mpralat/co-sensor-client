import sys
import serial
import argparse
from datetime import datetime
from websocket import run as websocket_run

SERVER_URL = 'wss://co-sensor.herokuapp.com'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--test', dest="test", action="store_true", default=False
    )
    parser.add_argument('url', nargs='?', default=SERVER_URL)

    args = parser.parse_args(sys.argv[1:])
    if args.test:
        from test_sensor import TestSensor as Sensor
    else:
        from sensor import Sensor as Sensor
    sensor = Sensor(args.url)

    websocket_run(sensor)


if __name__ == '__main__':
    main()
