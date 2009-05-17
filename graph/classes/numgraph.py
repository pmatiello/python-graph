import numpy

class NumGraph( object ):
    
    DISCONNECTED_VALUE = numpy.Inf
    
    def init( self, order=0 ):
        self._matrix = numpy.array( [ [ self.DISCONNECTED_VALUE ]*order ]*order )
        
    def order(self):
        return len( self._matrix )
        
    def __str__(self):
        """
        Return a string representing the graph when requested by str() (or print).

        @rtype:  string
        @return: String representing the graph.
        """
        return "<graph object " + str(self.nodes()) + " " + str(self.edges()) + ">"


    def __len__(self):
        """
        Return the order of the graph when requested by len().

        @rtype:  number
        @return: Size of the graph.
        """
        return self.order()


    def __iter__(self):
        """
        Return a iterator passing through all nodes in the graph.
        
        @rtype:  iterator
        @return: Iterator passing through all nodes in the graph.
        """
        return self.nodes()


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
        return numpy.isnan( self._matrix[ node ] )
    
    
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


    
    
        
    