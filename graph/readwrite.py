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

@sort: read, write, _read_xml, _write_xml
"""


# Module metadata
__authors__ = "Pedro Matiello"
__license__ = "MIT"


# Imports
from xml.dom.minidom import Document, parseString


# Stubs

def write(graph, fmt):
	"""
	Write the graph to a string. Depending of the output format, this string can be used by read() to rebuild the graph.
	
	@type  graph: graph
	@param graph: Graph.

	@type  fmt: string
	@param fmt: Output format. Possible formats are:
		1. 'xml' - XML (default)
		2. 'dot' - DOT Language (for GraphViz)

	@rtype:  string
	@return: String specifying the graph.
	"""
	if (fmt == None):
		fmt = 'xml'
	
	if (fmt == 'xml'):
		return _write_xml(graph)
	elif (fmt == 'dot'):
		return _write_dot(graph)
		

def read(graph, string, fmt):
	"""
	Read a graph from a string. Nodes and arrows specified in the input will be added to the current graph.
	
	@type  string: string
	@param string: Input string specifying a graph.

	@type  fmt: string
	@param fmt: Input format. Possible formats are:
		1. 'xml' - XML (default)
	"""
	if (fmt == None):
		fmt = 'xml'
	
	if (fmt == 'xml'):
		return _read_xml(graph, string)


# XML

def _write_xml(graph):
	"""
	Return a string specifying the given graph as a XML document.
	
	@type  graph: graph
	@param graph: Graph.

	@rtype:  string
	@return: String specifying the graph as a XML document.
	"""

	# Document root
	grxml = Document()
	grxmlr = grxml.createElement('graph')
	grxml.appendChild(grxmlr)

	# Each node...
	for each_node in graph.get_nodes():
		node = grxml.createElement('node')
		node.setAttribute('id',str(each_node))
		grxmlr.appendChild(node)

		# and its outgoing arrows
		for each_arrow in graph.get_node(each_node):
			arrow = grxml.createElement('arrow')
			arrow.setAttribute('to',str(each_arrow))
			arrow.setAttribute('wt',str(graph.get_arrow_weight(each_node, each_arrow)))
			node.appendChild(arrow)

	return grxml.toprettyxml()


def _read_xml(graph, string):
	"""
	Read a graph from a XML document. Nodes and arrows specified in the input will be added to the current graph.
	
	@type  graph: graph
	@param graph: Graph

	@type  string: string
	@param string: Input string in XML format specifying a graph.
	"""
	dom = parseString(string)
	for each_node in dom.getElementsByTagName("node"):
		graph.add_nodes([each_node.getAttribute('id')])
		for each_arrow in each_node.getElementsByTagName("arrow"):
			graph.add_arrow(each_node.getAttribute('id'), each_arrow.getAttribute('to'), wt=float(each_arrow.getAttribute('wt')))


# DOT Language

def _write_dot(graph):
	"""
	Return a string specifying the given graph in DOT Language (which can be used by GraphViz to generate a visualization of the given graph).
	
	@type  graph: graph
	@param graph: Graph.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""

	# Pre
	doc = ""
	edgemark = " -- "
	docstart = "graph graphname"
	
	# Check graph type
	for each_node in graph.get_nodes():
		for each_arrow in graph.get_node(each_node):
			if (not graph.has_edge(each_node, each_arrow)):
				return _write_dot_digraph(graph)
	return _write_dot_graph(graph)


def _write_dot_graph(graph):
	"""
	Return a string specifying the given graph in DOT Language.
	
	@type  graph: graph
	@param graph: Graph.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""

	# Start document
	doc = ""
	edgemark = " -- "
	doc = doc + "graph graphname" + "\n{\n"

	# Add nodes
	for each_node in graph.get_nodes():
		doc = doc + "\t" + each_node + "\n"
		# Add edges
		for each_arrow in graph.get_node(each_node):
			if (graph.has_edge(each_node, each_arrow) and (each_node < each_arrow)):
				doc = doc + "\t" + each_node + edgemark + each_arrow + "\n"
	# Finish
	doc = doc + "}"
	return doc


def _write_dot_digraph(graph):
	"""
	Return a string specifying the given digraph in DOT Language.
	
	@type  graph: graph
	@param graph: Graph.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""

	# Start document
	doc = ""
	edgemark = " -> "
	doc = doc + "digraph graphname" + "\n{\n"

	# Add nodes
	for each_node in graph.get_nodes():
		doc = doc + "\t" + each_node + "\n"
		# Add edges
		for each_arrow in graph.get_node(each_node):
			doc = doc + "\t" + each_node + edgemark + each_arrow + "\n"
	# Finish
	doc = doc + "}"
	return doc
