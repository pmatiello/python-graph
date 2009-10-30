class common( object ):
    """
    Standard methods common to all graph classes.
    """
    
    def __str__(self):
        """
        Return a string representing the graph when requested by str() (or print).

        @rtype:  string
        @return: String representing the graph.
        """
        str_nodes = repr( self.nodes() )
        str_edges = repr( self.edges() )
        return "%s %s" % ( str_nodes, str_edges )

    def __repr__(self):
        """
        Return a string representing the graph when requested by repr()

        @rtype:  string
        @return: String representing the graph.
        """
        return "<%s.%s %s>" % ( self.__class__.__module__, self.__class__.__name__, str(self) )
    
    def __iter__(self):
        """
        Return a iterator passing through all nodes in the graph.
        
        @rtype:  iterator
        @return: Iterator passing through all nodes in the graph.
        """
        for n in self.nodes():
            yield n
            
    def __len__(self):
        """
        Return the order of self when requested by len().

        @rtype:  number
        @return: Size of the graph.
        """
        return self.order()
    
    def __getitem__(self, node):
        """
        Return a iterator passing through all neighbors of the given node.
        
        @rtype:  iterator
        @return: Iterator passing through all neighbors of the given node.
        """
        for n in self.neighbors( node ):
            yield n
            
    def order(self):
        """
        Return the order of self, this is defined as the number of nodes in the graph.

        @rtype:  number
        @return: Size of the graph.
        """
        return len(self.nodes())
            
    def add_nodes(self, nodelist):
        """
        Add given nodes to the graph.
        
        @attention: While nodes can be of any type, it's strongly recommended to use only
        numbers and single-line strings as node identifiers if you intend to use write().
        Objects used to identify nodes absolutely must be hashable. If you need attach a mutable
        or non-hashable node, consider using the labeling feature.

        @type  nodelist: list
        @param nodelist: List of nodes to be added to the graph.
        """
        for each in nodelist:
            self.add_node(each)
            
    def add_graph(self, other ):
        """
        Add other graph to this graph.
        
        @attention: Attributes and labels are not preserved.
        
        @type  graph: graph
        @param graph: Graph
        """
        self.add_nodes( n for n in other.nodes() if not n in self.nodes() )
        
        for each_node in other.nodes():
            for each_edge in other.neighbors(each_node):
                if (not self.has_edge(each_node, each_edge)):
                    self.add_edge(each_node, each_edge)


    def add_spanning_tree(self, st):
        """
        Add a spanning tree to the graph.
        
        @type  st: dictionary
        @param st: Spanning tree.
        """
        self.add_nodes(list(st.keys()))
        for each in st:
            if (st[each] is not None):
                self.add_edge(st[each], each)
                
    
    def complete(self):
        """
        Make the graph a complete graph.
        
        @attention: This will modify the current graph.
        """
        for each in self.nodes():
            for other in self.nodes():
                if (each != other and not self.has_edge(each, other)):
                    self.add_edge(each, other)


    def inverse(self):
        """
        Return the inverse of the graph.
        
        @rtype:  graph
        @return: Complement graph for the graph.
        """
        inv = self.__class__()
        inv.add_nodes(self.nodes())
        inv.complete()
        for each in self.edges():
            if (inv.has_edge(each[0], each[1])):
                inv.del_edge(each[0], each[1])
        return inv
    
    def reverse(self):
        """
        Generate the reverse of a directed graph, returns an identical graph if not directed.
        Attributes & weights are preserved.
        
        @rtype: digraph
        @return: The directed graph that should be reversed.
        """
        N = self.__class__()
    
        #- Add the nodes
        N.add_nodes( n for n in N.nodes() if not n in self.nodes() )
    
        #- Add the reversed edges
        for (u, v) in self.edges():
            wt = self.edge_weight(u, v)
            label = self.edge_label(u, v)
            attributes = self.edge_attributes(u, v)
            N.add_edge(v, u, wt, label, attributes)
    
        return N
