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
Functions for reading and writing graphs.

@sort: read_xml, write_xml, write_dot_graph, write_dot_digraph, write_dot_hypergraph
"""


# Imports
from xml.dom.minidom import Document, parseString
import pydot


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
    for each_node in graph.nodes():
        node = grxml.createElement('node')
        node.setAttribute('id',str(each_node))
        grxmlr.appendChild(node)
        for each_attr in graph.get_node_attributes(each_node):
            attr = grxml.createElement('attribute')
            attr.setAttribute('attr', each_attr[0])
            attr.setAttribute('value', each_attr[1])
            node.appendChild(attr)

    # Each edge...
    for edge_from, edge_to in graph.edges():
        edge = grxml.createElement('edge')
        edge.setAttribute('from',str(edge_from))
        edge.setAttribute('to',str(edge_to))
        edge.setAttribute('wt',str(graph.get_edge_weight(edge_from, edge_to)))
        edge.setAttribute('label',str(graph.get_edge_label(edge_from, edge_to)))
        grxmlr.appendChild(edge)
        for attr_name, attr_value in graph.get_edge_attributes(edge_from, edge_to):
            attr = grxml.createElement('attribute')
            attr.setAttribute('attr', attr_name)
            attr.setAttribute('value', attr_value)
            edge.appendChild(attr)

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
    nodes = hypergraph.nodes()
    hyperedges = hypergraph.get_hyperedges()
    for each_node in (nodes + hyperedges):
        if (each_node in nodes):
            node = grxml.createElement('node')
        else:
            node = grxml.createElement('hyperedge')
        node.setAttribute('id',str(each_node))
        grxmlr.appendChild(node)

        # and its outgoing edge
        for each_edge in hypergraph.get_links(each_node):
            edge = grxml.createElement('link')
            edge.setAttribute('to',str(each_edge))
            node.appendChild(edge)

    return grxml.toprettyxml()


def read_xml(graph, string):
    """
    Read a graph from a XML document. Nodes and edges specified in the input will be added to the current graph.
    
    @type  graph: graph
    @param graph: Graph

    @type  string: string
    @param string: Input string in XML format specifying a graph.
    """
    dom = parseString(string)
    
    # Read nodes...
    for each_node in dom.getElementsByTagName("node"):
        graph.add_node(each_node.getAttribute('id'))
        for each_attr in each_node.getElementsByTagName("attribute"):
            graph.add_node_attribute(each_node.getAttribute('id'), (each_attr.getAttribute('attr'),
                each_attr.getAttribute('value')))

    # Read edges...
    for each_edge in dom.getElementsByTagName("edge"):
        graph.add_edge(each_edge.getAttribute('from'), each_edge.getAttribute('to'), \
            wt=float(each_edge.getAttribute('wt')), label=each_edge.getAttribute('label'))
        for each_attr in each_edge.getElementsByTagName("attribute"):
            attr_tuple = (each_attr.getAttribute('attr'), each_attr.getAttribute('value'))
            if (attr_tuple not in graph.get_edge_attributes(each_edge.getAttribute('from'), \
                each_edge.getAttribute('to'))):
                graph.add_edge_attribute(each_edge.getAttribute('from'), \
                    each_edge.getAttribute('to'), attr_tuple)


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
        for each_edge in each_node.getElementsByTagName("link"):
            hypergraph.link(each_node.getAttribute('id'), each_edge.getAttribute('to'))


################
# DOT Language #
################


def read_dot_graph(graph, string):
    """
    Read a graph from a string in dot format. Nodes and edges specified in the input will be added to the current graph.
    
    @type  graph: graph
    @param graph: Graph

    @type  string: string
    @param string: Input string in dot format specifying a graph.
    """
    dotG = pydot.graph_from_dot_data(string)
    
    # Read nodes...
    # Note: If the nodes aren't explicitly listed, they need to be
    for each_node in dotG.get_nodes():
        graph.add_node(each_node.get_name())
        for each_attr_key, each_attr_val in each_node.get_attributes().items():
            graph.add_node_attribute(each_node.get_name(), (each_attr_key, each_attr_val))
    
    # Read edges...
    for each_edge in dotG.get_edges():
        # Check if the nodes have been added
        if not dotG.get_node(each_edge.get_source()):
            graph.add_node(each_edge.get_source())
        if not dotG.get_node(each_edge.get_destination()):
            graph.add_node(each_edge.get_destination())
        
        # See if there's a weight
        if 'wt' in each_edge.get_attributes().keys():
            _wt = each_edge.get_attributes()['wt']
        else:
            _wt = 1
        
        # See if there is a label
        if 'label' in each_edge.get_attributes().keys():
            _label = each_edge.get_attributes()['label']
        else:
            _label = ''
        
        graph.add_edge(each_edge.get_source(), each_edge.get_destination(), wt=_wt, label=_label)
        
        for each_attr_key, each_attr_val in each_edge.get_attributes().items():
            if not each_attr_key in ['wt', 'label']:
                graph.add_edge_attribute(each_edge.get_source(), each_edge.get_destination(), \
                                            (each_attr_key, each_attr_val) )


def read_dot_hypergraph(hypergraph, string):
    """
    Read a hypergraph from a string in dot format. Nodes and edges specified in the input will be added to the current hypergraph.
    
    @type  hypergraph: hypergraph
    @param hypergraph: Hypergraph

    @type  string: string
    @param string: Input string in dot format specifying a graph.
    """
    dotG = pydot.graph_from_dot_data(string)
    
    # Read the hypernode nodes...
    # Note 1: We need to assume that all of the nodes are listed since we need to know if they
    #           are a hyperedge or a normal node
    # Note 2: We should read in all of the nodes before putting in the links
    for each_node in dotG.get_nodes():
        if 'node' == each_node.get('hyper_node_type'):
            hypergraph.add_node(each_node.get_name())
        elif 'hyperedge' == each_node.get('hyper_node_type'):
            hypergraph.add_hyperedge(each_node.get_name())
        else:
            print "Error: improper hyper_node_type - " + str(each_node.get('hyper_node_type'))
    
    # Now read in the links to connect the hyperedges
    for each_link in dotG.get_edges():
        if hypergraph.has_node(each_link.get_source()):
            link_hypernode = each_link.get_source()
            link_hyperedge = each_link.get_destination()
        elif hypergraph.has_node(each_link.get_destination()):
            link_hypernode = each_link.get_destination()
            link_hyperedge = each_link.get_source()
        
        hypergraph.link(link_hypernode, link_hyperedge)
    
    
def write_dot_digraph(graph, wt):
    """
    Return a string specifying the given digraph in DOT Language.
    
    @type  graph: graph
    @param graph: Graph.

    @type  wt: boolean
    @param wt: Whether arrows should be labelled with its weight.

    @rtype:  string
    @return: String specifying the graph in DOT Language.
    """
    return write_dot_graph(graph, wt, directed=True)


def write_dot_graph(graph, wt, directed=False):
    """
    Return a string specifying the given graph in DOT Language.
    
    @type  graph: graph
    @param graph: Graph.

    @type  wt: boolean
    @param wt: Whether edges should be labelled with its weight.
    
    @type  directed: boolean
    @param directed: Whether the graph should be directed or not.

    @rtype:  string
    @return: String specifying the graph in DOT Language.
    """
    dotG = pydot.Dot()
    
    dotG.set_name('graphname')
    
    if directed:
        dotG.set_type('digraph')
    else:
        dotG.set_type('graph')
    
    for node in graph.nodes():
        attr_list = {}
        for attr in graph.get_node_attributes(node):
            attr_list[str(attr[0])] = str(attr[1])
        
        newNode = pydot.Node(str(node), **attr_list)
        
        dotG.add_node(newNode)
        
    # Pydot doesn't work properly with the get_edge, so we use
    #  our own set to keep track of what's been added or not.
    seen_edges = set([])
    for edge_from, edge_to in graph.edges():
        if (str(edge_from) + "-" + str(edge_to)) in seen_edges:
            continue

        if (not directed) and (str(edge_to) + "-" + str(edge_from)) in seen_edges:
            continue
        
        attr_list = {}
        for attr in graph.get_edge_attributes(edge_from, edge_to):
            attr_list[str(attr[0])] = str(attr[1])
        
        if str(graph.get_edge_label(edge_from, edge_to)):
            attr_list['label'] = str(graph.get_edge_label(edge_from, edge_to))
        
        if wt:
            attr_list['wt'] = str(graph.get_edge_weight(edge_from, edge_to))
        
        newEdge = pydot.Edge(str(edge_from), str(edge_to), **attr_list)
        
        dotG.add_edge(newEdge)
        
        seen_edges.add(str(edge_from) + "-" + str(edge_to))
        
    return dotG.to_string()



def write_dot_hypergraph(hypergraph, colored=False):
    """
    Return a string specifying the given hypergraph in DOT Language.
    
    @type  hypergraph: hypergraph
    @param hypergraph: Hypergraph.
    
    @type  colored: boolean
    @param colored: Whether hyperedges should be colored.

    @rtype:  string
    @return: String specifying the hypergraph in DOT Language.
    """
    
    dotG = pydot.Dot()
    
    dotG.set_name('hypergraph')
    
    colortable = {}
    colorcount = 0
    
    # Add all of the nodes first
    for node in hypergraph.nodes():
        newNode = pydot.Node(str(node), hyper_node_type='node')
        
        dotG.add_node(newNode)
    
    for hyperedge in hypergraph.hyperedges():
        
        if (colored):
            colortable[hyperedge] = colors[colorcount % len(colors)]
            colorcount += 1
            
            newNode = pydot.Node(str(hyperedge), hyper_node_type='hyperedge', \
                                                 color=str(colortable[hyperedge]), \
                                                 shape='point')
        else:
            newNode = pydot.Node(str(hyperedge), hyper_node_type='hyperedge')
        
        dotG.add_node(newNode)
        
        for link in hypergraph.links(hyperedge):
            newEdge = pydot.Edge(str(hyperedge), str(link))
            dotG.add_edge(newEdge)
    
    return dotG.to_string()
    
