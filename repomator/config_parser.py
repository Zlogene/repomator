import os
import sys
from termcolor import colored
import yaml


def yml_existence():

    """The function checks all the dirs where config may exist"""

    if os.path.isfile(os.path.expanduser("~/.repomator.yaml")):
        return os.path.abspath(os.path.expanduser("~/.repomator.yaml"))
    elif os.path.isfile("/etc/repomator/repomator.yaml"):
        return os.path.abspath("/etc/repomator/repomator.yaml")
    else:
        print(colored("No configuration file found!", "red"))
        sys.exit(1)


def yml_parser():

    """The function parses yaml configuration file and returns its values for further usage"""

    with open(yml_existence(), 'r') as yamlconfig:
        doc = yaml.safe_load(yamlconfig)

    resp = dict()
    resp["url"] = doc["bugtracker"]["url"]
    resp["login"] = doc["bugtracker"]["login"]
    resp["password"] = doc["bugtracker"]["password"]

    return resp
