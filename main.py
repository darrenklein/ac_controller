import RPi.GPIO as GPIO
import sys
import time
from datetime import datetime
from lib.relay import Relay
from lib.temp_sensor import TempSensor

relay_pin = 16
# Set the GPIO mode to use the board numbers
GPIO.setmode(GPIO.BOARD)
# Initialize the AC relay pin in the off state
GPIO.setup(relay_pin, GPIO.OUT, initial=0)

# After turning the relay on or maintaining current status, sleep this period
# before checking the temperature again.
period = 30

def execute(relay, temp_sensor):
    while True:
        temp = temp_sensor.get_temp()
        print('Temperature at {now} is {temp} degrees Fahrenheit.'.format(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),temp=temp))
        if temp >= relay.upper_threshold and relay.is_on == False:
            print("Turning unit on...")
            relay.turn_on()
            time.sleep(period)
        elif temp < relay.lower_threshold and relay.is_on == False:
            print("Turning unit off...")
            relay.turn_off()
            # In this case, sleep for a manufacturer-specified reset period for the AC unit. Not all units may have such a recommendation.
            time.sleep(relay.reset_period)
        else:
            print("Maintaining current status...")
            time.sleep(period)

if __name__ == '__main__':
    try:
        relay = Relay(relay_pin)
        temp_sensor = temp_sensor()
        execute(relay, temp_sensor)
    except KeyboardInterrupt:
        print('Exiting...')
        GPIO.cleanup()
        sys.exit(0)
