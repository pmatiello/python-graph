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
Unittests for graph.algorithms.searching
"""


# Imports
import unittest
import pygraph
from pygraph.algorithms.searching import depth_first_search, breadth_first_search


class test_depth_first_search(unittest.TestCase):

    def setUp(self):
        pass

    def testEmptyGraph(self):
        G = pygraph.graph()
        st, pre, post = depth_first_search(G)
        assert st == {}
        assert pre == []
        assert post == []
    
    def testGraph(self):
        G = pygraph.graph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(1, 5)
        G.add_edge(3, 5)
        st, pre, post = depth_first_search(G)
        assert st == {1: None, 2: 1, 3: 2, 4: 5, 5: 3}
        assert pre == [1, 2, 3, 5, 4]
        assert post == [4, 5, 3, 2, 1]
    
    def testSanityGraph(self):
        G = pygraph.graph()
        G.generate(100, 500)
        st, pre, post = depth_first_search(G)
        for each in G:
            if (st[each] != None):
                assert pre.index(each) > pre.index(st[each])
                assert post.index(each) < post.index(st[each])

    def testEmptyDigraph(self):
        G = pygraph.digraph()
        st, pre, post = depth_first_search(G)
        assert st == {}
        assert pre == []
        assert post == []
    
    def testDigraph(self):
        G = pygraph.digraph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(1, 5)
        G.add_edge(3, 5)
        st, pre, post = depth_first_search(G)
        assert st == {1: None, 2: 1, 3: 2, 4: 2, 5: 3}
        assert pre == [1, 2, 3, 5, 4]
        assert post == [5, 3, 4, 2, 1]
    
    def testSanityDigraph(self):
        G = pygraph.digraph()
        G.generate(100, 500)
        st, pre, post = depth_first_search(G)
        for each in G:
            if (st[each] != None):
                assert pre.index(each) > pre.index(st[each])
                assert post.index(each) < post.index(st[each])


class test_breadth_first_search(unittest.TestCase):

    def setUp(self):
        pass

    def testEmptyGraph(self):
        G = pygraph.graph()
        st, lo = breadth_first_search(G)
        assert st == {}
        assert lo == []
    
    def testGraph(self):
        G = pygraph.graph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(1, 5)
        G.add_edge(3, 5)
        st, lo = breadth_first_search(G, 1)
        assert st == {1: None, 2: 1, 3: 2, 4: 2, 5: 1}
        assert lo == [1, 2, 5, 3, 4]
    
    def testSanityGraph(self):
        G = pygraph.graph()
        G.generate(100, 500)
        st, lo = breadth_first_search(G)
        for each in G:
            if (st[each] != None):
                assert lo.index(each) > lo.index(st[each])

    def testEmptyDigraph(self):
        G = pygraph.digraph()
        st, lo = breadth_first_search(G)
        assert st == {}
        assert lo == []
    
    def testDigraph(self):
        G = pygraph.digraph()
        G.add_nodes([1, 2, 3, 4, 5])
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(2, 4)
        G.add_edge(4, 5)
        G.add_edge(1, 5)
        G.add_edge(3, 5)
        st, lo = breadth_first_search(G)
        assert st == {1: None, 2: 1, 3: 2, 4: 2, 5: 1}
        assert lo == [1, 2, 5, 3, 4]
    
    def testSanityDigraph(self):
        G = pygraph.digraph()
        G.generate(100, 500)
        st, lo = breadth_first_search(G)
        for each in G:
            if (st[each] != None):
                assert lo.index(each) > lo.index(st[each])