# AC Controller
> A Python Raspberry Pi thermostat for an analog air conditioner.

This is a very basic IOT setup - the script turns a relay on or off (or leaves it on/off) based on temperature thresholds. Do with it what you will, I plugged an air conditioner into it.

Super big thanks to the folks at Adafruit for their great temperature sensing guide - (https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf)[https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf]

## Setup

### Hardware

- **Raspberry Pi** - I used a Pi Zero W 
- **DS18B20 Temperature sensor w/ 4.7k resistor** - (https://www.adafruit.com/product/381)[https://www.adafruit.com/product/381]
- **Controllable relay** - I used (https://dlidirect.com/products/iot-power-relay)[https://dlidirect.com/products/iot-power-relay]
- **Breadboard and associated hardware (breakout kit)**
- **5 male-to-male jumper cables**

### Put it all together now...

#### DS18B20

To set up the temperature sensor, follow the instructions at (https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf)[https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf] to wire up the breadboard and add OneWire support to your Pi.

#### Relay

Connect the relay's negative terminal with a male-to-male jumper to any ground pin - I used pin 6. Then connect the positive terminal with a male-to-male jumper to GPIO pin number 16.

## Use

Start the app with

```bash
python 3 main.py
```

### Screen

To allow this app to run perpetually in headless mode, I installed GNU Screen - https://www.gnu.org/software/screen/ on my Pi.

## Next steps...

I'd like to provide a simple user interface that would allow a person to manually turn the relay on/off and set different temperature ranges, etc.

I'm also planning to rebuild this app using Elixir Nerves.
