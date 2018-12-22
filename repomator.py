#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The module aims to handle gentoo arch-specific processes automatically.
TODO:  rewrite it using appropriate bugzilla rest-api class"""

import argparse
import os
import re
import sys
from bugzilla import bugtracker


def check_existence(path):

    """The function performs basic binary-existence checks"""

    if not os.path.isfile(path):
        print("Can't find: {}. Please install appropriate packages!".format(path))
        sys.exit(1)


check_existence("/usr/bin/git")
check_existence("/usr/bin/repoman")
check_existence("/usr/bin/ekeyword")

"""The list  of currently supported Gentoo GNU/Linux architectures"""

arches_list = ['alpha', 'amd64', 'arm', 'arm64', 'hppa', 'ia64', 'm68k', 'ppc', 'ppc64', 's390', 'sh', 'sparc', 'x86',
               '~alpha', '~amd64', '~arm', '~arm64', '~hppa', '~ia64', '~m68k', '~mips', '~mips', '~ppc', '~ppc64',
               '~s390', '~sh', '~sparc', '~x86']

parser = argparse.ArgumentParser(description='Repomator script v1.0')
parser.add_argument('-a', '--arch', help='specify architecture', choices=arches_list, required=True)
parser.add_argument('-b', '--bug', type=int, help='specify bug number', required=True)
parser.add_argument('-l', '--list', help='specify packages list', required=True)
parser.add_argument('-r', '--repo', help='specify repo path', required=True)

args = parser.parse_args()

packages = []

with open(args.list, 'r') as f:

    for line in f:

        package_category = re.search(r'((?<==)\w+-\w+|\w+-\w+|\w+)', line).group(0)
        package_name = re.search(r'(?<=/).*(?=-\d)|(\w+_\w+)', line).group(0)
        package_version = re.search(r'(?<=-)\d.*?(?=\s)', line).group(0)

        packages.append({
            "category": package_category,
            "name": package_name,
            "version": package_version
        })

for package in packages:

        os.chdir(os.path.join(args.repo, package["category"], package["name"]))
        os.system("/usr/bin/ekeyword {} {}-{}.ebuild".format(args.arch, package["name"], package["version"]))

for package in packages:

    os.chdir(os.path.join(args.repo, package["category"], package["name"]))
    if args.arch[:1] is not "~":
            os.system("/usr/bin/repoman ci -m \"{}/{}: {} stable wrt bug #{}\""
                      .format(package["category"], package["name"], args.arch, args.bug))
    else:
            os.system("/usr/bin/repoman ci -m \"{}/{}: Add {} keyword wrt bug #{}\""
                      .format(package["category"], package["name"], args.arch, args.bug))

bugtracker(args.arch, args.bug)
