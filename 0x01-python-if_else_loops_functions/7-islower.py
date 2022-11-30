#!/usr/bin/python3
def islower(c):
    if isinstance(c, str):
        al = [chr(x) for x in range(97, 123)]
              if c in al:
                  return True
              return False
