#!/usr/bin/python3

def no_c(my_string):

    return(my_string.translate({ord(s): None for s in 'cC'}))
