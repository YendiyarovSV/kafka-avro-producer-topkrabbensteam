

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


packages=find_packages(exclude=[])

for i in packages:
    print(i)
