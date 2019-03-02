"""The module handles all bugzilla needs"""

from bs4 import BeautifulSoup
import bugzilla
import requests
import sys
from repomator.config_parser import yml_parser
from termcolor import colored


def list_handler(bug):

    """The function downloads a package list straight from bugzilla"""

    config = yml_parser()

    resp = requests.get("{}/{}".format(config["url"], bug)).text
    soup = BeautifulSoup(resp, "html.parser")
    mydivs = soup.find("div", class_="uneditable_textarea").text

    if not mydivs:
        print(colored("Given bug has no atoms to keyword or stabilize!", "text"))
        sys.exit(1)

    with open("/tmp/{}-stablereq".format(bug), "w") as f:
        f.write(mydivs)

    return f.name


def bugtracker(arch, bug):

    """The function handles all the web requests using requests library"""

    config = yml_parser()

    bz = bugzilla.Bugzilla(config["url"])
    bz.login(config["login"], config["password"])

    if arch[0] is "~":
        arch = arch[1:]

        update = bz.build_update(
            cc_remove="{}@gentoo.org".format(arch),
            comment="~{} keyworded".format(arch))

        bz.update_bugs(bug, update)

    else:

        update = bz.build_update(
            cc_remove="{}@gentoo.org".format(arch),
            comment="{} stable".format(arch))

        bz.update_bugs(bug, update)

    print(colored("Posted comment to {}/{}".format(config["url"], bug), "green"))
