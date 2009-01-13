import unittest
import graph
from test_data import nations_of_the_world

class testAStar( unittest.TestCase ):
    """
    Test some very basic graph functions
    """

    def setUp(self):
        self.G = graph.graph()
        nations_of_the_world(self.G)

    def testBasic1(self):
        """
        Retrieve all the nodes in distance order
        """
        nodes = self.G.nodes()
        assert len(nodes) == len( set(nodes) )
        