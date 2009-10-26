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

@sort: read, write
"""


# Imports
from pygraph.classes.digraph import digraph
from pygraph.classes.graph import graph
from xml.dom.minidom import Document, parseString
from pygraph.classes.exceptions import InvalidGraphType


def write(G):
    """
    Return a string specifying the given graph as a XML document.
    
    @type  G: graph
    @param G: Graph.

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
        if (G.has_edge(each_edge.getAttribute('from'), each_edge.getAttribute('to'))):
            G.add_edge(each_edge.getAttribute('from'), each_edge.getAttribute('to'), \
                wt = float(each_edge.getAttribute('wt')), label = each_edge.getAttribute('label'))
        for each_attr in each_edge.getElementsByTagName("attribute"):
            attr_tuple = (each_attr.getAttribute('attr'), each_attr.getAttribute('value'))
            if (attr_tuple not in graph.edge_attributes(each_edge.getAttribute('from'), \
                each_edge.getAttribute('to'))):
                G.add_edge_attribute(each_edge.getAttribute('from'), \
                    each_edge.getAttribute('to'), attr_tuple)
    
    return G

