#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import sys
sys.path.append('..')
import graph

gr = graph.graph()

inputfile = file('graph.xml','r')
string = inputfile.read()
inputfile.close()

gr.read(string)
print gr
