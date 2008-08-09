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

@sort: read_xml, write_xml, write_dot, write_dot_hypergraph
"""


# Module metadata
__authors__ = "Pedro Matiello"
__license__ = "MIT"


# Imports
from xml.dom.minidom import Document, parseString


# Values
colors = ['aquamarine4', 'blue4', 'brown4', 'cornflowerblue', 'cyan4',
			'darkgreen', 'darkorange3', 'darkorchid4', 'darkseagreen4', 'darkslategray',
			'deeppink4', 'deepskyblue4', 'firebrick3', 'hotpink3', 'indianred3',
			'indigo', 'lightblue4', 'lightseagreen', 'lightskyblue4', 'magenta4',
			'maroon', 'palevioletred3', 'steelblue', 'violetred3']


# XML

def write_xml(graph):
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
		for each_arrow in graph.get_edges(each_node):
			arrow = grxml.createElement('arrow')
			arrow.setAttribute('to',str(each_arrow))
			arrow.setAttribute('wt',str(graph.get_arrow_weight(each_node, each_arrow)))
			node.appendChild(arrow)

	return grxml.toprettyxml()


def read_xml(graph, string):
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

def write_dot(graph, labeled=False):
	"""
	Return a string specifying the given graph in DOT Language (which can be used by GraphViz to generate a visualization of the given graph).
	
	@type  graph: graph
	@param graph: Graph.
	
	@type  labeled: boolean
	@param labeled: Whether edges/arrows should be labeled with its weight.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""
	# Check graph type
	for each_node in graph.get_nodes():
		for each_arrow in graph.get_edges(each_node):
			if (not graph.has_edge(each_node, each_arrow)):
				return _write_dot_digraph(graph, labeled)
	return _write_dot_graph(graph, labeled)


def _write_dot_graph(graph, labeled):
	"""
	Return a string specifying the given graph in DOT Language.
	
	@type  graph: graph
	@param graph: Graph.

	@type  labeled: boolean
	@param labeled: Whether edges should be labeled with its weight.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""
	# Start document
	doc = ""
	doc = doc + "graph graphname" + "\n{\n"
	label = "\n"

	# Add nodes
	for each_node in graph.get_nodes():
		doc = doc + "\t" + str(each_node) + "\n"
		# Add edges
		for each_arrow in graph.get_edges(each_node):
			if (graph.has_edge(each_node, each_arrow) and (each_node < each_arrow)):
				if (labeled):
					label = " [label= " + str(graph.get_arrow_weight(each_node, each_arrow)) + "]\n"
				doc = doc + "\t" + str(each_node) + " -- " + str(each_arrow) + label
	# Finish
	doc = doc + "}"
	return doc


def _write_dot_digraph(graph, labeled):
	"""
	Return a string specifying the given digraph in DOT Language.
	
	@type  graph: graph
	@param graph: Graph.

	@type  labeled: boolean
	@param labeled: Whether arrows should be labeled with its weight.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""
	# Start document
	doc = ""
	doc = doc + "digraph graphname" + "\n{\n"
	label = "\n"

	# Add nodes
	for each_node in graph.get_nodes():
		doc = doc + "\t" + str(each_node) + "\n"
		# Add edges
		for each_arrow in graph.get_edges(each_node):
			if (labeled):
				label = " [label= " + str(graph.get_arrow_weight(each_node, each_arrow)) + "]\n"
			doc = doc + "\t" + str(each_node) + " -> " + str(each_arrow) + label
	# Finish
	doc = doc + "}"
	return doc


def write_dot_hypergraph(hypergraph, coloured=False):
	"""
	Return a string specifying the given hypergraph in DOT Language.
	
	@type  hypergraph: hypergraph
	@param hypergraph: Hypergraph.
	
	@type  coloured: boolean
	@param coloured: Whether hyperedges should be coloured.

	@rtype:  string
	@return: String specifying the hypergraph in DOT Language.
	"""
	# Start document
	doc = ""
	doc = doc + "graph graphname" + "\n{\n"
	colortable = {}
	colorcount = 0


	# Add nodes
	color = ''
	for each_hyperedge in hypergraph.get_hyperedges():
		colortable[each_hyperedge] = colors[colorcount % len(colors)]
		colorcount = colorcount + 1
		if (coloured):
			color = " color=" + colortable[each_hyperedge]
		doc = doc + "\t" + str(each_hyperedge) + " [" + "shape=point" + color + "]\n"
	
	color = "\n"
	for each_node in hypergraph.get_nodes():
		for each_link in hypergraph.get_links(each_node):
			if (coloured):
				color = " [color=" + colortable[each_link] + "]\n"
			doc = doc + "\t" + str(each_node) + " -- " + str(each_link) + color

	doc = doc + "}"
	return doc
