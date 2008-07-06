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
Functions for reading and writing graphs.
"""


# Module metadata
__authors__ = "Pedro Matiello"
__license__ = "MIT"


# Imports
from xml.dom.minidom import Document


# Stubs

def write(graph, fmt):
	"""
	Write the graph to a string. Depending of the output format, this string can be used by read() to rebuild the graph.
	
	@type  graph: graph
	@param graph: Graph.

	@type  fmt: string
	@param fmt: Output format.

	@rtype:  string
	@return: String representing the graph.
	"""
	if (fmt == None):
		fmt = 'xml'
	
	if (fmt == 'xml'):
		return _write_xml(graph)
		

def read(graph, fmt):
	pass


# python-graph

def _write_xml(graph):
	grxml = Document()
	grxmlr = grxml.createElement('graph')
	grxml.appendChild(grxmlr)
	for each_node in graph.get_nodes():
		node = grxml.createElement('node')
		node.setAttribute('id',str(each_node))
		grxmlr.appendChild(node)
		for each_arrow in graph.get_node(each_node):
			arrow = grxml.createElement('arrow')
			arrow.setAttribute('to',str(each_arrow))
			node.appendChild(arrow)
	return grxml.toprettyxml()
