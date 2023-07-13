#!/usr/bin/python3
"""
Module of a method that determines the number
of minimum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        required to get the exact number n H characters in a file
        args:
		n: Number of characters to be displayed
        return:
               number of min operations
    """

    #check = 1
    start = 0
    counter = 0
    for check in range(1, n):
        remainder = n - check
        if (remainder % check == 0):
            start = check
            check += start
            counter += 2
        else:
            check += start
            counter += 1
    return counter
