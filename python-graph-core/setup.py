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
appname = "python-graph-tests"
appversion = open("../version.txt").read()

# Extra files
if (os.name == 'posix'):    # Files to be installed/packaged on Unix-like systems
    datadir = 'share/doc/'+appname+'-'+appversion
    datafiles = ['../README', '../COPYING', '../Changelog']
    docsdir = datadir + '/docs'
    docsfiles = []
    try:
        # Uncomment the line bellow if you want bdist_rpm to include the docs
        os.system('make docs')
        dirlisting = os.listdir('docs/')
    except:
        print "Documentation isn't present and will not be installed/packaged."
        dirlisting = []
    for each in dirlisting:
        docsfiles.append('docs/'+each)
else:    # Other systems
    datadir = ''
    datafiles = []
    docsdir = ''
    docsfiles = []

setup(
        name = appname,
        version = appversion,
        data_files = [(docsdir,docsfiles),
                       (datadir,datafiles)],
        author = "Pedro Matiello",
        author_email = "pmatiello@gmail.com",
        description = "A library for working with graphs in Python",
        license = "MIT",
        keywords = "python graphs hypergraphs networks library algorithms",
        url = "http://code.google.com/p/python-graph/",
        classifiers = ["License :: OSI Approved :: MIT License","Topic :: Software Development :: Libraries :: Python Modules"],
        long_description = "python-graph is a library for working with graphs in Python. This software provides a suitable data structure for representing graphs and a whole set of important algorithms.",
)
