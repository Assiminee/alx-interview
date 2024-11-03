#!/usr/bin/python3
"""
Utf-8 validation module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    data: List of integers
    return: True if data is a valid UTF-8 encoding, else return False
    """
    data = [n & 255 for n in data]
    try:
        bData = bytes(data)
        bData.decode('utf-8')
        return True
    except Exception:
        return False
