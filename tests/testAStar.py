import sys
sys.path.append('..')
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
        Test some very basic functionality
        """
        englands_neighbors = self.G.neighbors("England")
        assert set(['Wales', 'Scotland', 'France', 'Ireland']) == set( englands_neighbors )

    def testAStar1(self):
        heuristic = graph.heuristics.chow( "Wales", "North Korea", "Russia" )
        heuristic.optimize( self.G )
        result = graph.minmax.heuristic_search( self.G, "England", "India", heuristic )
        
    def testAStar_Unreachable(self):
        heuristic = graph.heuristics.chow( "Wales", "North Korea", "Russia" )
        
        self.G.add_node( "Sealand" )
        self.G.add_edge( "England", "Sealand" )
        heuristic.optimize( self.G )
        
        self.G.del_edge( "England", "Sealand" )
        
        try:
            result = graph.minmax.heuristic_search( self.G, "England", "Sealand" , heuristic )
        except graph.exceptions.unreachable, _:
            return
        
        assert False, "This test should rase an unreachable error."
            
        
    

class testAStarEuclideanHeuristic( unittest.TestCase ):
    """
    Test the Euclidean heuristic for the A* algorithm.
    """

    def setUp(self):
        self.G = graph.graph()
        self.G.add_node('A', [('position',[0,0])])
        self.G.add_node('B', [('position',[2,0])])
        self.G.add_node('C', [('position',[2,3])])
        self.G.add_node('D', [('position',[1,2])])
        self.G.add_edge('A', 'B', wt=4)
        self.G.add_edge('A', 'D', wt=5)
        self.G.add_edge('B', 'C', wt=9)
        self.G.add_edge('D', 'C', wt=2)            

    def testAStar1(self):
        heuristic = graph.heuristics.euclidean()
        heuristic.optimize(self.G)
        result = graph.minmax.heuristic_search(self.G, 'A', 'C', heuristic )
        assert result == ['A', 'D', 'C']