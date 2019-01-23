"""The module handles all bugzilla needs"""

from bs4 import BeautifulSoup
import json
import requests
from repomator.config_parser import yml_parser


def list_handler(bug):

    """The function downloads a package list straight from bugzilla"""

    config = yml_parser()

    resp = requests.get("{}/{}".format(config["url"], bug)).text
    soup = BeautifulSoup(resp, "html.parser")
    mydivs = soup.find("div", class_="uneditable_textarea").text

    with open("/tmp/{}-srablereq".format(bug), "w") as f:
        f.write(mydivs)

    return f.name


def bugtracker(arch, bug):

    """The function handles all the web requests using requests library"""

    config = yml_parser()

    comment_url = "{}/rest/bug/{}/comment".format(config["url"], bug)

    auth = requests.get("{}/rest/login?login={}&password={}".format(config["url"], config["login"], config["password"]))

    token = json.loads(auth.text)["token"]

    if arch.startswith("~"):
        requests.post(comment_url + "?token={}".format(token), data={"comment": "{} keyworded".format(arch)})
    else:
        requests.post(comment_url + "?token={}".format(token), data={"comment": "{} stable".format(arch)})
