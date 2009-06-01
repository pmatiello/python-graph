from pygraph.algorithms.generators import generate

class test_common:
    """
    Tests common to all graph types
    """
    def printfoo( self ):
        return "foo"
    
    def setUp(self):
        """
        Generate a graph as per the classes spec
        """
        assert isinstance(self.test_class, type ), "Expected a graph class for testing, got %s" % repr( self.test_class )
        G = self.test_class()
        generate(G, self.graph_order, self.edge_count)
        self.G = G
        
        
    def tearDown(self):
        del self.G
        
    def test_validate_node_edge_count(self):
        """
        Validate the expected number of nodes & edges.
        """
        
        assert len( self.G.nodes() ) == self.graph_order
        assert len( self.G.edges() ) == self.edge_count, "Found %i edges, expected %i" % ( len( self.G.edges() ), self.edge_count )
    
    def test_zero(self):
        """
        A test that can never fail.
        """
        return True