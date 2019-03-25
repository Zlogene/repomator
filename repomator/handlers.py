import os
import sys
from itertools import groupby
from termcolor import colored


def check_existence(path):

    """The function performs basic binary-existence checks"""

    if not os.path.isfile(path):
        print(colored("Can't find: {}. Please install appropriate packages!", "red".format(path)))
        sys.exit(1)


def uniq(data):

    """In case we have multiple (sorted) versions of a single package in a list
        we want to only keep the one appearance of the package in the list
        to avoid running repoman multiple times (it takes all the changes in the single commit)"""

    for _, group in groupby(data, lambda d: (d['category'], d['name'])):
        yield list(group)[0]

