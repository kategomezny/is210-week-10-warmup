#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 07, Task 05"""


DATA = {
    1: 2690330,
    28: 3419150,
    10: 4091979,
    90: 2694405,
    83: 2694527,
    45: 1137701,
    11: 374362,
    2: 326826,
    -16: 417202,
    -40: 333525,
    -100: 361237,
    55: 1209719,
    2158: 1771800
}

def iter_dict_funky_sum(integers):
    """Dictionary iteration using the iteritems() method.

    Arg:
        integers: (int).  A set of key/value pairs.

    Return:
        Int:  Total

    Examples:

        >>> import task_07
        >>> task_07.iter_dict_funky_sum(task_07.DATA)
        21520436
    """
    integers = DATA
    funky = 0
    for key, value in DATA.iteritems():
        funky += value - key
    return funky
