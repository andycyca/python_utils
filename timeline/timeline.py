# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:07:35 2020

@author: Andycyca
"""

__author__ = 'Andycyca'
__copyright__ = 'Copyright 2020'
__credits__ = ['Andycyca']
__license__ = 'MPL'
__version__ = '2.0'
__maintainer__ = 'Andycyca'
__email__ = 'andycyca@gmail.com'
__status__ = 'Alpha?'

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from palettable.cartocolors.sequential import SunsetDark_5_r as my_cmap

def simple_timeline(years, w=1000, h = 250, my_colors=my_cmap.mpl_colors,
                    save_image=True):
    '''
    Create an image timeline using years as data.

    Parameters
    ----------
    years : list of ints
        List or array with "transition" years. It's important to include the
        "start" and "end" of the timeline
    w : int, optional
        Width of the output image in pixels. The default is 1000.
    h : int, optional
        Height of the output image in pixels. The default is 250.
    my_colors : list of RGB tuples, optional
        Colors as a list of RGB tuples in the range 0-1 as used 
        by matplotlib. The default is the palettable colormap called
        cartocolors.sequential.SunsetDark_5_r
    save_image : bool. The default is True
        Whether to save the image as a png file.

    Returns
    -------
    im : numpy array
        Timeline image, as a numpy array.

    '''
    years.sort()
    n_colors = len(my_cmap.mpl_colors)    

    # Use this to normalize all dates to out_width
    norm = []
    line_width = years[-1] - years[0]
    width_factor = w / line_width
    for n in range(len(years)):
        norm.append(int((years[n] - years[0]) * width_factor))

    # Raw image array
    im = np.zeros((h, w, 3))

    for n in range(len(norm) - 1):
        sub_start = int(norm[n])
        sub_end = int((norm[n] + norm[n + 1]))
        im[:,sub_start:sub_end] = my_colors[n % n_colors]
    
    plt.imshow(im)
    if save_image:
        plt.imsave("timeline_raw.png", im)
    
    return im

# TODO: create documentation
# TODO: Test cases
def timeline_from_csv(filename, title="Mi línea del tiempo", legend=True):
    df = pd.read_csv(filename, sep=',', dtype={'group_name':str,
                                            'group_order':np.uint,
                                            'name':str,
                                            'start':np.int,
                                            'stop':np.int},
                     encoding='utf8')
    my_yticks = []
    my_ylabels = []
    fig, ax = plt.subplots(dpi=100)
    ax.set_title(title)
    for index, data in df.iterrows():
        ax.barh(y = data['group_order'],
                width = data['stop'] - data['start'],
                left = data['start'],
                edgecolor = 'k',
                label = data['name']
                )
        if data['group_order'] not in my_yticks:
            my_yticks.append(data['group_order'])
            my_ylabels.append(data['group_name'])
    ax.set_yticks(my_yticks)
    ax.set_yticklabels(my_ylabels)
    if legend:
        fig.legend()
    fig.show()
    fig.savefig("timeline_multi")
                
# TODO: Clean xticks
# TODO: Create documentation
def simple_timeline_fig(years, title="Mi línea de tiempo",my_colors=my_cmap.mpl_colors, legend=False):
    n_series = len(years)
    fig, ax = plt.subplots(dpi=100)
    ax.set_title(title)
    all_years = []
    for idx, series in enumerate(years):
        series.sort()
        widths = np.diff(series)
        ax.barh(y=idx, width=widths, left=series[:-1], color=my_colors,
                edgecolor='k', label=str(series))
        for y in series:
            all_years.append(y)
    all_years.sort()
    ax.set_yticks([])
    # ax.set_xticks([])
    ax.set_xticks(all_years)
    ax.set_xticklabels(all_years, rotation=45)
    if legend:
        fig.legend()
    fig.show()
    fig.savefig("timeline_fig")

'''
Example data:

y = [0, 250, 500, 750, 1000]
c = [(1.0, 0.0, 0.0),
     (0.0, 0.0 ,1.0),
     (0.0, 1.0, 0.0),
     (0.5, 0.5, 0.5),
     (0.7, 0.7, 0.7)]
simple_timeline(y, w=250, h=250, my_colors=c)
'''

# User-defined "transition" years
my_years = [[200, 450, 750, 1230],
            [-850, -100, -50, 150, 800]]

simple_timeline_fig(my_years)
timeline_from_csv('years.csv', legend=False)
