#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys


def printstats(dictn, size):
    """Console output."""
    print("File size: {:d}".format(size))
    for key in sorted(dictn.keys()):
        if dictn[key] != 0:
            print("{}: {:d}".format(i, dictn[key]))


stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
         "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printsts(stats, size)

        s_list = line.split()
        count += 1

        try:
            size += int(s_list[-1])
        except ValueError:
            pass

        try:
            if s_list[-2] in stats:
                stats[s_list[-2]] += 1
        except ValueError:
            pass
    printsts(stats, size)


except KeyboardInterrupt:
    printsts(sts, size)
    raise
