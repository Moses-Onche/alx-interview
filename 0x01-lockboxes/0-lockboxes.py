#!/usr/bin/python3
"""Solves the locked boxes problem"""


def canUnlockAll(boxes):
    """Describes a function that takes list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
