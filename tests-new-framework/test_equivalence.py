class test_equivalence( object ):
    
    def testEquivalenceTrue(self):
        """
        Test that two identically constructed graphs are considered equal.
        """
        F = self.makeTestGraph()
        assert self.G == F, "Two identically constructed graphs should be identical."
        
        