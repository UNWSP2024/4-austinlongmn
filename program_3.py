#!/usr/bin/env python
# Programmer: Austin Long
# Date: 2/12/2025
# Program: Average Rainfall

# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.
from typing import Callable

from user_input import get_input

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    # get the start year (this is used to show the user what year they are inputting for)
    start_year = get_input("Enter the year to start at: ",
                           int,
                           "You must enter an integer for the year.")

    # get the number of years to average
    num_years = get_input("Enter the number of years: ",
                          int,
                          "The number of years must be a valid positive integer.",
                          lambda num: num >= 0)

    # initialize the final value
    sum_rainfall = 0.0

    # for each year, input each month's average and average those
    for year_offset in range(num_years):
        yr_sum_rainfall = 0.0

        # iterate over months
        for month in MONTHS:
            # get average for month
            yr_sum_rainfall += get_input(f"Enter the average rainfall for {month} {start_year + year_offset}: ",
                                         float,
                                         "The average rainfall must be a valid positive number.",
                                         lambda num: num >= 0.0)

        # average rainfall over months
        sum_rainfall += yr_sum_rainfall / len(MONTHS)

    # average up all years
    avg_rainfall = sum_rainfall / num_years

    # display to user
    print(f"The average rainfall over these years was {avg_rainfall}")


if __name__ == '__main__':
    main()
