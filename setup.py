#python setup.py install

from setuptools import setup, find_packages
from typing import List

setup(
name='sensor',
version="0.0.1",
author='Sangam',
author_email="sangamsrivastav2002@gmail.com",
packages=find_packages(),
install_requires = ['pymongo']
)