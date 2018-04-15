#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Adding and removing keys from dictionaries"""


import data

CORRECTED = data.BANDS.copy()

NEW_VALUE2 = {'Dylan':{'Bob Dylan': ['vocals', 'guitar', 'harmonica']}}
CORRECTED.update(NEW_VALUE2)

del CORRECTED['Van Halen']['David Lee Roth']

NEW_VALUE = {'Sammy Hagar':['vocals']}
CORRECTED['Van Halen'].update(NEW_VALUE)
