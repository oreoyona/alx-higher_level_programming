#!/usr/bin/python3
def al():
    return \
        [chr(x) for x in range(97, 123) if chr(x) != 'e' and chr(x) != 'q']


print("{}".format("".join(al())), end='')
