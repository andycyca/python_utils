# -*- coding: utf-8 -*-
"""
Naive Round Robin implementation for a list

@author: Andy
"""

__author__ = 'Andycyca'
__copyright__ = 'Copyright 2019'
__credits__ = ['Andycyca']
__license__ = 'MPL'
__version__ = '2.0'
__maintainer__ = 'Andycyca'
__email__ = 'andycyca@gmail.com'
__status__ = 'Production?'


from txt2list import txt2list


def run_roundrobin(my_list):
    '''
    Runs a naive Round Robin tournament using a text file for the team names.

    After every round the user will be prompted to determine the winner.
    '1' Means the left team wins, '2' means the right team wins, '3'
    means there's a draw.

    Naive scoring: 2 pts to the winner, 1 for each team if draw.

    Parameters
    ----------
    my_list : Path
        The path to a text file with all the teams that will participate

    Returns
    -------
    scores : list
        The scores after the tournament is complete. Sorted in
        descending order
    teams : list
        The names after the tournament is complete. Sorted in
        descending order to match the scores.

    '''
    teams = []
    scores = []
    count = 0
    ugly_list = txt2list(my_list)

    for game in ugly_list:
        teams.append(game)
        scores.append(0)

    total = (len(teams) * (len(teams) - 1)) / 2

    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            print("* * *\n")
            print("%s VERSUS %s" % (teams[i], teams[j]))
            point = int(input("choose one:  "))
            if point == 1:
                scores[i] += 2
                print("+2 pt to %s" % teams[i])
            elif point == 2:
                scores[j] += 2
                print("+2 pt to %s" % teams[j])
            elif point == 3:
                scores[i] += 1
                scores[j] += 1
                print("Draw, 1 pt to both games")
            count += 1
            print("%s of %s done" % (count, round(total)))
            print("* * *\n\n")

    return scores, teams

