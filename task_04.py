#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mergin dictionary data"""


import data

NEW_ENTRY = {
    'Buckingham Nicks':{'Lindsey Buckingham': ['guitar', 'vocals'],
    'Stevie Nicks': ['vocals', 'tambourine']
    }
}
data.BANDS.update(NEW_ENTRY)

NEW_VALUE = data.BANDS['Buckingham Nicks']

data.BANDS['Fleetwood Mac'].update(NEW_VALUE)
