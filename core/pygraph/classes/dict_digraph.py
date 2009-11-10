# Copyright (c) 2007-2009 Pedro Matiello <pmatiello@gmail.com>
#                         Christian Muise <christian.muise@gmail.com>
#                         Johannes Reinhardt <jreinhardt@ist-dein-freund.de>
#                         Nathan Davis <davisn90210@gmail.com>
#                         Zsolt Haraszti <zsolt@drawwell.net>
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
Digraph class
"""

# Imports
from pygraph.classes.exceptions import AdditionError, DeletionError
from pygraph.mixins.labeling import labeling
from pygraph.mixins.common import common
from pygraph.mixins.basegraph import basegraph

class Node( object ):
    
    def __init__(self):
        self.__neighbors = {}
        self.__incidents = {}
        
    def __repr__(self):
        return "<%s.%s %s>" % (self.__class__.__module__, self.__class__.__name__, str(self) )
    
    def __str__(self):
        str_n = ", ".join( repr(a) for a in self.__neighbors.keys() )
        str_i = ", ".join( repr(a) for a in self.__incidents.keys() )
        return "N: %s, I: %s" % (str_n, str_i)
    
    def order(self):
        return len(self.__neighbors)    
            
    def get_incidents(self):
        return self.__incidents.keys()
            
    def set_incident(self, u, **kwargs ):
        if not u in self.__incidents:
            self.__incidents[u] = kwargs
        else:
            raise AdditionError( "Node %s is already incident on %s" % (repr(u), repr(self)) )
        
    def has_incident(self, u):
        return u in self.__incidents
    
    def del_incident(self, u):
        if u in self.__incidents:
            del self.__incidents[u]
        else:
            raise DeletionError( "Edge %s is not incident on %s" % (repr(u), repr(self)) )
        
    def get_neighbors(self):
        return self.__neighbors.keys()
        
    def set_neighbor(self, v, **kwargs ):
        if not v in self.__neighbors:
            self.__neighbors[v] = kwargs
        else:
            raise AdditionError( "Node %s is already a neighbor of %s" % (repr(v), repr(self)) )
        
    def del_neighbor(self, v):
        if v in self.__neighbors:
            del self.__neighbors[v]
        else:
            raise DeletionError( "Edge %s is not not a neighbor of %s" % (repr(v), repr(self)) )
    
    def has_neighbor(self, v):
        return v in self.__neighbors
        
class dict_digraph( basegraph, common, labeling ):
    """
    Adapts anything which looks like a dict to something which looks and behaves like one of our digraphs. Objects in the graph can be anything 
    
    Digraphs are built of nodes and directed edges.

    @sort: __init__, __getitem__, __iter__, __len__, __str__, add_edge, add_edge_attribute,
    add_graph, add_node, add_node_attribute, add_nodes, add_spanning_tree, complete, 
    del_edge, del_node, edges, edge_attributes, edge_label,
    edge_weight, node_attributes, has_edge, has_node, incidents, inverse,
    neighbors, node_degree, node_order, nodes, reverse, set_edge_label, set_edge_weight
    """
    DIRECTED = True
    
    def __init__( self, G=None, inverted=False, reversed=False ):
        """
        Initialize a digraph.
        """
        if G:
            self.G = G
        else:
            self.G = {}
            
        common.__init__(self)
        labeling.__init__(self)
        
    def nodes(self):
        """
        Return node list.

        @rtype:  list
        @return: Node list.
        """
        return self.G.keys()


    def neighbors(self, node):
        """
        Return all nodes that are directly accessible from given node.

        @type  node: node
        @param node: Node identifier

        @rtype:  list
        @return: List of nodes directly accessible from given node.
        """
        N = self.G[ node ]
        return N.get_neighbors()
    
    
    def incidents(self, node):
        """
        Return all nodes that are incident to the given node.
        
        @type  node: node
        @param node: Node identifier

        @rtype:  list
        @return: List of nodes directly accessible from given node.    
        """
        N = self.G[ node ]
        return N.get_incidents()
        
    def edges(self):
        """
        Return all edges in the graph.
        
        @rtype:  iterator
        @return: List of all edges in the graph.
        """
        for N_id in self.nodes():
            N = self.G[N_id]
            for neighbor_id in N.get_neighbors():
                yield (N_id, neighbor_id)

    def has_node(self, node):
        """
        Return whether the requested node exists.

        @type  node: node
        @param node: Node identifier

        @rtype:  boolean
        @return: Truth-value for node existence.
        """
        return node in self.G

    def add_node(self, node, obj=None ):
        """
        Add given node to the graph.
        
        @attention: While nodes can be of any type, it's strongly recommended to use only
        numbers and single-line strings as node identifiers if you intend to use write().

        @type  node: node
        @param node: Node identifier.
        """
        if obj==None:
            obj = Node()
            
        if node in self.G:
            raise AdditionError( "The node %s already exists" % repr(node) )
        self.G[node]=obj


    def add_edge(self, edge, wt = 1, label="", ):
        """
        Add an directed edge (u,v) to the graph connecting nodes u to v.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.
        
        @type  wt: number
        @param wt: Edge weight.
        
        @type  label: string
        @param label: Edge label.
        """
        u,v = edge
        
        try:
            U = self.G[u]
        except KeyError as ke:
            raise AdditionError("Cannot add an edge from non-existant node %s" % repr(u) )
            
        try:
            V = self.G[v]
        except KeyError as ke:
            raise AdditionError("Cannot add an edge to non-existant node %s" % repr(v) )
            
        # Add some guard in case the node already exists.
        U.set_neighbor(v, label=label, wt=wt )
        V.set_incident(u)

    def del_node(self, node):
        """
        Remove a node from the graph.
        
        @type  node: node
        @param node: Node identifier.
        """
        for neighbor_id in self.neighbors(node):
            neighbor = self.G[ neighbor_id ]
            neighbor.del_incident(node)
            
        del self.G[ node ]
        


    def del_edge(self, edge ):
        """
        Remove an directed edge (u, v) from the graph.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.
        """
        u,v = edge 
        U = self.G[u]
        V = self.G[v]
        
        U.del_neighbor(v)
        V.del_incident(u)


    def has_edge(self, edge ):
        """
        Return whether an edge between nodes u and v exists.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.

        @rtype:  boolean
        @return: Truth-value for edge existence.
        """
        u,v=edge
        try:
            return self.G[u].has_neighbor(v)
        except KeyError as ke:
            return False

    
    def node_order(self, node):
        """
        Return the order of the given node.
        
        @rtype:  number
        @return: Order of the given node.
        """
        N = self.G[node]
        return N.order()
    
if __name__ == "__main__":
    gr = dict_digraph()
    import pdb
    pdb.set_trace()
    