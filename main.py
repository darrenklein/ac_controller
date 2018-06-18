import httplib2
import json
import sys
import time
from datetime import datetime
import settings
import secret

# AC turned off by default
ac_on = False

# Depending on the temperature and current state of the AC, turn it on/off or leave it on/off.
def toggle_ac(temp):
    global ac_on

    if temp >= settings.temp_threshold and ac_on == False:
        ac_on = True
        print('Temp above threshold, turning AC on...')
    elif temp >= settings.temp_threshold and ac_on == True:
        print('Temp above threshold, keeping AC on...')
    elif temp < settings.temp_threshold and ac_on == True:
        ac_on = False
        print('Temp below threshold, turning AC off...')
    else:
        print('Temp below threshold, keeping AC off...')

# The weather data is received as a bytestring
def decode_and_parse_data(raw_data):
    decoded_data = raw_data.decode('utf8').replace("'", '"')
    return json.loads(decoded_data)

# The temperature is returned in Kelvin - convert to Fahrenheit.
def convert_k_to_f(temp_k):
    return 9/5 * (temp_k - 273) + 32

# Get the temperature from the decoded data.
def get_temp(data):
    temp_k = data['main']['temp']
    return convert_k_to_f(temp_k)

# Get local weather data
def fetch_data():
    h = httplib2.Http()
    resp_headers, raw_data = h.request('http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={api_key}'.format(latitude=secret.latitude,longitude=secret.longitude,api_key=secret.api_key), 'GET')
    return raw_data

def execute():
    while 1:
        print('Checking local weather data...')
        raw_data = fetch_data()
        data = decode_and_parse_data(raw_data)
        temp = get_temp(data)
        print('Temperature at {now} is {temp} degrees Fahrenheit.'.format(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),temp=temp))
        toggle_ac(temp)
        time.sleep(settings.sleep_period)

if __name__ == '__main__':
    try:
        execute()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
