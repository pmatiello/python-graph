class labeling( object ):
    """
    Generic labeling support for graphs
    """
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
        return self.edge_properties[(u, v)][1]


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
        self.edge_properties[(u, v)][1] = wt
        self.edge_properties[(v, u)][1] = wt


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
        return self.edge_properties[(u, v)][0]


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
        self.edge_properties[(u, v)][0] = label
        self.edge_properties[(v, u)][0] = label
    
    
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
        self.edge_attr[(u,v)] = self.edge_attr[(u,v)] + [attr]
        self.edge_attr[(v,u)] = self.edge_attr[(v,u)] + [attr]


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
        return self.edge_attr[(u,v)]