import os
import sys
import yaml


def yml_existence():

    """The function checks all the dirs where config may exist"""

    if os.path.isfile(os.path.expanduser("~/.repomator.yaml")):
        return os.path.abspath(os.path.expanduser("~/.repomator.yaml"))
    elif os.path.isfile("/etc/repomator.yaml"):
        return os.path.abspath("/etc/repomator.yaml")
    else:
        sys.exit("No configuration file found!")


def yml_parser():

    """The function parses yaml configuration file and returns its values for further usage"""

    with open(yml_existence(), 'r') as yamlconfig:
        doc = yaml.load(yamlconfig)

    resp = dict()
    resp["url"] = doc["bugtracker"]["url"]
    resp["login"] = doc["bugtracker"]["login"]
    resp["password"] = doc["bugtracker"]["password"]
    resp["comment"] = doc["general"]["comment"]

    return resp