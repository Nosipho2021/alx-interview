#!/usr/bin/python3
"""UTF-8 validation module"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding.
    """
    skip = 0

    for byte in data:
        if skip > 0:
            # Check if the byte is a valid continuation byte
            if (byte & 0b11000000) != 0b10000000:
                return False
            skip -= 1
        else:
            if (byte & 0b10000000) == 0b00000000:
                skip = 0  # 1-byte character
            elif (byte & 0b11100000) == 0b11000000:
                skip = 1  # 2-byte character
            elif (byte & 0b11110000) == 0b11100000:
                skip = 2  # 3-byte character
            elif (byte & 0b11111000) == 0b11110000:
                skip = 3  # 4-byte character
            else:
                return False

    return skip == 0
