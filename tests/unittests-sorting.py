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
Unittests for graph.algorithms.sorting
"""


import unittest
import graph


class test_topological_sorting(unittest.TestCase):

    def testTree(self):
        gr = graph.digraph()
        gr.add_nodes([0,1,2,3,4,5,6,7,8])
        gr.add_edge(0,1)
        gr.add_edge(0,2)
        gr.add_edge(1,3)
        gr.add_edge(1,4)
        gr.add_edge(2,5)
        gr.add_edge(2,6)
        gr.add_edge(3,7)
        gr.add_edge(8,0)
        ts = gr.topological_sorting()
        assert ts.index(8) < ts.index(0)
        assert ts.index(1) > ts.index(0)
        assert ts.index(2) > ts.index(0)
        assert ts.index(3) > ts.index(1)
        assert ts.index(4) > ts.index(1)
        assert ts.index(5) > ts.index(2)
        assert ts.index(6) > ts.index(2)
        assert ts.index(7) > ts.index(3)
    
    def testDigraph(self):
        
        def has_parent(node, list):
            for each in list:
                if gr.has_edge(each, node):
                    return True
            return (ts == [])
            
        gr = graph.digraph()
        gr.add_nodes([0,1,2,3,4,5,6,7,8])
        gr.add_edge(0,1)
        gr.add_edge(0,2)
        gr.add_edge(1,3)
        gr.add_edge(1,4)
        gr.add_edge(2,5)
        gr.add_edge(2,6)
        gr.add_edge(3,7)
        gr.add_edge(8,0)
        gr.add_edge(7,5)
        gr.add_edge(3,0)
        gr.add_edge(4,3)
        gr.add_edge(2,7)
        gr.add_edge(6,0)
        ts = gr.topological_sorting()
        while (ts):
            x = ts.pop()
            assert has_parent(x, ts)