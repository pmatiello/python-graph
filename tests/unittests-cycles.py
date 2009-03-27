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
Unittests for graph.algorithms.cycles
"""


import unittest
import graph


class test_find_cycle(unittest.TestCase):

    def setUp(self):
        pass

    def testGraph(self):
        G = graph.graph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(1, 5)
        G.add_edge(3, 5)
        # Cycles: 1-2-4-5, 3-2-4-5 and 1-2-3-5
        assert G.find_cycle() == [2,3,5,4]

    def testNoCycleGraph(self):
        G = graph.graph()
        G.add_nodes([1,2,3])
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        assert G.find_cycle() == []

    def testDigraph(self):
        G = graph.digraph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(5, 1)
        # Cycle: 1-2-4-5
        assert G.find_cycle() == [1,2,4,5]
    
    def testNoCycleDigraph(self):
        G = graph.digraph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(3, 5)
        assert G.find_cycle() == []
    
    def testNoCycleDigraph2(self):
        G = graph.digraph()
        G.add_nodes([1,2,3])
        G.add_edge(1,2)
        G.add_edge(1,3)
        G.add_edge(2,3)
        print G.find_cycle()
    

    def testMisleadingDigraph(self):
        G = graph.digraph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(3, 5)
        G.add_edge(3, 1)
        assert G.find_cycle() == [1, 2, 3]
    
    def testSmallCycleDigraph(self):
        G = graph.digraph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(2, 1)
        # Cycle: 1-2
        assert G.find_cycle() == [1,2]
