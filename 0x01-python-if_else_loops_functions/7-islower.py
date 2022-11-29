#!/usr/bin/python3
def islower(c):
    al = [chr(x) for x in range(97, 123)]
    if c in al:
        return True
    return False
