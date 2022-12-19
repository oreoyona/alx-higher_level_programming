#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print(my_list[i], end='')
    except:
        return
    count = 0

    for i in my_list:
        count = count + 1
    return count
    
