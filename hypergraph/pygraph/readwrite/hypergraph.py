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
Functions for reading and writing hypergraphs in Dot and XML markup..

@sort: read_dot, read_markup, write_dot, write_markup
"""


# Imports
from pygraph.classes.hypergraph import hypergraph
from xml.dom.minidom import Document, parseString
from pygraph.classes.exceptions import InvalidGraphType
import pydot


def write_markup(hgr):
    """
    Return a string specifying the given hypergraph as a XML document.
    
    @type  hgr: hypergraph
    @param hgr: Hypergraph.

    @rtype:  string
    @return: String specifying the graph as a XML document.
    """

    # Document root
    grxml = Document()
    grxmlr = grxml.createElement('hypergraph')
    grxml.appendChild(grxmlr)

    # Each node...
    nodes = hgr.nodes()
    hyperedges = hgr.hyperedges()
    for each_node in (nodes + hyperedges):
        if (each_node in nodes):
            node = grxml.createElement('node')
        else:
            node = grxml.createElement('hyperedge')
        node.setAttribute('id', str(each_node))
        grxmlr.appendChild(node)

        # and its outgoing edge
        for each_edge in hgr.links(each_node):
            edge = grxml.createElement('link')
            edge.setAttribute('to', str(each_edge))
            node.appendChild(edge)

    return grxml.toprettyxml()


def read_markup(string):
    """
    Read a graph from a XML document. Nodes and hyperedges specified in the input will be added
    to the current graph.

    @type  string: string
    @param string: Input string in XML format specifying a graph.
        
    @rtype: hypergraph
    @return: Hypergraph
    """
    
    hgr = hypergraph()
    
    dom = parseString(string)
    for each_node in dom.getElementsByTagName("node"):
        hgr.add_nodes(each_node.getAttribute('id'))
    for each_node in dom.getElementsByTagName("hyperedge"):
        hgr.add_hyperedges(each_node.getAttribute('id'))
    dom = parseString(string)
    for each_node in dom.getElementsByTagName("node"):
        for each_edge in each_node.getElementsByTagName("link"):
            hgr.link(each_node.getAttribute('id'), each_edge.getAttribute('to'))
    return hgr


def read_dot(string):
    """
    Read a hypergraph from a string in dot format. Nodes and edges specified in the input will be added to the current hypergraph.
    
    @type  string: string
    @param string: Input string in dot format specifying a graph.
    
    @rtype:  hypergraph
    @return: Hypergraph
    """
    hgr = hypergraph()
    dotG = pydot.graph_from_dot_data(string)
    
    # Read the hypernode nodes...
    # Note 1: We need to assume that all of the nodes are listed since we need to know if they
    #           are a hyperedge or a normal node
    # Note 2: We should read in all of the nodes before putting in the links
    for each_node in dotG.get_nodes():
        if 'node' == each_node.get('hyper_node_type'):
            hgr.add_node(each_node.get_name())
        elif 'hyperedge' == each_node.get('hyper_node_type'):
            hgr.add_hyperedge(each_node.get_name())
        else:
            print ("Error: improper hyper_node_type - %s" % str(each_node.get('hyper_node_type')))
    
    # Now read in the links to connect the hyperedges
    for each_link in dotG.get_edges():
        if hgr.has_node(each_link.get_source()):
            link_hypernode = each_link.get_source()
            link_hyperedge = each_link.get_destination()
        elif hgr.has_node(each_link.get_destination()):
            link_hypernode = each_link.get_destination()
            link_hyperedge = each_link.get_source()
        
        hgr.link(link_hypernode, link_hyperedge)
    
    return hgr


def write_dot(hgr, colored = False):
    """
    Return a string specifying the given hypergraph in DOT Language.
    
    @type  hgr: hypergraph
    @param hgr: Hypergraph.
    
    @type  colored: boolean
    @param colored: Whether hyperedges should be colored.

    @rtype:  string
    @return: String specifying the hypergraph in DOT Language.
    """ 
    dotG = pydot.Dot()
    
    if not 'name' in dir(hgr):
        dotG.set_name('hypergraph')
    else:
        dotG.set_name(hgr.name)
    
    colortable = {}
    colorcount = 0
    
    # Add all of the nodes first
    for node in hgr.nodes():
        newNode = pydot.Node(str(node), hyper_node_type = 'node')
        
        dotG.add_node(newNode)
    
    for hyperedge in hgr.hyperedges():
        
        if (colored):
            colortable[hyperedge] = colors[colorcount % len(colors)]
            colorcount += 1
            
            newNode = pydot.Node(str(hyperedge), hyper_node_type = 'hyperedge', \
                                                 color = str(colortable[hyperedge]), \
                                                 shape = 'point')
        else:
            newNode = pydot.Node(str(hyperedge), hyper_node_type = 'hyperedge')
        
        dotG.add_node(newNode)
        
        for link in hgr.links(hyperedge):
            newEdge = pydot.Edge(str(hyperedge), str(link))
            dotG.add_edge(newEdge)
    
    return dotG.to_string()