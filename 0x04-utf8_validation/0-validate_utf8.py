#!/usr/bin/python3

'''determine if a dataset represents valid utf-8 encoding'''


def validUTF8(data) -> bool:
    ''' determines if a dataset is of valid utf-8 encoding'''
    no_bytes = 0
    for byte in data:
        mask = 1 << 7
        if not no_bytes:
            while byte & mask:
                no_bytes += 1
                mask >>= 1
            if not no_bytes:
                continue
            if no_bytes == 1 or no_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        no_bytes -= 1
    return no_bytes == 0