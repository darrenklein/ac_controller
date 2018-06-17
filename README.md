# AC Controller

A simple Python app for Raspberry Pi, intended to turn on my air conditioner if it gets too hot.

## Setup

### Install Dependencies

This app uses *httplib2*. To install dependencies, run

```bash
pip3 install -r requirements.txt
```

### Credentials

This app gathers local weather information from *OpenWeatherMap*, which requires an API key. Include this value in a .gitignored file named `credentials.py`; for example:

```python
api_key = 'key_here'
```

## Use

Start the app running

```bash
python 3 main.py
```
