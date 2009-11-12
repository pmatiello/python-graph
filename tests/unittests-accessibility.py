# Copyright (c) Pedro Matiello <pmatiello@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


"""
Unittests for graph.algorithms.accessibility
"""


import unittest
import pygraph
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms.accessibility import accessibility
from pygraph.algorithms.accessibility import mutual_accessibility
from pygraph.algorithms.accessibility import connected_components
from pygraph.classes.hypergraph import hypergraph
import testlib

class test_accessibility(unittest.TestCase):

    def setUp(self):
        pass

    def test_mutual_accessibility_in_digraph(self):
        gr = testlib.new_digraph()
        
        ma = mutual_accessibility(gr)
        for n in gr:
            for m in gr:
                if (m in ma[n]):
                    assert m in depth_first_search(gr, n)[0]
                    assert n in depth_first_search(gr, m)[0]
                else:
                    assert m not in depth_first_search(gr, n)[0] or n not in depth_first_search(gr, m)[0]

    def test_accessibility_hypergraph(self):
        gr = hypergraph()
        
        # Add some nodes / edges
        gr.add_nodes(range(8))
        gr.add_hyperedges(['a', 'b', 'c'])
        
        # Connect the 9 nodes with three size-3 hyperedges
        for node_set in [['a',0,1,2], ['b',2,3,4], ['c',5,6,7]]:
            for node in node_set[1:]:
                gr.link(node, node_set[0])
        
        access = accessibility(gr)
        
        assert 8 == len(access)
        
        for i in xrange(5):
            assert set(access[i]) == set(xrange(5))
        
        for i in xrange(5,8):
            assert set(access[i]) == set(xrange(5,8))
        
    def test_connected_components_hypergraph(self):
        gr = hypergraph()
        
        # Add some nodes / edges
        gr.add_nodes(range(9))
        gr.add_hyperedges(['a', 'b', 'c'])
        
        # Connect the 9 nodes with three size-3 hyperedges
        for node_set in [['a',0,1,2], ['b',3,4,5], ['c',6,7,8]]:
            for node in node_set[1:]:
                gr.link(node, node_set[0])
        
        cc = connected_components(gr)
        
        assert 3 == len(set(cc.values()))
        
        assert cc[0] == cc[1] and cc[1] == cc[2]
        assert cc[3] == cc[4] and cc[4] == cc[5]
        assert cc[6] == cc[7] and cc[7] == cc[8]
        
        
        # Do it again with two components and more than one edge for each
        gr = hypergraph()
        gr.add_nodes(range(9))
        gr.add_hyperedges(['a', 'b', 'c', 'd'])
        
        for node_set in [['a',0,1,2], ['b',2,3,4], ['c',5,6,7], ['d',6,7,8]]:
            for node in node_set[1:]:
                gr.link(node, node_set[0])
        
        cc = connected_components(gr)
        
        assert 2 == len(set(cc.values()))
        
        for i in [0,1,2,3]:
            assert cc[i] == cc[i+1]
        
        for i in [5,6,7]:
            assert cc[i] == cc[i+1]
            
        assert cc[4] != cc[5]
        
if __name__ == "__main__":
    unittest.main()
