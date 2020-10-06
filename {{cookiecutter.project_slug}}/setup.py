# -*- coding: utf-8 -*-
import sys

from setuptools import find_packages
from setuptools import setup

NAME = '{{cookiecutter.project}}'
VERSION = '{{cookiecutter.version}}'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ['jupyter', 'matplotlib', 'numpy', 'pandas', 'scipy']

setup(
    name=NAME,
    version=VERSION,
    description='{{cookiecutter.description}}',
    author_email='{{cookiecutter.author_email}}',
    url='',
    install_requires=REQUIRES,
    packages=find_packages()
)
