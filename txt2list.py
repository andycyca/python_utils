# -*- coding: utf-8 -*-
"""
Simple script to turn text files into lists.

One line, one item.

@author: Andycyca
"""

__author__ = 'Andycyca'
__copyright__ = 'Copyright 2020'
__credits__ = ['Andycyca']
__license__ = 'MPL'
__version__ = '2.0'
__maintainer__ = 'Andycyca'
__email__ = 'andycyca@gmail.com'
__status__ = 'Beta?'


def txt2list(textfile, score=False, init_score=0):
    outlist = []
    with open(textfile, encoding="utf-8") as f:
        for line in f:
            if score is False:
                outlist.append(line[:-1])
            else:
                outlist.append([line[:-1], init_score])
    return outlist
