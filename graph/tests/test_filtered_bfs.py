import unittest
import graph
import pprint
import logging

from test_data import nations_of_the_world

log = logging.getLogger( __name__ )

logging.basicConfig()

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
        from_england = self.G.filtered_breadth_first_search( "England" )
        
        assert set( a[1] for a in from_england ) == set ( self.G.nodes() )
        
    def testBasic2(self):
        """
        Test some very basic functionality
        """
        MAXCOST = 6
        
        def myfilterfn( cost, node ):
            if cost > MAXCOST:
                return False
            return True
            
        from_england = self.G.filtered_breadth_first_search( "England", myfilterfn )
        
        costs, nations = zip( *from_england )
        
        for c in costs:
            assert c <= MAXCOST
            
    def testBasic3(self):
        """
        Test some very basic functionality
        """        
        def myfilterfn( cost, node ):
            if node=="Scotland":
                return False
            return True
            
        from_england = self.G.filtered_breadth_first_search( "England", myfilterfn )
        
        costs, nations = zip( *from_england )
        assert not "Scotland" in nations 
        
    def testBasic4(self):
        """
        Test some very basic functionality
        """        
        def myfilterfn( cost, node ):
            if node=="England":
                return False
            return True
            
        from_england = [ a for a in self.G.filtered_breadth_first_search( "England", myfilterfn ) ]
        
        assert len(from_england) == 0, "Should be an empty list, got %s" % repr( from_england )
        
        
        

            
        