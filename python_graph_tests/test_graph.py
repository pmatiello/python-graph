import unittest
import graph

from python_graph_tests.utils import nations_of_the_world

class test_graph( unittest.TestCase ):
    """
    Test some very basic graph functions
    """
    
    def setUp(self):
        self.G = graph.graph()
        countries_of_the_world(G)
        
    def testBasic1(self):
        """
        Test some very basic functionality
        """
        englands_neighbors = self.G.neighbors("England")
        
        import pdb
        pdb.set_trace()
        
        