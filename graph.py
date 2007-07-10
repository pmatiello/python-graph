# Copyright (c) 2007 Pedro Matiello <pmatiello@gmail.com>
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
A library for working with graphs in Python.
"""

import __python_graph_algorithms__ as _algorithms

class graph:
	"""
	Graph class.
	Data structure is built on __init__.
	Basic operations are defined in this file.
	Algorithms should refer to external files.
	"""


	def __init__(self):
		"""
		Initialize a graph.
		Data structure is defined here.
		"""
		self.nodes = []		# This is an adjacency list


	def __str__(self):
		"""
		Return a string representing the graph when requested by str() (or print).
		"""
		return str(self.nodes)


	def __len__(self):
		"""
		Return the size of the graph when requested by len().
		"""
		return len(self.nodes)


	def get_nodes(self):
		"""
		Return node list.
		"""
		return self.nodes


	def get_node(self, node):
		"""
		Return requested node.
		"""
		return self.nodes[node]


	def add_nodes(self, num):
		"""
		Create num nodes.
		"""
		while (num > 0):
			self.nodes.append([])
			num = num - 1


	def add_edge(self, u, v):
		"""
		Add an edge (u,v) to the graph connecting nodes u and v.
		Warning: this function should not be used in directed graphs: use add_arrow() instead.
		"""
		if (v not in self.nodes[u]):
			self.nodes[u].append(v)
			self.nodes[v].append(u)


	def add_arrow(self, u, v):
		"""
		Add an arrow (u,v) to the directed graph connecting node u to node v.
		"""
		if (v not in self.nodes[u]):
			self.nodes[u].append(v)


	def del_edge(self, u, v):
		"""
		Remove an edge (u, v) from the graph.
		Warning: this function should not be used in directed graphs: use del_arrow() instead.
		"""
		if (v in self.nodes[u]):
			self.nodes[u].remove(v)
			self.nodes[v].remove(u)


	def del_arrow(self, u, v):
		"""
		Remove an arrow (u, v) from the directed graph.
		"""
		if (v in self.nodes[u]):
			self.nodes[u].remove(v)


	depth_first_search = _algorithms.searching.depht_first_search
