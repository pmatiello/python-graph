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
Unittests for graph.algorithms.readwrite
"""


import unittest
import pygraph
import time

class test_readwrite(unittest.TestCase):

    def _check_nodes(self, gr, dot):
        dot = dot.split("\n")
        for node in gr:
            assert str(node) + ";" in dot;

    def _check_edges(self, gr, dot):
        dot = dot.split("\n")
        for node in gr:
            for edge in gr[node]: 
                assert ((str(node) + " -- " + str(edge) + ";" in dot) or
                        (str(edge) + " -- " + str(node) + ";" in dot))

    def _check_arrows(self, gr, dot):
        dot = dot.split("\n")
        for node in gr:
            for edge in gr[node]: 
                assert str(node) + " -> " + str(edge) + ";" in dot
    
    def testWriteGraphDot(self):
        gr = pygraph.graph()
        gr.add_nodes([1, 2, 3, 4, 5])
        gr.add_edge(1, 2)
        gr.add_edge(2, 3)
        gr.add_edge(2, 4)
        gr.add_edge(4, 5)
        gr.add_edge(1, 5)
        gr.add_edge(3, 5)
        dot = gr.write('dot')
        self._check_nodes(gr, dot)
        self._check_edges(gr, dot)
    
    def testWriteDigraphDot(self):
        gr = pygraph.digraph()
        gr.add_nodes([1, 2, 3, 4, 5])
        gr.add_edge(1, 2)
        gr.add_edge(2, 3)
        gr.add_edge(2, 4)
        gr.add_edge(4, 5)
        gr.add_edge(1, 5)
        gr.add_edge(3, 5)
        dot = gr.write('dot')
        self._check_nodes(gr, dot)
        self._check_arrows(gr, dot)
 

    def testReadGraphDot(self):
        dot = ['graph graphname {', '1;', '2;', '3;', '4;', '5;', '1 -- 2;', '3 -- 2;', '4 -- 5;', '1 -- 5;', '4 -- 2;', '5 -- 3;', '}', '']
        dot = "\n".join(dot)
        gr = pygraph.graph()
        gr.read(dot, 'dot')
        self._check_nodes(gr, dot)
        self._check_edges(gr, dot)
    
    def testReadDigraphDot(self):
        dot = ['digraph graphname {', '1;', '2;', '3;', '4;', '5;', '1 -> 2;', '4 -> 5;', '1 -> 5;', '2 -> 3;', '2 -> 4;', '3 -> 5;', '}', '']
        dot = "\n".join(dot)
        gr = pygraph.digraph()
        gr.read(dot, 'dot')
        self._check_nodes(gr, dot)
        self._check_arrows(gr, dot)
