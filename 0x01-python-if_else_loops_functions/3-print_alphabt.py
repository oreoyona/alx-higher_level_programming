#!/usr/bin/python3
print("{}".format\
      ("".join\
       ([chr(x) for x in range(97, 123) if chr(x) != 'e' and chr(x) != 'q'])), end='')
