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
appname = "python-graph"
appversion = "1.6.1"

setup(
        name = "%s_dot" % appname,
        version = appversion,
        namespace_packages = ["pygraph"],
        packages = ['pygraph'],
        install_requires = ['pydot', '%s==%s' % (appname, appversion) ],
        author = "Pedro Matiello",
        author_email = "pmatiello@gmail.com",
        description = "DOT extensions for %s" % appname,
        license = "MIT",
        keywords = "python graphs hypergraphs networks library algorithms",
        url = "http://code.google.com/p/python-graph/",
        classifiers = ["License :: OSI Approved :: MIT License","Topic :: Software Development :: Libraries :: Python Modules"],
        long_description = "python-graph is a library for working with graphs in Python. This software provides a suitable data structure for representing graphs and a whole set of important algorithms.",
)