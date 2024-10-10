#!/usr/bin/python3
"""
Lockbox algorithm
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    """
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
