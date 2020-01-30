#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_3 = tuple_b or (0, 0)

    if len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)

    if len(tuple_3) < 2:
        tuple_3 = (tuple_b[0], 0)

    new_tuple = (tuple_a[0] + tuple_3[0], tuple_a[1] + tuple_3[1])
    return new_tuple
