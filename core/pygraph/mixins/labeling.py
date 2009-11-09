class labeling( object ):
    """
    Generic labeling support for graphs
    """
    WEIGHT_ATTRIBUTE_NAME = "weight"
    DEFAULT_WEIGHT = 1
    
    LABEL_ATTRIBUTE_NAME = "label"
    DEFAULT_LABEL = ""
    
    def __init__(self):
        # Metadata bout edges
        self.edge_properties = {}    # Mapping: Edge -> Dict mapping, lablel-> str, wt->num
        self.edge_attr = {}          # Key value pairs: (Edge -> Attributes)
        
        # Metadata bout nodes
        self.node_attr = {}          # Pairing: Node -> Attributes
        
    def del_node_labeling( self, node ):
        if node in self.node_attr:
            # Since attributes and properties are lazy, they might not exist.
            del( self.node_attr[node] )
        
    def del_edge_labeling( self, edge ):
        
        keys = [edge]
        if not self.DIRECTED:
            keys.append(edge[::-1])
            
        for key in keys:
            for mapping in [self.edge_properties, self.edge_attr ]:
                try:
                    del ( mapping[key] )
                except KeyError:
                    pass
    
    def edge_weight(self, edge):
        """
        Get the weight of an edge.

        @type  edge: edge
        @param edge: One edge.
        
        @rtype:  number
        @return: Edge weight.
        """
        return self.get_edge_properties( edge ).setdefault( self.WEIGHT_ATTRIBUTE_NAME, self.DEFAULT_WEIGHT )


    def set_edge_weight(self, edge, wt):
        """
        Set the weight of an edge.

        @type  edge: edge
        @param edge: One edge.

        @type  wt: number
        @param wt: Edge weight.
        """
        self.set_edge_properties(edge, weight=wt )
        if not self.DIRECTED:
            self.set_edge_properties((edge[1], edge[0]) , weight=wt )


    def edge_label(self, edge):
        """
        Get the label of an edge.

        @type  edge: edge
        @param edge: One edge.
        
        @rtype:  string
        @return: Edge label
        """
        return self.get_edge_properties( edge ).setdefault( self.LABEL_ATTRIBUTE_NAME, self.DEFAULT_LABEL )

    def set_edge_label(self, edge, label):
        """
        Set the label of an edge.

        @type  edge: edge
        @param edge: One edge.

        @type  label: string
        @param label: Edge label.
        """
        self.set_edge_properties(edge, label=label )
        if not self.DIRECTED:
            self.set_edge_properties((edge[1], edge[0]) , label=label )
            
    def set_edge_properties(self, edge, **properties ):
        self.edge_properties.setdefault( edge, {} ).update( properties )
        
    def get_edge_properties(self, edge):
        return self.edge_properties.setdefault( edge, {} )
            
    def add_edge_attribute(self, edge, attr):
        """
        Add attribute to the given edge.

        @type  edge: edge
        @param edge: One edge.

        @type  attr: tuple
        @param attr: Node attribute specified as a tuple in the form (attribute, value).
        """
        self.edge_attr[edge] = self.edge_attributes(edge) + [attr]
        
        if not self.DIRECTED:
            self.edge_attr[(edge[1],edge[0])] = self.edge_attributes((edge[1], edge[0])) + [attr]
    
    def add_edge_attributes(self, edge, attrs):
        """
        Append a sequence of attributes to the given edge
        
        @type  edge: edge
        @param edge: One edge.

        @type  attrs: tuple
        @param attrs: Node attributes specified as a sequence of tuples in the form (attribute, value).
        """
        for attr in attrs:
            self.add_edge_attribute(edge, attr)
    
    
    def add_node_attribute(self, node, attr):
        """
        Add attribute to the given node.

        @type  node: node
        @param node: Node identifier

        @type  attr: tuple
        @param attr: Node attribute specified as a tuple in the form (attribute, value).
        """
        self.node_attr[node] = self.node_attr[node] + [attr]


    def node_attributes(self, node):
        """
        Return the attributes of the given node.

        @type  node: node
        @param node: Node identifier

        @rtype:  list
        @return: List of attributes specified tuples in the form (attribute, value).
        """
        return self.node_attr[node]


    def edge_attributes(self, edge):
        """
        Return the attributes of the given edge.

        @type  edge: edge
        @param edge: One edge.

        @rtype:  list
        @return: List of attributes specified tuples in the form (attribute, value).
        """
        try:
            return self.edge_attr[edge]
        except KeyError:
            return []
