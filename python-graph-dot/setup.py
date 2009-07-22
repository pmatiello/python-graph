#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import logging

try:
    from setuptools import setup, find_packages
except ImportError, ie:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

# Startup
appname = "python-graph-dot"
appversion = open("../version.txt").read()

setup(
        name = appname,
        version = appversion,
        namespace_packages = ['pygraph' ],
        packages = ['pygraph', ],
        install_requires = ['pydot', 'python-graph-core==%s' % appversion ],
        author = "Pedro Matiello",
        author_email = "pmatiello@gmail.com",
        description = "DOT support for python-graph",
        license = "MIT",
        keywords = "python graphs hypergraphs networks library algorithms",
        url = "http://code.google.com/p/python-graph/",
        classifiers = ["License :: OSI Approved :: MIT License","Topic :: Software Development :: Libraries :: Python Modules"],
        long_description = "python-graph is a library for working with graphs in Python. This software provides a suitable data structure for representing graphs and a whole set of important algorithms.",
)
