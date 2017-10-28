# CO Sensor [Raspberry Pi] + [Django Channels] Project - Client

# Getting started

## Virtual environment

#### Create virtual environment
`python -m venv ../client-env`
#### Activate virtual environment
`source ../client-env/bin/activate`
#### Install required python modules
`pip install -r requirements.txt`

## Run the client

#### On Raspberry Pi with live server *https://co-sensor.herokuapp.com*
`python main.py`

#### On Raspberry Pi with different server URL
`python main.py wss://server-url.com`

#### Test client mocking the behaviuor of existing Raspberry Pi with different server URL
`python main.py --test ws://localhost:5000`
