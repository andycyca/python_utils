# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:01:31 2020

@author: Andycyca

Basic visualization and analysis for Everything2 nodes, using purely
public-data (i.e. no access to the database itself because I still don't
know how to do it).

Visualization assumes you have made a proper [Node Backup] and extract the
html files **and only html files** to a single directory that here we will
call 'p'

Requirements:

- Python 3.x (which should have os and re)
- matplotlib
- palettable
"""

__author__ = 'Andycyca'
__copyright__ = 'Copyright 2020'
__credits__ = ['Andycyca']
__license__ = 'MPL'
__version__ = '2.0'
__maintainer__ = 'Andycyca'
__email__ = 'andycyca@gmail.com'
__status__ = 'Alpha'

import os
from os.path import join, getsize
import re
import matplotlib.pyplot as plt
from palettable.tableau import Tableau_20 as my_cmap


def trim_extension(filename):
    '''
    Trims the html extension.
    '''
    return filename[:-5]


def get_title_and_type(filename):
    '''
    Returns (approximate) title and type of node.

    Assumes the filename is formatted like so:

        This is my node title (nodetype)

    If the filename cannot be parsed, it will return the strings
    "NONETYPE" and "unparseable"

    Parameters
    ----------
    filename : Path
         Path to a single file without extension.

    Returns
    -------
    TITLE
        String of the node title.
    TYPE
        String of the node type.

    '''
    regex = r"^(.+) \((.+)\)$"
    match = re.search(regex, filename)
    if match:
        return match.group(1), match.group(2)
    else:
        return "NONETYPE", "unparseable"


def get_node_data(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            name = trim_extension(filename)
            title, nodetype = get_title_and_type(name)
            node_data.append([title, nodetype, getsize(join(root, filename))])
            if nodetype not in node_count:
                node_count[nodetype] = 1
            else:
                node_count[nodetype] += 1
    # Minor sanitization
    if "unparseable" in node_count:
        del node_count['unparseable']

    if without_drafts:
        del node_count['draft']

    if without_logs:
        del node_count['log']


# Begin here
p = 'C:\\Users\\craze\\Documents\\Python\\e2'

# Set to hold raw data
node_count = {}
node_data = []
without_drafts = False
without_logs = False

# Process the whole thing
get_node_data(p)

# For easier counting
node_types = len(node_count)
total_nodes = len(node_data)

# Sort by number of nodes in descending order
sorted_list = sorted(node_count.items(), key=lambda kv: kv[1], reverse=True)

# Sort by node size (approximate)
node_data = sorted(node_data, key=lambda size: size[2], reverse=True)

# For visualization purposes
my_xticks = []
for idx, _ in enumerate(sorted_list):
    my_xticks.append(sorted_list[idx][0])

# Fig 1: all nodes, by type (includes drafts)
fig, ax = plt.subplots()
plt.title('Noding distribution for user')
ax.set_prop_cycle('color', my_cmap.mpl_colors)
for idx, name in enumerate(sorted_list):
    plt.bar(idx, sorted_list[idx][1])
plt.xticks(range(node_types), labels=my_xticks, rotation='vertical')
plt.xlabel('Node types')
plt.ylabel('Frequency (absolute)')
plt.savefig('nodesbytype.png')

# Fig 2: All node sizes
fig, ax = plt.subplots()
ax.set_yscale('log')
plt.title('Node sizes')
ax.set_prop_cycle('color', my_cmap.mpl_colors)
plt.scatter(range(total_nodes), [node_data[i][2] for i in range(total_nodes)],
            marker='.')
plt.xlabel('Node rating')
plt.ylabel('Size (bytes)')
plt.savefig('nodesbysize.png')
plt.show()
