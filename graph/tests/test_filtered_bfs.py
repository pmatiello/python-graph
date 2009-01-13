import unittest
import graph
import pprint
from test_data import nations_of_the_world

class testBFS( unittest.TestCase ):
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
        from_england = graph.filtered_bfs.filtered_bfs( self.G, "England" )
        
        assert set( from_england ) == set ( self.G.nodes() )
        
    def testBasic2(self):
        """
        Test some very basic functionality
        """
        def myfilterfn( cost, node ):
            REJECT_STRING = "Slov"
            
            assert type(cost) == int
            assert type(node) == str
            if cost > 6:
                return False
            if REJECT_STRING in node:
                return False 
            return True
            
        from_england = graph.filtered_bfs.filtered_bfs( self.G, "England", myfilterfn )

        for c in ["Slovenia", "Slovakia", "India", "South Korea"]:
            assert c not in from_england
        
        pprint.pprint( [ a for a in from_england ] )