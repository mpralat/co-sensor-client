from sensor_interface import SensorInterface
import asyncio
import websockets
import json
import datetime
from tzlocal import get_localzone


async def sensor_client(sensor: SensorInterface):
    url = sensor.get_url()
    url += '/sensors/room/' + sensor.get_serial_number() + '/sensor'
    print("Attempting to connect to", url)

    async with websockets.connect(url) as websocket:
        print("Connected to", url)

        while True:
            measurement = sensor.measure()
            now = datetime.datetime.now().astimezone(get_localzone())
            payload = {
                "timestamp": now.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
                "value": measurement
            }
            print(payload)
            dumped = json.dumps(payload)
            try:
                await websocket.send(dumped)
            except Exception as error:
                print("EXCEPTION OCCURED DURING SENDING DATA\n", error)
                websocket.close()
                break

    print("Closed connection.")


def run(sensor):
    try:
        asyncio.get_event_loop().run_until_complete(
            sensor_client(sensor)
        )
    except BrokenPipeError as error:
        print(error)
