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
python-graph

Unit tests for python-graph
"""


# Imports
import unittest
import pygraph
from pygraph.algorithms.searching import depth_first_search, breadth_first_search
from pygraph.algorithms import filters


class test_find_filter(unittest.TestCase):

    def testEmptyGraphBFS(self):
        G = pygraph.graph()
        st, lo = breadth_first_search(G, filter=filters.find(5))
        assert st == {}
        assert lo == []
    
    def testGraphBFS(self):
        G = pygraph.graph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(1, 5)
        G.add_edge(3, 5)
        st, lo = breadth_first_search(G, 1, filter=filters.find(5))
        assert st == {1: None, 2: 1, 5: 1}
    
    def testDigraphBFS(self):
        G = pygraph.digraph()
        G.add_nodes([1, 2, 3, 4, 5, 6])
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 3)
        G.add_edge(5, 1)
        G.add_edge(3, 5)
        G.add_edge(5, 6)
        st, lo = breadth_first_search(G, 1, filter=filters.find(5))
        assert st == {1: None, 2: 1, 3: 1, 4: 2, 5: 3}

    def testEmptyGraphDFS(self):
        G = pygraph.graph()
        st, pre, post = depth_first_search(G)
        assert st == {}
        assert pre == []
        assert post == []
    
    def testGraphDFS(self):
        G = pygraph.graph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(1, 5)
        G.add_edge(3, 5)
        st, pre, post = depth_first_search(G, 1, filter=filters.find(5))
        assert st == {1: None, 2: 1, 3: 2, 5: 3}
        st, pre, post = depth_first_search(G, 1, filter=filters.find(2))
        assert st == {1: None, 2: 1}

    
    def testDigraphDFS(self):
        G = pygraph.digraph()
        G.add_nodes([1, 2, 3, 4, 5, 6])
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 3)
        G.add_edge(5, 1)
        G.add_edge(3, 5)
        G.add_edge(5, 6)
        st, pre, post = depth_first_search(G, 1, filter=filters.find(5))
        assert st == {1: None, 2: 1, 3: 4, 4: 2, 5: 3}


class test_radius_filter(unittest.TestCase):

    def setUp(self):
        pass

    def testEmptyGraphBFS(self):
        G = pygraph.graph()
        st, lo = breadth_first_search(G, filter=filters.radius(2))
        assert st == {}
        assert lo == []
    
    def testGraphBFS(self):
        G = pygraph.graph()
        G.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(3, 5)
        G.add_edge(4, 6)
        G.add_edge(5, 7)
        G.add_edge(1, 8, wt=3)
        G.add_edge(8, 9)
        G.add_edge(3, 9)
        st, lo = breadth_first_search(G, 1, filter=filters.radius(2))
        assert st == {1: None, 2: 1, 3: 1, 4: 2, 5: 3, 9: 3}
    
    def testDigraphBFS(self):
        G = pygraph.digraph()
        G.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(3, 5)
        G.add_edge(4, 6)
        G.add_edge(5, 7)
        G.add_edge(1, 8, wt=3)
        G.add_edge(7, 8, wt=3)
        G.add_edge(8, 9)
        G.add_edge(3, 9)
        st, lo = breadth_first_search(G, 1, filter=filters.radius(2))
        assert st == {1: None, 2: 1, 3: 1, 4: 2, 5: 3, 9: 3}
        st, lo = breadth_first_search(G, 7, filter=filters.radius(2))
        assert st == {7: None}

    def testEmptyGraphDFS(self):
        G = pygraph.graph()
        st, pre, post = depth_first_search(G, filter=filters.radius(2))
        assert st == {}
        assert pre == []
        assert post == []
    
    def testGraphDFS(self):
        G = pygraph.graph()
        G.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(3, 5)
        G.add_edge(4, 6)
        G.add_edge(5, 7)
        G.add_edge(1, 8, wt=3)
        G.add_edge(8, 9)
        G.add_edge(3, 9)
        st, pre, post = depth_first_search(G, 1, filter=filters.radius(2))
        assert st == {1: None, 2: 1, 3: 1, 4: 2, 5: 3, 9: 3}
    
    def testDigraphDFS(self):
        G = pygraph.digraph()
        G.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(3, 5)
        G.add_edge(4, 6)
        G.add_edge(5, 7)
        G.add_edge(1, 8, wt=3)
        G.add_edge(7, 8, wt=3)
        G.add_edge(8, 9)
        G.add_edge(3, 9)
        st, pre, post = depth_first_search(G, 1, filter=filters.radius(2))
        assert st == {1: None, 2: 1, 3: 1, 4: 2, 5: 3, 9: 3}
        st, pre, post = depth_first_search(G, 7, filter=filters.radius(2))
        assert st == {7: None}