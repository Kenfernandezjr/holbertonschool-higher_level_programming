#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx < 0:
        return(my_list)

    elif len(my_list) > idx:
        new = my_list.copy()
        new[idx] = element
        return(new)

    else:
        return(my_list)
