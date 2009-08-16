# Copyright (c) 2007-2009 Pedro Matiello <pmatiello@gmail.com>
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
Functions for reading and writing graphs in a XML markup.

@sort: read, write, read_hypergraph, write_hypergraph
"""


# Imports
from pygraph.classes.Digraph import digraph
from pygraph.classes.Graph import graph
from xml.dom.minidom import Document, parseString
from pygraph.classes.Exceptions import InvalidGraphType


def write(G):
    """
    Return a string specifying the given graph as a XML document.
    
    @type  graph: graph
    @param graph: Graph.

    @rtype:  string
    @return: String specifying the graph as a XML document.
    """
    
    # Document root
    grxml = Document()
    if (type(G) == graph):
        grxmlr = grxml.createElement('graph')
    elif (type(G) == digraph ):
        grxmlr = grxml.createElement('digraph')
    else:
        raise InvalidGraphType
    grxml.appendChild(grxmlr)

    # Each node...
    for each_node in G.nodes():
        node = grxml.createElement('node')
        node.setAttribute('id', str(each_node))
        grxmlr.appendChild(node)
        for each_attr in G.node_attributes(each_node):
            attr = grxml.createElement('attribute')
            attr.setAttribute('attr', each_attr[0])
            attr.setAttribute('value', each_attr[1])
            node.appendChild(attr)

    # Each edge...
    for edge_from, edge_to in G.edges():
        edge = grxml.createElement('edge')
        edge.setAttribute('from', str(edge_from))
        edge.setAttribute('to', str(edge_to))
        edge.setAttribute('wt', str(G.edge_weight(edge_from, edge_to)))
        edge.setAttribute('label', str(G.edge_label(edge_from, edge_to)))
        grxmlr.appendChild(edge)
        for attr_name, attr_value in G.edge_attributes(edge_from, edge_to):
            attr = grxml.createElement('attribute')
            attr.setAttribute('attr', attr_name)
            attr.setAttribute('value', attr_value)
            edge.appendChild(attr)

    return grxml.toprettyxml()


def write_hypergraph(hypergraph):
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
    nodes = hypergraph.nodes()
    hyperedges = hypergraph.hyperedges()
    for each_node in (nodes + hyperedges):
        if (each_node in nodes):
            node = grxml.createElement('node')
        else:
            node = grxml.createElement('hyperedge')
        node.setAttribute('id', str(each_node))
        grxmlr.appendChild(node)

        # and its outgoing edge
        for each_edge in hypergraph.links(each_node):
            edge = grxml.createElement('link')
            edge.setAttribute('to', str(each_edge))
            node.appendChild(edge)

    return grxml.toprettyxml()


def read(string):
    """
    Read a graph from a XML document and return it. Nodes and edges specified in the input will
    be added to the current graph.
    
    @type  string: string
    @param string: Input string in XML format specifying a graph.
    
    @rtype: graph
    @return: Graph
    """
    dom = parseString(string)
    if dom.getElementsByTagName("graph"):
        G = graph()
    elif dom.getElementsByTagName("digraph"):
        G = digraph()
    else:
        raise InvalidGraphType
    
    # Read nodes...
    for each_node in dom.getElementsByTagName("node"):
        G.add_node(each_node.getAttribute('id'))
        for each_attr in each_node.getElementsByTagName("attribute"):
            G.add_node_attribute(each_node.getAttribute('id'),
                                     (each_attr.getAttribute('attr'),
                each_attr.getAttribute('value')))

    # Read edges...
    for each_edge in dom.getElementsByTagName("edge"):
        G.add_edge(each_edge.getAttribute('from'), each_edge.getAttribute('to'), \
            wt = float(each_edge.getAttribute('wt')), label = each_edge.getAttribute('label'))
        for each_attr in each_edge.getElementsByTagName("attribute"):
            attr_tuple = (each_attr.getAttribute('attr'), each_attr.getAttribute('value'))
            if (attr_tuple not in graph.edge_attributes(each_edge.getAttribute('from'), \
                each_edge.getAttribute('to'))):
                G.add_edge_attribute(each_edge.getAttribute('from'), \
                    each_edge.getAttribute('to'), attr_tuple)
    
    return G


def read_hypergraph(hypergraph, string):
    """
    Read a graph from a XML document. Nodes and hyperedges specified in the input will be added
    to the current graph.
    
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
        for each_edge in each_node.getElementsByTagName("link"):
            hypergraph.link(each_node.getAttribute('id'), each_edge.getAttribute('to'))

