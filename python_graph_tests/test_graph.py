import unittest
import graph

from python_graph_tests.utils import countries_of_the_world

class test_graph( unittest.TestCase ):
    """
    Test some very basic graph functions
    """
    
    def setUp(self):
        self.G = graph.graph()
        countries_of_the_world(G)
        
        
        