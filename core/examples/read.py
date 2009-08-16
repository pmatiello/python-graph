#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import sys
sys.path.append('..')
import pygraph

inputfile = file('graph.xml','r')
string = inputfile.read()
inputfile.close()

gr = pygraph.readwrite.markup.read(string)
print pygraph.readwrite.markup.write(gr)
