""" A class representing the thermometer """
class Thermometer:
    # The thermometer returns temperature in Celsius - convert to Fahrenheit.
    def convert_c_to_f(self, temp_c):
        return (temp_c * 1.8) + 32

    def get_temp(self):
        # TODO: Get the actual temp from the thermometer.
        return self.convert_c_to_f(30.0)

    # TODO: Assign a GPIO pin and set it here - then use that pin in get_temp.
    # def __init__(self):
    #     self.gpio_pin = XXXXX
