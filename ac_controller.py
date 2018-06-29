# import RPi.GPIO as GPIO
# import httplib2
# import json
# import sys
# import time
# from datetime import datetime
# import settings
# import secret

# # Set the GPIO mode to use the board numbers
# GPIO.setmode(GPIO.BOARD)
# # Setting the GPIO output pin to 16
# pin = 16
# # Initialize the pin to be turned off
# GPIO.setup(pin, GPIO.OUT, initial=0)

# # Depending on the temperature and current state of the AC, turn it on/off or leave it on/off.
# def toggle_ac(temp):
#     if temp >= settings.temp_threshold and GPIO.input(pin) == 0:
#         print('Temp above threshold, turning AC on...')
#         GPIO.output(pin, 1)
#     elif temp >= settings.temp_threshold and GPIO.input(pin) == 1:
#         print('Temp above threshold, keeping AC on...')
#     elif temp < settings.temp_threshold and GPIO.input(pin) == 1:
#         print('Temp below threshold, turning AC off...')
#         GPIO.output(pin, 0)
#     else:
#         print('Temp below threshold, keeping AC off...')

# # The weather data is received as a bytestring
# def decode_and_parse_data(raw_data):
#     decoded_data = raw_data.decode('utf8').replace("'", '"')
#     return json.loads(decoded_data)

# # The temperature is returned in Kelvin - convert to Fahrenheit.
# def convert_k_to_f(temp_k):
#     return 9/5 * (temp_k - 273) + 32

# # Get the temperature from the decoded data.
# def get_temp(data):
#     temp_k = data['main']['temp']
#     return convert_k_to_f(temp_k)

# # Get local weather data
# def fetch_data():
#     h = httplib2.Http()
#     resp_headers, raw_data = h.request('http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={api_key}'.format(latitude=secret.latitude,
#                                                                                                                                               longitude=secret.longitude,
#                                                                                                                                               api_key=secret.api_key), 'GET')
#     return raw_data

# def execute():
#     while True:
#         raw_data = fetch_data()
#         data = decode_and_parse_data(raw_data)
#         temp = get_temp(data)
#         print('Temperature at {now} is {temp} degrees Fahrenheit.'.format(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),temp=temp))
#         toggle_ac(temp)
#         time.sleep(settings.sleep_period)








import RPi.GPIO as GPIO
import sys
import time
from lib.relay import Relay
from lib.thermometer import Thermometer

# Set the GPIO mode to use the board numbers
GPIO.setmode(GPIO.BOARD)
# Initialize the AC relay pin to be turned off
GPIO.setup(ac_relay_pin, GPIO.OUT, initial=0)

# After turning the relay on or maintaining current status, sleep this period
# before checking the temperature again.
period = 30

def execute(relay, thermometer):
    while True:
        temp = thermometer.get_temp()
        if temp >= relay.upper_threshold and relay.is_on == False:
            print("Turning unit on...")
            relay.turn_on()
            time.sleep(period)
        elif temp < relay.lower_threshold:
            print("Turning unit off...")
            relay.turn_off()
            time.sleep(relay.reset_period)
        else:
            print("Maintaining current status...")
            time.sleep(period)

if __name__ == '__main__':
    try:
        relay = Relay()
        thermometer = Thermometer()
        execute(relay, thermometer)
    except KeyboardInterrupt:
        print('Exiting...')
        GPIO.cleanup()
        sys.exit(0)
