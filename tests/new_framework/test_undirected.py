class test_undirected:
    """
    Tests which apply only to undirected graphs
    """
    
    @staticmethod
    def is_odd( num ):
        if num % 2 > 0:
            return True
        return False
    
    def test_vertex_edge_count1(self):
        """
        For any graph G, the sum of the degrees of the verteces of G
        equals twice the number of edges of G.
        """
        sum_of_the_degrees = sum( [ len( self.G[a] ) for a in self.G ] )
        number_of_edges = len( self.G.edges() )
        assert sum_of_the_degrees == number_of_edges * 2
        
    def test_vertex_odd_even(self):
        """
        Every graph contains an even number of odd verteces.
        """
        odd_verteces = [ v for v in self.G if self.is_odd( len(self.G[v]) ) ]
        assert not self.is_odd( len( odd_verteces ) )
        