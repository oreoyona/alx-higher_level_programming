#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpyl = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            cpyl[count] = True
        else:
            cpyl[count] = False
    return(cpyl)
