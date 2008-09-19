#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


"""
This small application will build and draw a graph for a given finite definite automaton described
as a labelled transition system.

This is a very naive, probably useless, possibly incorrect, barely tested implementation. No
validation is ever performed. Take care or it will burn your house and kill your cat.
"""


# Module metadata
__authors__ = "Pedro Matiello"
__license__ = "MIT"


# Imports
import sys
sys.path.append('..')
import graph
sys.path.append('/usr/lib/graphviz/python/')
import gv


def load_automaton(filename):
	"""
	Read a automaton described as a labelled transition system and build the equivalent graph.
	
	@type  filename: string
	@param filename: Name of the file containing the LTS-described automaton.
	
	@rtype:  graph
	@return: Automaton's graph.
	"""
	gr = graph.digraph()
	infile = file(filename,'r')
	line = infile.readline()
	final = []
	while (line):
		line = line.replace("\n",'').split(' ')
		datatype = line[0]
		data = line[1:]
		if (datatype == 'Q'):
			# States
			for each in data:
				gr.add_node(each)
		if (datatype == 'A'):
			# Alphabet
			pass
		if (datatype == 'F'):
			# Final states
			final = final + data
		if (datatype == 's'):
			# Initial state
			gr.add_node('.',attrs=[('shape','point')])
			gr.add_edge('.',data[0])
		if (datatype == 't'):
			# Transitions
			if (gr.has_edge(data[1], data[2])):
				gr.set_edge_label(data[1], data[2], \
					gr.get_edge_label(data[1], data[2]) + ', ' + data[0])
			else:
				gr.add_edge(data[1], data[2], label=data[0])
		line = infile.readline()
	
	for node in gr:
		if (node in final and node != '.'):
			gr.add_node_attribute(node, ('shape','doublecircle'))
		elif (node != '.'):
			gr.add_node_attribute(node, ('shape','circle'))
	
	return gr, final


# Main
try:
	filename = sys.argv[1]
	gr, final = load_automaton(sys.argv[1])
	dot = gr.write(fmt='dot')
except IndexError:
	print "Syntax: %s filename" % sys.argv[0]
	sys.exit(1)
except IOError:
	print "Can't open file %s" % filename
	sys.exit(2)


# Print graph as PNG image
gvv = gv.readstring(dot)
gv.layout(gvv,'circo')
gv.render(gvv,'png',filename + '.png')
