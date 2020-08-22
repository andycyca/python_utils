# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:46:23 2020

@author: Andycyca
"""

__author__ = 'Andycyca'
__copyright__ = 'Copyright Fri Aug 21 12:46:23 2020, {project_name}'
__credits__ = ['Andycyca']
__license__ = 'MPL'
__version__ = '2.0'
__maintainer__ = 'Andycyca'
__email__ = 'andycyca@gmail.com'
__status__ = 'Production?'

import matplotlib.pyplot as plt
import numpy as np

def generate_positions(n):
    i = 0
    while True:
        yield n-i, i
        i += 1

def update_pixels(array, pos):
    if array[pos[0], pos[1]] == 1:
        array[pos[0] + 1, pos[1]] += 1
        array[pos[0], pos[1] + 1] += 1
    else:
        array[pos[0], pos[1]] = 0

base = 750
table = np.zeros((base, base))
table[0, 0] = 1
cm = 'RdYlGn'

for gen in range(base - 1):
    series = generate_positions(gen)
    for _ in range(gen + 1):
        update_pixels(table, next(series))
        # print(next(series))

sierpinski = table % 2
plt.figure()
plt.imshow(table, cmap=cm)
plt.show()
plt.imsave("sierpinski.png", sierpinski, cmap=cm)