#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("0 arguments")
    else:
        y = 1
        if len(sys.argv) == 2:
            print("1 argument")
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
        for x in range(1, len(sys.argv)):
            print("{}: {}".format(x, sys.argv[y]))
            y = y + 1
