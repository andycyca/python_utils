# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:56:37 2020

@author: Andycyca
"""

__author__ = 'Andycyca'
__copyright__ = 'Copyright 2020'
__credits__ = ['Andycyca']
__license__ = 'MPL'
__version__ = '2.0'
__maintainer__ = 'Andycyca'
__email__ = 'andycyca@gmail.com'
__status__ = 'Alpha'

import numpy as np
import matplotlib.pyplot as plt
from palettable.colorbrewer.diverging import RdGy_5 as my_cmap
import random
import linecache

n = 4
answers = []
totals = {"Y": 0, "W": 0, "N": 0}
mapping = {"Y": 1, "W": 0.5, "N": 0}
prompt = " ([Y]es / [N]o / [W]hat) >>> "
with open('personalitytest.txt', encoding='utf8') as f:
    line_total = sum(1 for _ in f)
qs = random.sample(range(line_total), k=n**2)

for idx, q in enumerate(qs):
    print("\n\t" + str(idx + 1) + " of " + str(n ** 2))
    question = linecache.getline('personalitytest.txt', q)
    a = input(question + prompt).upper()
    while a not in totals:
        print("You silly goose! Please choose 'Yes' or 'No'")
        a = input(question + prompt).upper()
    totals[a] += 1
    answers.append(mapping[a])

'''
with open('personalitytest.txt', encoding='utf8') as f:
    for line in f.readlines():
        a = input(str(line) + " (Y/N) >>> ").upper()
        while a not in totals:
            print("You silly goose! Please choose 'Yes' or 'No'")
            a = input(q + " (Y/N) >>> ").upper()
        totals[a] += 1
        answers.append(mapping[a])
'''

img = np.asarray(answers[:n**2]).reshape((n, n))
plt.figure(figsize=(10, 10), dpi=100)
plt.set_cmap(my_cmap.mpl_colormap)
plt.title('Your very own personalized personality\nfor a special person like yourself')
plt.xlabel('')
plt.ylabel('')
plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.savefig('mypersonalpersonalitytest.png', dpi='figure')
