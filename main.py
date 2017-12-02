import argparse
import re
import sys

from websocket import run as websocket_run

SERVER_URL = 'wss://co-sensor.herokuapp.com'


def hex_type(serial_no, pattern=re.compile(r'^[0-9A-F]{16}$')):
    if not pattern.match(serial_no):
        raise argparse.ArgumentTypeError('Serial number should be a hex number, 16 characters long')
    return serial_no


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--test', dest="test", action="store_true", default=False
    )
    parser.add_argument('url', nargs='?', default=SERVER_URL)
    parser.add_argument('--serial', '-s', default="E8A44117E02E4147", type=hex_type)

    args = parser.parse_args(sys.argv[1:])
    if args.test:
        from test_sensor import TestSensor as Sensor
        sensor = Sensor(args.url, args.serial)
    else:
        from sensor import Sensor as Sensor
        sensor = Sensor(args.url)


    websocket_run(sensor)


if __name__ == '__main__':
    main()
