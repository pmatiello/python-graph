import random
import time
import logging
import warnings
from pygraph.algorithms.generators import generate

log = logging.getLogger(__name__)

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
        self.randomseed = hash( time.time() )
        assert isinstance(self.test_class, type ), "Expected a graph class for testing, got %s" % repr( self.test_class )
        self.G = self.makeTestGraph()
        
    def makeTestGraph(self):
        G = self.test_class()
        log.warn("Generating %s with random seed: %i" % ( self.test_class, self.randomseed ) )
        random.seed( self.randomseed )
        generate(G, self.graph_order, self.edge_count)
        return G
        
        
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