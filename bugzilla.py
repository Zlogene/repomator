"""The module handles all bugzilla needs"""

import json
#from pprint import pprint
import os
import yaml
import requests


def yml_existence():

    """The function checks all the dirs where config may exist"""

    if os.path.isfile(os.path.expanduser("~/.repomator.yaml")):
        return os.path.abspath(os.path.expanduser("~/.repomator.yaml"))
    elif os.path.isfile("/etc/repomator.yaml"):
        return os.path.abspath("/etc/repomator.yaml")
    else:
        print("File Not Found")


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


def bugtracker(arch, bug, email):

    """The function handles all the web requests using requests library"""

    if arch[0] is "~":
        arch = arch[1:]

    config = yml_parser()

    comment_url = '{}/rest/bug/{}/comment'.format(config["url"], bug)
 #   cc_url = '{}/rest/bug/{}'.format(config["url"], bug)

    comment_data = json.dumps({"comment": "{} {}".format(arch, config["comment"])})
#  cc_change = json.dumps({"cc": {"remove": [{}].format(email)}})

    auth = requests.get('{}/rest/login?login={}&password={}'.format(config["url"], config["login"], config["password"]))

    token = json.loads(auth.text)["token"]

    requests.post(comment_url + "?token={}".format(token), data=comment_data)

#    abra = requests.put(cc_url + "?token={}".format(token), data=cc_change)

#    pprint(abra.text)
