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
from pygraph.readwrite import *
import time

class test_readwrite_dot(unittest.TestCase):

    def _check_nodes(self, gr, dot):
        dot = dot.split("\n")
        for node in gr:
            assert str(node) + ";" in dot

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
        dotstr = dot.write(gr)
        self._check_nodes(gr, dotstr)
        self._check_edges(gr, dotstr)

    def testWriteDigraphDot(self):
        gr = pygraph.digraph()
        gr.add_nodes([1, 2, 3, 4, 5])
        gr.add_edge(1, 2)
        gr.add_edge(2, 3)
        gr.add_edge(2, 4)
        gr.add_edge(4, 5)
        gr.add_edge(1, 5)
        gr.add_edge(3, 5)
        dotstr = dot.write(gr)
        self._check_nodes(gr, dotstr)
        self._check_arrows(gr, dotstr)

    def testReadGraphDot(self):
        dotstr = ['graph graphname {', '1;', '2;', '3;', '4;', '5;', '1 -- 2;', '3 -- 2;', '4 -- 5;', '1 -- 5;', '4 -- 2;', '5 -- 3;', '}', '']
        dotstr = "\n".join(dotstr)
        gr = dot.read(dotstr)
        self._check_nodes(gr, dotstr)
        self._check_edges(gr, dotstr)

    def testReadDigraphDot(self):
        dotstr = ['digraph graphname {', '1;', '2;', '3;', '4;', '5;', '1 -> 2;', '4 -> 5;', '1 -> 5;', '2 -> 3;', '2 -> 4;', '3 -> 5;', '}', '']
        dotstr = "\n".join(dotstr)
        gr = dot.read(dotstr)
        self._check_nodes(gr, dotstr)
        self._check_arrows(gr, dotstr)

class test_readwrite_markup(unittest.TestCase):

    def _check_nodes(self, gr, xml):
        xml = xml.split("\n")
        print xml
        for node in gr:
            ok = False
            for line in xml:
                if("node" in line and str(node) in line):
                    ok = True
            assert ok

    def _check_edges(self, gr, xml):
        xml = xml.split("\n")
        for node in gr:
            for edge in gr[node]:
                ok = False
                for line in xml:
                    if ("edge" in line and str(node) in line and str(edge) in line):
                        ok = True
                assert ok

    def testWriteGraphXML(self):
        gr = pygraph.graph()
        gr.add_nodes([1, 2, 3, 4, 5])
        gr.add_edge(1, 2)
        gr.add_edge(2, 3)
        gr.add_edge(2, 4)
        gr.add_edge(4, 5)
        gr.add_edge(1, 5)
        gr.add_edge(3, 5)
        xml = markup.write(gr)
        self._check_nodes(gr, xml)
        self._check_edges(gr, xml)

    def testWriteDigraphXML(self):
        gr = pygraph.digraph()
        gr.add_nodes([1, 2, 3, 4, 5])
        gr.add_edge(1, 2)
        gr.add_edge(2, 3)
        gr.add_edge(2, 4)
        gr.add_edge(4, 5)
        gr.add_edge(1, 5)
        gr.add_edge(3, 5)
        xml = markup.write(gr)
        self._check_nodes(gr, xml)
        self._check_edges(gr, xml)
        print xml

    def testReadGraphXML(self):
        xml = '<?xml version="1.0" ?> <digraph>     <node id="1"/>     <node id="2"/>     <node id="3"/>     <node id="4"/>     <node id="5"/>     <edge from="1" label="" to="2" wt="1"/>     <edge from="4" label="" to="5" wt="1"/>     <edge from="1" label="" to="5" wt="1"/>     <edge from="2" label="" to="3" wt="1"/>     <edge from="2" label="" to="4" wt="1"/>     <edge from="3" label="" to="5" wt="1"/> </digraph>'
        gr = markup.read(xml)
        self._check_nodes(gr, xml)
        self._check_edges(gr, xml)

    def testReadDigraphXML(self):
        xml = '<?xml version="1.0" ?> <digraph>     <node id="1"/>     <node id="2"/>     <node id="3"/>     <node id="4"/>     <node id="5"/>     <edge from="1" label="" to="2" wt="1"/>     <edge from="4" label="" to="5" wt="1"/>     <edge from="1" label="" to="5" wt="1"/>     <edge from="2" label="" to="3" wt="1"/>     <edge from="2" label="" to="4" wt="1"/>     <edge from="3" label="" to="5" wt="1"/> </digraph>'
        gr = markup.read(xml)
        self._check_nodes(gr, xml)
        self._check_edges(gr, xml)
