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
Unittests for graph.classes.hypergraph
"""


import unittest
import pygraph
from pygraph.algorithms.generators import generate
from pygraph.classes.exceptions import AdditionError
from pygraph.classes.hypergraph import hypergraph
import testlib
from copy import copy

class test_hypergraph(unittest.TestCase):

    # Add/Remove nodes and edges
    
    def test_raise_exception_on_duplicate_node_addition(self):
        gr = hypergraph()
        gr.add_node('a_node')
        try:
            gr.add_node('a_node')
        except AdditionError:
            pass
        else:
            fail()

    def test_raise_exception_on_duplicate_edge_link(self):
        gr = hypergraph()
        gr.add_node('a node')
        gr.add_hyperedge('an edge')
        gr.link('a node', 'an edge')
        try:
            gr.link('a node', 'an edge')
        except AdditionError:
            pass
        else:
            fail()
    
    def test_raise_exception_when_edge_added_from_non_existing_node(self):
        gr = hypergraph()
        gr.add_nodes([0,1])
        try:
            gr.link(3,0)
        except KeyError:
            pass
        else:
            fail()
        assert gr.neighbors(0) == set([])
    
    def test_raise_exception_when_edge_added_to_non_existing_node(self):
        gr = hypergraph()
        gr.add_nodes([0,1])
        try:
            gr.link(0,3)
        except KeyError:
            pass
        else:
            fail()
        assert gr.neighbors(0) == set([])
    
    def test_remove_node(self):
        gr = testlib.new_hypergraph()
        gr.del_node(0)
        self.assertTrue(0 not in gr.nodes())
        for e in gr.hyperedges():
            for n in gr.links(e):
                self.assertTrue(n in gr.nodes())
    
    def test_remove_link_from_node_to_same_node(self):
        gr = hypergraph()
        gr.add_node(0)
        gr.add_hyperedge(0)
        gr.link(0, 0)
        gr.unlink(0, 0)
    
    def test_remove_node_with_edge_to_itself(self):
        gr = hypergraph()
        gr.add_node(0)
        gr.add_hyperedge(0)
        gr.link(0, 0)
        gr.del_node(0)


if __name__ == "__main__":
    unittest.main()
