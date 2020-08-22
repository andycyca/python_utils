# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:56:37 2020

@author: Andycyca

THIS FILE PART OF THE

    ****************************
    * COMBINATORIC SHITPOSTING *
    *            FOR           *
    *     MATHEMATICAL TEENS   *
    ****************************

PROJECT.

NOT INTENDED FOR SERIOUS USE.

I'M SERIOUS ABOUT THAT

FOR MORE INFORMATION, ASK ANDYCYCA

https://everything2.com/user/andycyca

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

print('''
      WELCOME TO THE UNOFFICIAL EVERYTHING2 PERSONALITY TEST
      
      have you ever noticed how nobody understands you?
      have you ever wondered why no one sees what you see?
      
      WORRY NO MORE
      
      THIS TEST HAS BEEN CAREFULLY CRAFTED TO ASSIGN YOU
      A PERSONALITY TYPE THAT UNIQUELY IDENTIFIES YOUR PERSON
      FROM AMONG
      
      2 ^ 100 = 1 267 650 600 228 229 401 496 703 205 376
      
      OTHER PEOPLE
      
                       **THAT'S RIGHT!**
      
     YOU CAN BE THE UNIQUE SNOWFLAKE IN AN OCEAN OF ICE (WHICH IS
     MORE LIKE A SNOWSTORM BUT YOU GET THE IDEA)
     
     =========================================
     | PLEASE NOTE                           |
     |                                       |
     | YOU NEED TO BE OVER 21 YEARS OLD      |
     | AND COMFORTABLE WITH SEXUAL QUESTIONS |
     | FOR MAXIMUM EFFECT                    |
     =========================================
      ''')

print('''
      PLEASE SELECT A NUMBER FROM 2--10 INCLUSIVE
      
      A LARGER NUMBER TAKES MORE TIME TO COMPLETE THE TEST
      BUT GIVES YOU A MORE ACCURATE RESULT
      AND YOU WANT TO SHOW HOW UNIQUE YOU ARE, RIGHT?
      ''')

n = int(input('SELECT A NUMBER:  '))
while n not in range(2,11):
    print('YOU DAFT PRICK')
    print('YOU DUMB COW')
    print('PLEASE DONT MAKE ME HURT MYSELF')
    n = int(input('SELECT A NUMBER:  '))
answers = []
totals = {"Y": 0, "N": 0}
mapping = {"Y": 1, "N": 0}
prompt = " ([Y]es / [N]o / [W]hat) >>> "
with open('personalitytest.txt', encoding='utf8') as f:
    line_total = sum(1 for _ in f)
qs = random.sample(range(line_total), k=n**2)

for idx, q in enumerate(qs):
    print("\n\t" + str(idx + 1) + " of " + str(n ** 2))
    question = linecache.getline('personalitytest.txt', q)
    a = input(question + prompt).upper()
    if a == 'W':
        a = random.choice(['Y', 'N'])
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
print('''
      ========================================================
      | Success! Your personality test results are saved as: |
      |     "mypersonalpersonalitytest.png"                  |
      ========================================================
      
      (Go read about personality tests and reductionism)
      ''')