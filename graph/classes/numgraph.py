import numpy

from graph.classes.base import base as base_graph

class NumGraph( base_graph ):
    
    DISCONNECTED_VALUE = numpy.Inf
    
    def init( self, order=0 ):
        # The main matrix, stores an adjacency table
        self._matrix = numpy.array( [ [ self.DISCONNECTED_VALUE ]*order ]*order )
        self._lookup = numpy.array( [ None ] * order )
        
        
    def order(self):
        return len( self._matrix )
        
    def __getitem__(self, node):
        """
        Return a iterator passing through all neighbors of the given node.
        
        @rtype:  iterator
        @return: Iterator passing through all neighbors of the given node.
        """
        for each in self.node_neighbors[node]:
            yield each
        
    def nodes(self):
        """
        Return node list.

        @rtype:  list
        @return: Node list.
        """
        return xrange( 0, len( self._matrix ) )
    
    def neighbors(self, node):
        """
        Return all nodes that are directly accessible from given node.

        @type  node: node
        @param node: Node identifier

        @rtype:  list
        @return: List of nodes directly accessible from given node.
        """
        index = self._lookup.index( node )
        return numpy.array( a for a in self._matrix[ index ] if not a == self.DISCONNECTED_VALUE )
    
    
    def edges(self):
        """
        Return all edges in the graph.
        
        @rtype:  list
        @return: List of all edges in the graph.
        """
        o = len( self._matrix )
        
        for i in xrange( 0, o ):
            for j in xrange( 0, o ):
                if i > j:
                    v = self._matrix[i][j]
                    if v not in [ self.DISCONNECTED_VALUE ]:
                        yield (i,j)
        
    def has_node(self, node):
        """
        Return whether the requested node exists.

        @type  node: node
        @param node: Node identifier

        @rtype:  boolean
        @return: Truth-value for node existence.
        """
        if node in self._lookup:
            return True
        return False


    def add_node(self, node, attrs=[]):
        """
        Add given node to the graph.
        
        @attention: While nodes can be of any type, it's strongly recommended to use only numbers
        and single-line strings as node identifiers if you intend to use write().

        @type  node: node
        @param node: Node identifier.
        
        @type  attrs: list
        @param attrs: List of node attributes specified as (attribute, value) tuples.
        """
        if node not in self._lookup:
            self._lookup.append(node)
            self._add_row_col( self._matrix )
            

        
    