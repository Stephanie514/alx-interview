#!/usr/bin/python3
"""
validate_utf8 module
    Requirement:
        Prototype: def validUTF8(data)
        Return: True if data is a valid UTF-8 encoding, else return False
        A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data, therefore you only
        need to handle the 8 least significant bits of each integeer
"""


def validUTF8(data):
    """Determines if a given data set represents
     a valid UTF-8 encoding or not
    """
    def is_start_byte(byte):
        return (byte & 128) == 0 or (byte & 224) == 192 or \
               (byte & 240) == 224 or (byte & 248) == 240

    def is_continuation_byte(byte):
        return (byte & 192) == 128

    count = 0
    for d in data:
        if count == 0:
            if not is_start_byte(d):
                return False
            if (d & 224) == 192:
                count = 1
            elif (d & 240) == 224:
                count = 2
            elif (d & 248) == 240:
                count = 3
        else:
            if not is_continuation_byte(d):
                return False
            count -= 1
    return count == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))
    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111,
            108, 33]
    print(validUTF8(data))
    data = [229, 65, 127, 256]
    print(validUTF8(data))
