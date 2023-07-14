#!/usr/bin/env python
from setuptools import setup

VERSION = '0.1.0'
DESCRIPTION = "Fork of PyBloom: A Probabilistic data structure"
LONG_DESCRIPTION = """
Minor fork of pybloom to get it working in a modern Python enviornment.
pybloom is a Python implementation of the bloom filter probabilistic data
structure. The module also provides a Scalable Bloom Filter that allows a
bloom filter to grow without knowing the original set size.
"""

setup(name="pybloom3",
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      keywords=[
          'data structures', 'bloom filter', 'bloom', 'filter',
          'probabilistic', 'set'
      ],
      author="Jay Baird",
      author_email="jay.baird@me.com",
      maintainer="Richard Rogers",
      maintainer_email="richard@whylabs.ai",
      url="http://github.com/whylabs/whylogs-bloom/",
      license="MIT License",
      platforms=['any'],
      test_suite="pybloom.tests",
      zip_safe=True,
      install_requires=['bitarray>=0.3.4'],
      packages=['whylogs-bloom'])
