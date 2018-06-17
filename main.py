import httplib2
import json
import secret

# The weather data is received as a bytestring
def decode_and_parse_data(raw_data):
    decoded_data = raw_data.decode('utf8').replace("'", '"')
    return json.loads(decoded_data)

# The temperature is returned in Kelvin - convert to Fahrenheit.
def convert_k_to_f(temp_k):
    return 9/5 * (temp_k - 273) + 32

# Get the temperature from the decoded data.
def get_temp(data):
    temp_k = decode_and_parse_data(raw_data)['main']['temp']
    return convert_k_to_f(temp_k)

# Get local weather data
def execute():
    h = httplib2.Http()
    resp_headers, raw_data = h.request(f'http://api.openweathermap.org/data/2.5/weather?lat={secret.latitude}&lon={secret.longitude}&APPID={secret.api_key}', 'GET')
    return raw_data

if __name__ == '__main__':
    raw_data = execute()
    data = decode_and_parse_data(raw_data)
    temp = get_temp(data)
    print(temp)
