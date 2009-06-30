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
Unittests for graph.classes.Graph
"""


import unittest
import pygraph
from pygraph.algorithms.generators import generate
import testlib
import copy

class testGraph(unittest.TestCase):

    def setUp(self):
        pass

    def testRandomGraph(self):
        gr = generate(100, 500)
        self.assertEqual(gr.nodes(),range(100))
        self.assertEqual(len(gr.edges()), 500*2)
        for each, other in gr.edges():
            self.assertTrue(each in gr)
            self.assertTrue(other in gr)
    
    def testRandomEmptyGraph(self):
        gr = generate(0,0)
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testNodeRemoval(self):
        gr = testlib.new_graph()
        gr.del_node(0)
        self.assertTrue(0 not in gr)
        for each, other in gr.edges():
            self.assertTrue(each in gr)
            self.assertTrue(other in gr)

    def testGraphInverse(self):
        gr = testlib.new_graph()
        inv = gr.inverse()
        for each in gr.edges():
            self.assertTrue(each not in inv.edges())
        for each in inv.edges():
            self.assertTrue(each not in gr.edges())
    
    def testEmptyGraphInverse(self):
        gr = pygraph.graph()
        inv = gr.inverse()
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testGraphComplete(self):
        gr = pygraph.graph()
        gr.add_nodes(xrange(10))
        gr.complete()
        for i in xrange(10):
            for j in range(10):
                self.assertTrue((i, j) in gr.edges() or i == j)
    
    def testEmptyGraphComplete(self):
        gr = pygraph.graph()
        gr.complete()
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testGraphWithOneNodeComplete(self):
        gr = pygraph.graph()
        gr.add_node(0)
        gr.complete()
        self.assertTrue(gr.nodes() == [0])
        self.assertTrue(gr.edges() == [])
    
    def testAddGraph(self):
        gr1 = testlib.new_graph()
        gr2 = testlib.new_graph()
        gr1.add_graph(gr2)
        for each in gr2.nodes():
            self.assertTrue(each in gr1)
        for each in gr2.edges():
            self.assertTrue(each in gr1.edges())
    
    def testAddEmptyGraph(self):
        gr1 = testlib.new_graph()
        gr1c = copy.copy(gr1)
        gr2 = pygraph.graph()
        gr1.add_graph(gr2)
        self.assertTrue(gr1.nodes() == gr1c.nodes())
        self.assertTrue(gr1.edges() == gr1c.edges())
    
    def testAddSpanningTree(self):
        gr = pygraph.graph()
        st = {0: None, 1: 0, 2:0, 3: 1, 4: 2, 5: 3}
        gr.add_spanning_tree(st)
        for each in st:
            self.assertTrue((each, st[each]) in gr.edges() or (each, st[each]) == (0, None))
            self.assertTrue((st[each], each) in gr.edges() or (each, st[each]) == (0, None))

    def testAddEmptySpanningTree(self):
        gr = pygraph.graph()
        st = {}
        gr.add_spanning_tree(st)
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testEdgeToItselfRemoval(self):
        gr = pygraph.graph()
        gr.add_node(0)
        gr.add_edge(0, 0)
        gr.del_edge(0, 0)
    
    def testNodeWithEdgeToItselfRemoval(self):
        gr = pygraph.graph()
        gr.add_node(0)
        gr.add_edge(0, 0)
        gr.del_node(0)
        
    def testTrivalEquality0(self):
        gr1 = pygraph.graph()
        gr2 = pygraph.graph()
        assert gr1 == gr2, "All zero node graphs should be equivalent to each other."
    
    def testTrivalEquality1(self):
        gr1 = pygraph.graph()
        gr1.add_node(0)
        gr2 = pygraph.graph()
        gr2.add_node(0)
        assert gr1 == gr2, "All one node graphs should be equivalent to each other."
    
    def testTrivalEquality2(self):
        gr1 = pygraph.graph()
        gr1.add_node(0)
        gr1.add_node(1)
        gr1.add_edge(0,1)
        gr2 = pygraph.graph()
        gr2.add_node(0)
        gr2.add_node(1)
        gr2.add_edge(0,1)
        assert gr1 == gr2, "Two identically constructed graphs should be equivalent to each other."
