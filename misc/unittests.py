#!/usr/bin/python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
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
import sys
sys.path.append('..')
import graph
import unittest


# Tests
class testGraph(unittest.TestCase):

	def setUp(self):
		pass

	def testRandomGraph(self):
		gr = graph.graph()
		gr.generate(100, 500)
		self.assertEqual(gr.nodes(),range(100))
		self.assertEqual(len(gr.edges()), 500*2)
		for each, other in gr.edges():
			self.assert_(each in gr)
			self.assert_(other in gr)
	
	def testNodeRemoval(self):
		gr = graph.graph()
		gr.generate(10, 30)
		gr.del_node(0)
		self.assert_(0 not in gr)
		for each, other in gr.edges():
			self.assert_(each in gr)
			self.assert_(other in gr)

	def testGraphInverse(self):
		gr = graph.graph()
		gr.generate(100, 500)
		inv = gr.inverse()
	
	def testGraphComplete(self):
		gr = graph.graph()
		gr.add_nodes(xrange(10))
		gr.complete()
		for i in xrange(10):
			for j in range(10):
				self.assert_((i, j) in gr.edges() or i == j)
	
	def testAddGraph(self):
		gr1 = graph.graph()
		gr1.generate(25, 100)
		gr2 = graph.graph()
		gr2.generate(40, 200)
		gr1.add_graph(gr2)
		for each in gr2.nodes():
			self.assert_(each in gr1)
		for each in gr2.edges():
			self.assert_(each in gr1.edges())

# Run tests
if __name__ == '__main__':
    unittest.main()
