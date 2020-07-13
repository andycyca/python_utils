# -*- coding: utf-8 -*-
"""
Naive character and string encoding to binary

Created on Wed Jul  8 12:55:04 2020

@author: Andycyca
"""

__author__ = 'Andycyca'
__copyright__ = 'Copyright 2020'
__credits__ = ['Andycyca']
__license__ = 'MPL'
__version__ = '2.0'
__maintainer__ = 'Andycyca'
__email__ = 'andycyca@gmail.com'
__status__ = 'Production?'


def char2bin(letter):
    '''Returns a naive, non-standard binary encoding of a single character. '''
    aleph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. '
    if letter in aleph:
        result = format(aleph.index(letter), '08b') + ' '
    else:
        result = format(64, '08b') + ' '
    return result


def str2bin(string, row=5):
    '''Returns a naive binary encoding of string.'''
    binaried = ''
    for letter in string:
        binaried += char2bin(letter)
    formatted = ''
    for idx, bit in enumerate(binaried):
        if idx % ((9 * row)) == 0 and idx > 0:
            formatted += '\n'
        formatted += bit
    return formatted
