#!/usr/bin/python3
def x():
    return \
        ["{:02d}".format((x)[0], (x)[-1])  for x in range(1, 100)]


print(x())
