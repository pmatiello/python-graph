#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import sys
sys.path.append('..')
from pygraph.readwrite.markup import read, write

inputfile = file('graph.xml','r')
string = inputfile.read()
inputfile.close()

gr = read(string)
print write(gr)
