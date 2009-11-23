import unittest
import testlib
from copy import copy
from pygraph.classes.dict_digraph import dict_digraph, Node
from pygraph.classes.exceptions import AdditionError, DeletionError
from pygraph.classes.graph import graph

class test_new_digraph( unittest.TestCase ):
    # Add/Remove nodes and edges
    
    def setUp(self):
        self._gr = {}
    
    def test_raise_exception_on_duplicate_node_addition(self):
        gr = dict_digraph( self._gr )
        gr.add_node('a_node')
        try:
            gr.add_node('a_node')
        except AdditionError as ae:
            return
        except Exception as e:
            fail("Expected an AdditionError, got %s" % repr(e) )
        else:
            self.fail("Should have raised an AdditionError")

    def test_raise_exception_on_duplicate_edge_addition(self):
        gr = dict_digraph( self._gr )
        gr.add_node('a_node')
        gr.add_node('other_node')
        gr.add_edge(("a_node","other_node"))
        try:
            gr.add_edge(("a_node","other_node"))
        except AdditionError:
            pass
        else:
            self.fail()
    
    def test_raise_exception_when_edge_added_from_non_existing_node(self):
        gr = dict_digraph( self._gr )
        gr.add_nodes([0,1])
        try:
            gr.add_edge((3,0))
        except AdditionError:
            pass
        else:
            self.fail("The graph allowed an edge to be added from a non-existing node.")
            
        assert len(gr.neighbors(0)) == 0
        assert len(gr.neighbors(1)) == 0    
    
    def test_in(self):
        gr = dict_digraph( {} )
        gr.add_node(0)
        assert 0 in gr
        
    def test_remove_node1(self):
        gr = dict_digraph( {} )
        gr.add_node(0)
        gr.add_node(1)
        gr.add_edge((0,1))
        gr.del_node(0)
        assert len([a for a in gr.edges()]) == 0
        
    def test_remove_node2(self):
        gr = dict_digraph( {} )
        gr.add_node(0)
        gr.add_node(1)
        gr.add_edge((1,0))
        gr.del_node(0)
        assert len([a for a in gr.edges()]) == 0

    def test_remove_node3(self):
        gr = testlib.new_dict_digraph()
        gr.del_node(0)
        self.assertTrue(0 not in gr)
        
        for (u, v) in gr.edges():
            assert u in gr, "v: %s is not in Graph: %s" % (v, gr)
            
            try:
                assert v in gr, "u: %s is not in Graph: %s" % (u, gr)
            except Exception as e:
                import pdb
                pdb.set_trace()
    
    def test_remove_edge_from_node_to_same_node(self):
        gr = dict_digraph( self._gr )
        gr.add_node(0)
        e = (0,0)
        gr.add_edge(e)
        assert gr.has_edge(e) 
        gr.del_edge((0, 0))
    
    def test_remove_node_with_edge_to_itself(self):
        gr = dict_digraph( self._gr )
        gr.add_node(0)
        gr.add_edge((0, 0))
        gr.del_node(0)

    
    # Invert graph
    
    def test_invert_digraph(self):
        gr = testlib.new_digraph()
        inv = gr.inverse()
        for each in gr.edges():
            self.assertTrue(each not in inv.edges())
        for each in inv.edges():
            self.assertTrue(each not in gr.edges())
    
    def test_invert_empty_digraph(self):
        gr = dict_digraph( self._gr )
        inv = gr.inverse()
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    
    # Reverse graph
    def test_reverse_digraph(self):
        gr = dict_digraph( self._gr )
        rev = gr.reverse()
        for (u, v) in gr.edges():
            self.assertTrue((v, u) in rev.edges())
        for (u, v) in rev.edges():
            self.assertTrue((v, u) in gr.edges())
    
    def test_invert_empty_digraph(self):
        gr = dict_digraph( self._gr )
        rev = gr.reverse()
        self.assertEqual( len(list(rev.nodes())), 0 )
        self.assertEqual( len(list(rev.edges())), 0 )
    
    # Complete graph
    
    def test_complete_digraph(self):
        gr = dict_digraph( self._gr )
        gr.add_nodes(range(10))
        gr.complete()
        
        all_edges = [ e for e in gr.edges() ]
        
        for i in range(10):
            for j in range(10):
                e = (i,j)
                if not i==j:
                    assert e in all_edges
                    assert gr.has_edge(e)
                else:
                    assert not e in all_edges
                    assert not gr.has_edge(e)
    
    def test_complete_empty_digraph(self):
        gr = dict_digraph( self._gr )
        gr.complete()
        self.assertEqual
        self.assertEqual( len(gr.nodes()), 0 )
        self.assertEqual( len(list(gr.edges())), 0 )
    
    def test_complete_digraph_with_one_node(self):
        gr = dict_digraph( self._gr )
        gr.add_node(0)
        gr.complete()
        self.assertEqual( len(gr), 1 )
        
        all_edges = [e for e in gr.edges() ]

        self.assertEqual( len( all_edges ), 0 )
    
    # Add graph
    
    def test_add_digraph(self):
        gr1 = testlib.new_digraph()
        gr2 = testlib.new_digraph()
        gr1.add_graph(gr2)
        for each in gr2.nodes():
            self.assertTrue(each in gr1)
        for each in gr2.edges():
            self.assertTrue(each in gr1.edges())
    
    def test_add_empty_digraph(self):
        gr1 = testlib.new_digraph()
        gr1c = copy(gr1)
        gr2 = dict_digraph()
        gr1.add_graph(gr2)
        self.assertTrue(gr1.nodes() == gr1c.nodes())
        self.assertTrue(gr1.edges() == gr1c.edges())
    
    def test_add_graph_into_diagraph(self):
        d = dict_digraph()
        g = graph()
        
        A = "A"
        B = "B"
        
        g.add_node( A )
        g.add_node( B )
        g.add_edge( (A,B) )
        
        d.add_graph( g )
        
        assert d.has_node( A )
        assert d.has_node( B )
        assert d.has_edge( (A,B) )
        assert d.has_edge( (B,A) )    
    
    # Add spanning tree
    
    def test_add_spanning_tree(self):
        gr = dict_digraph()
        st = {0: None, 1: 0, 2:0, 3: 1, 4: 2, 5: 3}
        gr.add_spanning_tree(st)
        for each in st:
            self.assertTrue((st[each], each) in gr.edges() or (each, st[each]) == (0, None))

    def test_add_empty_spanning_tree(self):
        gr = dict_digraph()
        st = {}
        gr.add_spanning_tree(st)
        assert len( [a for a in gr.nodes() ] ) == 0
        assert len( [a for a in gr.edges() ] ) == 0
#        
    def test_repr(self):
        """
        Validate the repr string
        """
        gr = dict_digraph( self._gr )
        gr_repr = repr( gr )
        assert isinstance(gr_repr, str )
        assert gr.__class__.__name__ in gr_repr
        
        gr.add_node(0)
        gr.add_node(1)
        
        gr.add_edge((0,1))
        gr_repr = repr(gr)
    
    def test_order_len_equivlance(self):
        """
        Verify the behavior of G.order()
        """
        gr = testlib.new_graph()
        assert len(gr) == gr.order()
        assert gr.order() == len( gr.node_neighbors )
    
if __name__ == "__main__":
    unittest.main()