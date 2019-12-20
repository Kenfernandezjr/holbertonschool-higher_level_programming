#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for x in (my_list):
        if x == search:
            my_list[search] = replace
