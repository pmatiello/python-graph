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
Unittests for graph.classes.Digraph
"""


import unittest
import pygraph
import copy

class testGraph(unittest.TestCase):

    def setUp(self):
        pass

    def testRandomGraph(self):
        gr = pygraph.digraph()
        gr.generate(100, 500)
        self.assertEqual(gr.nodes(),range(100))
        self.assertEqual(len(gr.edges()), 500)
        for each, other in gr.edges():
            self.assertTrue(each in gr)
            self.assertTrue(other in gr)
    
    def testRandomEmptyGraph(self):
        gr = pygraph.digraph()
        gr.generate(0,0)
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testNodeRemoval(self):
        gr = pygraph.digraph()
        gr.generate(10, 90)
        gr.del_node(0)
        self.assertTrue(0 not in gr)
        for each, other in gr.edges():
            self.assertTrue(each in gr)
            self.assertTrue(other in gr)

    def testGraphInverse(self):
        gr = pygraph.digraph()
        gr.generate(50, 300)
        inv = gr.inverse()
        for each in gr.edges():
            self.assertTrue(each not in inv.edges())
        for each in inv.edges():
            self.assertTrue(each not in gr.edges())
    
    def testEmptyGraphInverse(self):
        gr = pygraph.digraph()
        inv = gr.inverse()
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testGraphComplete(self):
        gr = pygraph.digraph()
        gr.add_nodes(xrange(10))
        gr.complete()
        for i in xrange(10):
            for j in range(10):
                self.assertTrue((i, j) in gr.edges() or i == j)
    
    def testEmptyGraphComplete(self):
        gr = pygraph.digraph()
        gr.complete()
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testGraphWithOneNodeComplete(self):
        gr = pygraph.digraph()
        gr.add_node(0)
        gr.complete()
        self.assertTrue(gr.nodes() == [0])
        self.assertTrue(gr.edges() == [])
    
    def testAddGraph(self):
        gr1 = pygraph.digraph()
        gr1.generate(25, 100)
        gr2 = pygraph.digraph()
        gr2.generate(40, 200)
        gr1.add_graph(gr2)
        for each in gr2.nodes():
            self.assertTrue(each in gr1)
        for each in gr2.edges():
            self.assertTrue(each in gr1.edges())
    
    def testAddEmptyGraph(self):
        gr1 = pygraph.digraph()
        gr1.generate(25, 100)
        gr1c = copy.copy(gr1)
        gr2 = pygraph.digraph()
        gr1.add_graph(gr2)
        self.assertTrue(gr1.nodes() == gr1c.nodes())
        self.assertTrue(gr1.edges() == gr1c.edges())
    
    def testAddSpanningTree(self):
        gr = pygraph.digraph()
        st = {0: None, 1: 0, 2:0, 3: 1, 4: 2, 5: 3}
        gr.add_spanning_tree(st)
        for each in st:
            self.assertTrue((st[each], each) in gr.edges() or (each, st[each]) == (0, None))

    def testAddEmptySpanningTree(self):
        gr = pygraph.digraph()
        st = {}
        gr.add_spanning_tree(st)
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
        

# Run tests
if __name__ == '__main__':
    unittest.main()
