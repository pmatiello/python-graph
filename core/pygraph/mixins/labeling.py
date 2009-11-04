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
        
    def del_edge_labeling( self, u, v ):
        k = (u,v)
        
        keys = [k]
        if not self.DIRECTED:
            keys.append(k[::-1])
            
        for key in keys:
            for mapping in [self.edge_properties, self.edge_attr ]:
                try:
                    del ( mapping[key] )
                except KeyError:
                    pass
    
    def edge_weight(self, u, v):
        """
        Get the weight of an edge.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.
        
        @rtype:  number
        @return: Edge weight.
        """
        return self.get_edge_properties( u,v, ).setdefault( self.WEIGHT_ATTRIBUTE_NAME, self.DEFAULT_WEIGHT )


    def set_edge_weight(self, u, v, wt):
        """
        Set the weight of an edge.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.

        @type  wt: number
        @param wt: Edge weight.
        """
        self.set_edge_properties(u, v, weight=wt )
        if not self.DIRECTED:
            self.set_edge_properties(v, u , weight=wt )


    def edge_label(self, u, v):
        """
        Get the label of an edge.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.
        
        @rtype:  string
        @return: Edge label
        """
        k = (u,v)
        return self.get_edge_properties( u,v, ).setdefault( self.LABEL_ATTRIBUTE_NAME, self.DEFAULT_LABEL )

    def set_edge_label(self, u, v, label):
        """
        Set the label of an edge.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.

        @type  label: string
        @param label: Edge label.
        """
        self.set_edge_properties(u, v, label=label )
        if not self.DIRECTED:
            self.set_edge_properties(v, u , label=label )
            
    def set_edge_properties(self, u, v, **properties ):
        k = (u,v)
        self.edge_properties.setdefault( k, {} ).update( properties )
        
    def get_edge_properties(self, u, v):
        k = (u,v)
        return self.edge_properties.setdefault( k, {} )
            
    def add_edge_attribute(self, u, v, attr):
        """
        Add attribute to the given edge.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.

        @type  attr: tuple
        @param attr: Node attribute specified as a tuple in the form (attribute, value).
        """
        self.edge_attr[(u,v)] = self.edge_attributes(u,v) + [attr]
        
        if not self.DIRECTED:
            self.edge_attr[(v,u)] = self.edge_attributes(v,u) + [attr]
    
    def add_edge_attributes(self, u, v, attrs):
        """
        Append a sequence of attributes to the given edge
        
        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.

        @type  attrs: tuple
        @param attrs: Node attributes specified as a sequence of tuples in the form (attribute, value).
        """
        for attr in attrs:
            self.add_edge_attribute(u, v, attr)
    
    
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


    def edge_attributes(self, u, v):
        """
        Return the attributes of the given edge.

        @type  u: node
        @param u: One node.

        @type  v: node
        @param v: Other node.

        @rtype:  list
        @return: List of attributes specified tuples in the form (attribute, value).
        """
        try:
            return self.edge_attr[(u,v)]
        except KeyError as ke:
            return []