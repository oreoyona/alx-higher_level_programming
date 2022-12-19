#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            if type(my_list[i]) == "int":
                count = count + 1
                print("{:d}".format(my_list[i], end='')
        print()
    except Exception as e:
        print(e)
    return count
