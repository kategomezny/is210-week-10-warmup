#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Changing dictionary values"""


import data

NEW_SUPERHEROES = data.SUPERHEROES.copy()

NEW_SUPERHEROES['Logan']['alias'] = 'Wolverine'
