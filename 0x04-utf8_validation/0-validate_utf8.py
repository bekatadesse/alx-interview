#!/usr/bin/python3
"""
    UTF8-validator
"""


def validUTF8(data):
    """
    Validates whether the given list of integers represents
    a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing
        the UTF-8 encoding of a string.

    Returns:
        bool: True if the input data is a valid UTF-8 encoding,
              False otherwise.
    """
    # Count the number of bytes in the current UTF-8 sequence
    bytes_to_follow = 0
    for num in data:
        # Check if the current byte is the start of a new UTF-8 sequence
        if bytes_to_follow == 0:
            if num >> 5 == 0b110:
                bytes_to_follow = 1
            elif num >> 4 == 0b1110:
                bytes_to_follow = 2
            elif num >> 3 == 0b11110:
                bytes_to_follow = 3
            elif num >> 7 == 0b0:
                bytes_to_follow = 0
            else:
                return False
        # Check if the current byte is a continuation byte
        else:
            if num >> 6 != 0b10:
                return False
            bytes_to_follow -= 1
    # If there are still bytes left to follow, the input is invalid
    return bytes_to_follow == 0
