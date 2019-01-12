# repomator

This script is designed to handle gentoo keywording and stabilization lists work.
It uses bugzilla REST api rather than `xmlrpc` which is marked 
[obsolete](https://bugzilla.readthedocs.io/en/latest/integrating/apis.html#api-list) by bugzilla developers.
The work is still in progress so the script will recive major updates later, to expand its possibilities.

# requirements

The script requires [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/), [pyyaml](http://pyyaml.org/wiki/PyYAML) and [requests](http://docs.python-requests.org/en/master/) 
modules  to be installed.

# usage

Type `repomator -h` for more info. Your `repomator.yaml` config file should be edited and placed either in `/etc` or in `$HOME`
