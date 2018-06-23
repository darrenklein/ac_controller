# AC Controller

A simple Python app for Raspberry Pi, intended to turn on my air conditioner if it gets too hot.

## Setup

### Install Dependencies

This app uses *httplib2*. To install dependencies, run

```bash
pip3 install -r requirements.txt
```

### secret.py

This app gathers local weather information from *OpenWeatherMap*, which requires an API key. Include this value in a .gitignored file named `secret.py`, along with latitude/longitude coordinates for the desired location. For example:

```python
api_key = 'key_here'
latitude = 30.5
longitude = -75.0
```

### GPIO/Breadboard

This is a very basic IOT setup - ultimately, this isn't controlling the air conditioner directly, but rather is controlling a relay - I'm using the AC/DC controllable relay put out by Digital Loggers - https://dlidirect.com/products/iot-power-relay

Connect the relay's negative terminal with a male-to-male jumper to any ground pin - I'm using pin 6. Then connect the positive terminal with a male-to-male jumper to a GPIO pin - in my code, I'm using pin 16.

## Use

Start the app running

```bash
python 3 main.py
```

### Screen

To allow this app to run perpetually in headless mode, I installed GNU Screen - https://www.gnu.org/software/screen/ on my Raspberry Pi 3 B+.

### Settings

You can customize the behavior a bit with the values in the `settings.py` file.

`sleep_period` will change how frequently the script checks the local temperature.

`temp_threshold` is the value above which a certain behavior (in this case, turning on my air conditioner) should take place.
