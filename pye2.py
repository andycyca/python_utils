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

# %% Front matter
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
import argparse

# %% Parsing information

# Initiate the parser
parser = argparse.ArgumentParser()

# Define the program description
text = '''
Basic visualization and analysis for Everything2 nodes,
using purely public data'''


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is invalid")


# Initiate the parser with a description
parser = argparse.ArgumentParser(description=text)
parser.add_argument('path',
                    type=dir_path,
                    help='path to your html files')
parser.add_argument('-v', '--version',
                    help='show program version', action='store_true')
parser.add_argument('-d', '--drafts',
                          help='turn on drafts in visualization',
                          action='store_true')
parser.add_argument('-l', '--logs',
                          help='turn on logs in visualization',
                          action='store_true')
parser.add_argument('-u', '--username',
                    help='a username for display',
                    default='')
parser.add_argument('-o', '--output',
                    help='output directory')
args = parser.parse_args()

# %% Discrete main functions


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
    '''
    Generates data from files in 'path'

    Parameters
    ----------
    path : str
        Path to html files.

    Returns
    -------
    nodecount : dict
        A dict with node types and frequency count.
    nodedata : List
        List of arrays. Every entry has [node, type, size] information.

    '''
    nodecount = {}
    nodedata = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            name = trim_extension(filename)
            title, nodetype = get_title_and_type(name)
            nodedata.append([title, nodetype, getsize(join(root, filename))])
            if nodetype not in nodecount:
                nodecount[nodetype] = 1
            else:
                nodecount[nodetype] += 1
    # Minor sanitization
    if "unparseable" in nodecount:
        del nodecount['unparseable']

    if not args.drafts:
        del nodecount['draft']

    if not args.logs:
        del nodecount['log']

    return nodecount, nodedata


def create_graphs(sortedlist, totalnodes, nodecount, nodedata):
    # For visualization purposes
    my_xticks = []
    for idx, _ in enumerate(sortedlist):
        my_xticks.append(sortedlist[idx][0])

    # Fig 1: all nodes, by type (includes drafts)
    fig, ax = plt.subplots()
    if args.username:
        plt.title('Noding distribution for ' + args.username)
    else:
        plt.title('Noding distribution for user')
    ax.set_prop_cycle('color', my_cmap.mpl_colors)
    for idx, name in enumerate(sortedlist):
        plt.bar(idx, sortedlist[idx][1])
    plt.xticks(range(len(nodecount)), labels=my_xticks, rotation='vertical')
    plt.xlabel('Node types')
    plt.ylabel('Frequency (absolute)')
    plt.savefig('nodesbytype.png')

    # Fig 2: All node sizes
    fig, ax = plt.subplots()
    ax.set_yscale('log')
    if args.username:
        plt.title('Node sizes for ' + args.username)
    else:
        plt.title('Node sizes for user')
    ax.set_prop_cycle('color', my_cmap.mpl_colors)
    plt.scatter(range(totalnodes),
                [nodedata[i][2] for i in range(totalnodes)],
                marker='.')
    plt.xlabel('Node rating')
    plt.ylabel('Size (bytes)')
    plt.savefig('nodesbysize.png')
    plt.show()


# %% Main function
def main(p=args.path):

    if args.version:
        print('python visualization program for everything2, v.20200713')

    # Process the whole thing
    node_count, node_data = get_node_data(p)

    # For easier counting
    node_types = len(node_count)  # For future use
    total_nodes = len(node_data)

    # Sort by number of nodes in descending order
    sorted_list = sorted(node_count.items(),
                         key=lambda kv: kv[1], reverse=True)

    # Sort by node size (approximate)
    node_data = sorted(node_data, key=lambda size: size[2], reverse=True)

    create_graphs(sorted_list, total_nodes, node_count, node_data)


if __name__ == "__main__":
    main()
