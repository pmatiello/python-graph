#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import os

# Startup
appname = "python-graph"
appversion = "1.1.0"
docfolder = '/usr/share/doc/' + appname + '-' + appversion + '/'
docfiles = os.listdir('docs')
for i in xrange(len(docfiles)):
	docfiles[i] = 'docs/' + docfiles[i]

setup(
	name = appname,
	version = appversion,
	packages = ['graph'],
	data_files = [(docfolder, ['README','Changelog','COPYING']),
				(docfolder + 'docs/', docfiles),
				],

	# metadata
	author = "Pedro Matiello",
	author_email = "pmatiello@gmail.com",
	description = "A library for working with graphs in Python",
	license = "MIT",
	keywords = "python graph algorithms library",
	url = "http://code.google.com/p/python-graph/",
	classifiers = ["License :: OSI Approved :: MIT License","Topic :: Software Development :: Libraries :: Python Modules"],
	long_description = "python-graph is a library for working with graphs in Python. This software provides a suitable data structure for representing graphs and a whole set of important algorithms."
)

