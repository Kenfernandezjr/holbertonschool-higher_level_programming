#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    strg = my_list.copy()

    if idx < 0:
        return(strg)

    elif idx > len(my_list):
        return(strg)

    else:
        strg[idx] = element
        return(strg)
