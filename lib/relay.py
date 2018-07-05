""" A class representing the controllable relay """
import RPi.GPIO as GPIO

class Relay:
    def turn_on(self):
        self.is_on = True
        return GPIO.output(self.gpio_pin, 1)

    def turn_off(self):
        self.is_on = False
        return GPIO.output(self.gpio_pin, 0)

    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        # If the temp goes above the upper threshold, turn on the unit. If it goes below the
        # lower threshold, turn it off. Leave a buffer in between, so that it won't quickly turn
        # itself back off.
        # TODO: performance-tune this.
        self.upper_threshold = 77.00
        self.lower_threshold = 76.00
        # According the the AC unit in use, if it has been turned off, wait three minutes
        # before attempting to turn it back on.
        self.reset_period = 180
        self.is_on = False
