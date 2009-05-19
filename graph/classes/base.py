class base(object):
    """
    Base behavior common to all graphs
    """
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
        for node in self.nodes():
            yield node
            
    def __getitem__(self, node):
        """
        Return a iterator passing through all neighbors of the given node.
        
        @rtype:  iterator
        @return: Iterator passing through all neighbors of the given node.
        """
        for each in self.node_neighbors[node]:
            yield each
            
    def generate(self, num_nodes, num_edges, weight_range=(1, 1)):
        """
        Add nodes and random edges to the graph.
        
        @type  num_nodes: number
        @param num_nodes: Number of nodes.
        
        @type  num_edges: number
        @param num_edges: Number of edges.

        @type  weight_range: tuple
        @param weight_range: tuple of two integers as lower and upper limits on randomly generated
        weights (uniform distribution).
        """
        generators.generate(self, num_nodes, num_edges, weight_range)
        
    def add_nodes(self, nodelist):
        """
        Add given nodes to the graph.
        
        @attention: While nodes can be of any type, it's strongly recommended to use only numbers
        and single-line strings as node identifiers if you intend to use write().

        @type  nodelist: list
        @param nodelist: List of nodes to be added to the graph.
        """
        for each in nodelist:
            self.add_node(each)