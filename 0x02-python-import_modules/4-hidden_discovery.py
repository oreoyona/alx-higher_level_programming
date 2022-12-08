#!/usr/bin/python3
if __name__ == '__main__':
    names = __import__('hidden_4.pyc')
    for x in names:
        if x.startswith('__'):
            continue
        print("{}".format(x))
