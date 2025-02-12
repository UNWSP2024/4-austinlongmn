#!/usr/bin/env python
# Programmer: Austin Long
# Date: 2/12/2025
# Bank Balance
from collections.abc import Callable


# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

# this function will handle the tedious task of getting valid input from the user.
# (I had to move it to this file because pytest didn't like the redirected input and print functions
# across modules)
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


def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0  # initialize for while loop
    total = 0.0

    # get budget
    budget = get_input("Enter your budget for the month: $",
                       float,
                       "You must enter a valid positive number.",
                       lambda amount: amount >= 0)

    # loop for each item
    while True:
        # input price from user
        spent = get_input("Enter the price of the item (signal EOF or enter 0 if you are done): $",
                          float,
                          "You must enter a valid number (no currency symbols).",
                          lambda price: price >= 0)

        # if 0, then we are done.
        if spent == 0:
            break

        # add item to total
        total += spent

    # get difference
    difference = budget - total

    # display output to user
    if difference < 0:
        print(f"You are ${-difference:.2f} over budget.")
    else:
        print(f"You are ${difference:.2f} under budget. Good job!")


if __name__ == '__main__':
    main()
