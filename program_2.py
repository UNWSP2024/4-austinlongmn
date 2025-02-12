#!/usr/bin/env python
# Programmer: Austin Long
# Date: 2/12/2025
# Program: Movie Tix

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.


def main():
    # initialize variables
    total = 0
    while True:
        # input movie
        input("Enter a movie: ")

        # input valid integer for number of tickets
        while True:
            try:
                num_tickets = int(input("Enter the number of tickets that you want: "))
                if num_tickets < 0:
                    print("Error: you must enter a positive number of tickets.")
                else:
                    break
            except ValueError: # user didn't enter a number
                print("Error: you must enter a valid positive integer number.")

        # add to total
        total += num_tickets

        if input("Would you like to input another movie? (y/n) ").upper() == "N":
            break

    # display total
    print(f"You will need to by {total} tickets in total.")

if __name__ == '__main__':
    main()