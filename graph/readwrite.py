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
		for each_arrow in graph.get_neighbors(each_node):
			arrow = grxml.createElement('arrow')
			arrow.setAttribute('to',str(each_arrow))
			arrow.setAttribute('wt',str(graph.get_arrow_weight(each_node, each_arrow)))
			arrow.setAttribute('label',str(graph.get_arrow_label(each_node, each_arrow)))
			node.appendChild(arrow)

	return grxml.toprettyxml()


def write_xml_hypergraph(hypergraph):
	"""
	Return a string specifying the given hypergraph as a XML document.
	
	@type  hypergraph: hypergraph
	@param hypergraph: Hypergraph.

	@rtype:  string
	@return: String specifying the graph as a XML document.
	"""

	# Document root
	grxml = Document()
	grxmlr = grxml.createElement('hypergraph')
	grxml.appendChild(grxmlr)

	# Each node...
	nodes = hypergraph.get_nodes()
	hyperedges = hypergraph.get_hyperedges()
	for each_node in (nodes + hyperedges):
		if (each_node in nodes):
			node = grxml.createElement('node')
		else:
			node = grxml.createElement('hyperedge')
		node.setAttribute('id',str(each_node))
		grxmlr.appendChild(node)

		# and its outgoing arrows
		for each_arrow in hypergraph.get_links(each_node):
			arrow = grxml.createElement('link')
			arrow.setAttribute('to',str(each_arrow))
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
		graph.add_node(each_node.getAttribute('id'))
		for each_arrow in each_node.getElementsByTagName("arrow"):
			graph.add_arrow(each_node.getAttribute('id'), each_arrow.getAttribute('to'), wt=float(each_arrow.getAttribute('wt')), label=each_arrow.getAttribute('wt'))


def read_xml_hypergraph(hypergraph, string):
	"""
	Read a graph from a XML document. Nodes and hyperedges specified in the input will be added to the current graph.
	
	@type  hypergraph: hypergraph
	@param hypergraph: Hypergraph

	@type  string: string
	@param string: Input string in XML format specifying a graph.
	"""
	dom = parseString(string)
	for each_node in dom.getElementsByTagName("node"):
		hypergraph.add_nodes(each_node.getAttribute('id'))
	for each_node in dom.getElementsByTagName("hyperedge"):
		hypergraph.add_hyperedges(each_node.getAttribute('id'))
	dom = parseString(string)
	for each_node in dom.getElementsByTagName("node"):
		for each_arrow in each_node.getElementsByTagName("link"):
			hypergraph.link(each_node.getAttribute('id'), each_arrow.getAttribute('to'))


# DOT Language

def write_dot(graph, wt=False):
	"""
	Return a string specifying the given graph in DOT Language (which can be used by GraphViz to generate a visualization of the given graph).
	
	@type  graph: graph
	@param graph: Graph.
	
	@type  wt: boolean
	@param wt: Whether edges/arrows should be wt with its weight.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""
	# Check graph type
	for each_node in graph.get_nodes():
		for each_arrow in graph.get_neighbors(each_node):
			if (not graph.has_edge(each_node, each_arrow) or graph.get_arrow_weight(each_node, each_arrow) != graph.get_arrow_weight(each_arrow, each_node)):
				return _write_dot_digraph(graph, wt)
	return _write_dot_graph(graph, wt)


def _write_dot_graph(graph, wt):
	"""
	Return a string specifying the given graph in DOT Language.
	
	@type  graph: graph
	@param graph: Graph.

	@type  wt: boolean
	@param wt: Whether edges should be wt with its weight.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""
	# Start document
	doc = ""
	doc = doc + "graph graphname" + "\n{\n"
	label = "\n"

	# Add nodes
	for each_node in graph.get_nodes():
		doc = doc + "\t\"%s\"\n" % str(each_node)
		# Add edges
		for each_arrow in graph.get_neighbors(each_node):
			if (graph.has_edge(each_node, each_arrow) and (each_node < each_arrow)):
				labelvars = {
					'label' : graph.get_arrow_label(each_node, each_arrow),
					'weigth': graph.get_arrow_weight(each_node, each_arrow)
				}
				if (wt):
					label = '[label="%(label)s (%(weigth)d)"]\n' % labelvars
				else:
					label = '[label="%(label)s"]\n' % labelvars
				arrowvars = {
					'from' : str(each_node),
					'to' : str(each_arrow)
				}
				doc = doc + '\t"%(from)s" -- "%(to)s" ' % arrowvars + label
	# Finish
	doc = doc + "}"
	return doc


def _write_dot_digraph(graph, wt):
	"""
	Return a string specifying the given digraph in DOT Language.
	
	@type  graph: graph
	@param graph: Graph.

	@type  wt: boolean
	@param wt: Whether arrows should be wt with its weight.

	@rtype:  string
	@return: String specifying the graph in DOT Language.
	"""
	# Start document
	doc = ""
	doc = doc + "digraph graphname" + "\n{\n"
	label = "\n"

	# Add nodes
	for each_node in graph.get_nodes():
		doc = doc + "\t\"%s\"\n" % str(each_node)
		# Add arrows
		for each_arrow in graph.get_neighbors(each_node):
			labelvars = {
				'label' : graph.get_arrow_label(each_node, each_arrow),
				'weigth': graph.get_arrow_weight(each_node, each_arrow)
			}
			if (wt):
				label = '[label="%(label)s (%(weigth)d)"]\n' % labelvars
			else:
				label = '[label="%(label)s"]\n' % labelvars
			arrowvars = {
				'from' : str(each_node),
				'to' : str(each_arrow)
			}
			doc = doc + '\t"%(from)s" -> "%(to)s" ' % arrowvars + label
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


	# Add hyperedges
	color = ''
	for each_hyperedge in hypergraph.get_hyperedges():
		colortable[each_hyperedge] = colors[colorcount % len(colors)]
		colorcount = colorcount + 1
		if (coloured):
			color = " color=%s" % colortable[each_hyperedge]
		vars = {
			'hyperedge' : str(each_hyperedge),
			'color' : color
		}
		doc = doc + '\t"%(hyperedge)s" [shape=point %(color)s]\n' % vars
	
	color = "\n"
	# Add nodes and links
	for each_node in hypergraph.get_nodes():
		doc = doc + "\t\"%s\"\n" % str(each_node)
		for each_link in hypergraph.get_links(each_node):
			if (coloured):
				color = " [color=%s]\n" % colortable[each_link]
			linkvars = {
				'node' : str(each_node),
				'hyperedge' : str(each_link)
			}
			doc = doc + '\t %(node)s -- %(hyperedge)s' % linkvars + color

	doc = doc + "}"
	print doc
	return doc
