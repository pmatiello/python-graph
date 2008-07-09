#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = "python-graph",
    version = "0.75",
	packages = ['graph'],

    # metadata for upload to PyPI
    author = "Pedro Matiello",
    author_email = "pmatiello@gmail.com",
    description = "A library for working with graphs in Python",
    license = "MIT",
    keywords = "python graph algorithms library",
    url = "http://code.google.com/p/python-graph/",
    classifiers = ["License :: OSI Approved :: MIT License","Topic :: Software Development :: Libraries :: Python Modules"],
	long_description = "python-graph is a library for working with graphs in Python. This software provides a suitable data structure for representing graphs and a whole set of important algorithms."
)

