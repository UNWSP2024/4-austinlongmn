# Programmer: Austin Long
# Date: 2/10/2025
# This file defines a function for making the process of getting user input easier.
from typing import Callable

print("user_input")
print(input, print)

# this function will handle the tedious task of getting valid input from the user.
def get_input(message: str, conversion: Callable[[str], any], error_message: str = "Invalid input.", validation=None):
    """
    This function gets input from the user with validation.
    :param message: The message to display to the user when prompting for the value.
    :param conversion: The conversion function that will turn the provided string into the value. Must throw ValueError if the input is invalid.
    :param error_message: The message that will be shown if the input is invalid.
    :param validation: The function to determine whether the converted value is valid (optional).
    :return: The converted value.
    """
    while True:
        try:
            value = conversion(input(message))
            if callable(validation) and not validation(value):
                raise ValueError(error_message)
            return value
        except ValueError:
            print(error_message)


def get_bool_input(message: str, error_message: str):
    """
    This function gets yes or no input from the user with validation.
    :param message: The message to display to the user when prompting for the value.
    :param error_message: The message that will be shown if the input is invalid.
    :return: The converted value.
    """

    def bool_conversion(user_input):
        normalized = user_input.upper()
        if normalized == "YES" or normalized == "Y":
            return True
        elif normalized == "NO" or normalized == "N":
            return False
        else:
            raise ValueError("Value must be \"Yes\" or \"No\".")

    return get_input(message, bool_conversion, error_message)
