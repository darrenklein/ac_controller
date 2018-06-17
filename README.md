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

## Use

Start the app running

```bash
python 3 main.py
```
