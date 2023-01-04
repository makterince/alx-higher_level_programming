#!/usr/bin/python3
def print_last_digit(number):
    # if the number is negative
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end="")
        # if the number is positive
    else:
        last_digit = number % 10
        print(last_digit, end="")
    # return the absolute value with the abs function
    return abs(last_digit)
