from setuptools import setup
from setuptools import find_packages

setup(
    name='repomator',
    version='2.0',
    url='https://github.com/Zlogene/repomator',
    license='Apache-2.0',
    packages=find_packages(),
    scripts=["bin/repomator"],
    author='Mikle Kolyada',
    author_email='zlogene@gentoo.org',
    description='Gentoo GNU/Linux branches tooling',

    data_files=[('/etc/repomator', ['data/repomator.yaml'])],

    install_requires=[
        'beautifulsoup4 >= 4.5.1',
        'requests >= 2.18.4',
        'pyyaml >= 3.13'
    ]
)
