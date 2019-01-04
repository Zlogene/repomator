"""The module handles all bugzilla needs"""

from bs4 import BeautifulSoup
import json
import requests
from config_parser import yml_parser


def list_handler(bug):

    """The function downloads a package list straight from bugzilla"""

    config = yml_parser()

    resp = requests.get("{}/{}".format(config["url"], bug)).text
    soup = BeautifulSoup(resp, "html.parser")
    mydivs = soup.find("div", class_="uneditable_textarea").text

    with open("/tmp/{}-srablereq".format(bug), "r+") as f:
        f.write(mydivs)

    return f.name


def bugtracker(arch, bug):

    """The function handles all the web requests using requests library"""

    if arch[0] is "~":
        arch = arch[1:]

    config = yml_parser()

    comment_url = "{}/rest/bug/{}/comment".format(config["url"], bug)

    comment_data = json.dumps({"comment": "{} {}".format(arch, config["comment"])})

    auth = requests.get("{}/rest/login?login={}&password={}".format(config["url"], config["login"], config["password"]))

    token = json.loads(auth.text)["token"]

    requests.post(comment_url + "?token={}".format(token), data=comment_data)
